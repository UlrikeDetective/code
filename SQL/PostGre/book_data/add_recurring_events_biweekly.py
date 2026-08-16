"""Module for adding recurring events to High Tide Books database and web app.

This script manages recurring events (such as the bi-weekly 'Colourful Kitchen'
cooking workshop) for the High Tide Books application.

It supports three execution modes:
1. HTTP POST (default): Sends event data directly to the Express web app
   endpoint at http://localhost:3005/admin/add-event using urllib.
2. SQL Generator: Exports a .sql file containing SQL INSERT statements.
3. Direct DB: Connects directly to PostgreSQL using psycopg/psycopg2 if available.
"""

import argparse
from datetime import datetime, timedelta, time
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import List, Dict, Any, Optional

# Optional PostgreSQL library import
try:
    import psycopg2
    HAS_PSYCOPG2 = True
except ImportError:
    try:
        import psycopg as psycopg2  # Type: ignore
        HAS_PSYCOPG2 = True
    except ImportError:
        HAS_PSYCOPG2 = False


def load_dotenv(dotenv_path: Optional[str] = None) -> None:
    """Load environment variables from a .env file into os.environ.

    This function parses simple KEY=VALUE formatted lines from a .env file,
    stripping whitespace and surrounding quotes, without requiring external
    third-party dependencies. Existing environment variables are preserved.

    Args:
        dotenv_path: Filepath to the .env file. Defaults to '.env' in script dir.
    """
    if dotenv_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        dotenv_path = os.path.join(script_dir, ".env")

    if not os.path.exists(dotenv_path):
        return

    try:
        with open(dotenv_path, "r", encoding="utf-8") as env_file:
            for line in env_file:
                line_str = line.strip()
                # Skip blank lines and comment lines starting with '#'
                if not line_str or line_str.startswith("#"):
                    continue
                if "=" in line_str:
                    key, value = line_str.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    # Do not overwrite variables already set in os.environ
                    if key and key not in os.environ:
                        os.environ[key] = value
    except Exception as err:
        print(f"[WARN] Could not parse .env file at {dotenv_path}: {err}")


# Load environment credentials safely from .env file before defining constants
load_dotenv()

# Configuration Constants (PEP 8 UPPER_CASE) loaded safely from environment/.env
DEFAULT_DB_HOST = (
    os.getenv("PGHOST") or os.getenv("POSTGRES_HOST") or "localhost"
)
DEFAULT_DB_PORT = int(
    os.getenv("PGPORT") or os.getenv("POSTGRES_PORT") or "5432"
)
DEFAULT_DB_USER = (
    os.getenv("PGUSER") or os.getenv("POSTGRES_USER") or "postgres"
)
DEFAULT_DB_PASSWORD = (
    os.getenv("PGPASSWORD") or os.getenv("POSTGRES_PASSWORD") or ""
)
DEFAULT_DB_NAME = (
    os.getenv("PGDATABASE") or os.getenv("POSTGRES_DB") or "books"
)
DEFAULT_WEB_URL = (
    os.getenv("WEB_URL") or "http://localhost:3005/admin/add-event"
)

# Default event parameters for "Colourful Kitchen"
DEFAULT_EVENT_NAME = "Movie night"
DEFAULT_LOCATION = "the bookshop"
DEFAULT_DESCRIPTION = (
    "Bi-weekly Movie night."
)
DEFAULT_WEEKDAY = 6  # Monday (0 = Monday, 1 = Tuesday, 2 = Wednesday...)
DEFAULT_TIME = time(20, 0)  # 8:00 PM / 20:00

# Start date for the first event of this series (YYYY-MM-DD format)
DEFAULT_START_DATE = "2026-09-19"


def get_next_weekday(start_date: datetime, target_weekday: int) -> datetime:
    """Calculate the next date matching a specific weekday on or after start_date.

    Args:
        start_date: The starting reference date for the event series.
        target_weekday: Weekday index (0 = Monday, 1 = Tuesday, 2 = Wednesday).

    Returns:
        The next datetime matching target_weekday on or after start_date.
        If start_date is already on target_weekday, start_date is returned.
    """
    days_ahead = target_weekday - start_date.weekday()
    if days_ahead < 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def generate_recurring_dates(
    first_event_datetime: datetime,
    occurrences: int = 20,
    interval_weeks: int = 2
) -> List[datetime]:
    """Generate a series of recurring event timestamps starting from first_event_datetime.

    Args:
        first_event_datetime: Datetime of the first event in the series.
        occurrences: Total number of recurring event instances to generate.
        interval_weeks: Number of weeks between occurrences (2 = bi-weekly).

    Returns:
        List of datetime objects representing each scheduled occurrence.
    """
    event_dates: List[datetime] = []
    current_dt = first_event_datetime

    for _ in range(occurrences):
        event_dates.append(current_dt)
        # Advance by specified number of weeks for the next event in series
        current_dt += timedelta(weeks=interval_weeks)

    return event_dates


def send_event_via_http(
    event_name: str,
    event_datetime: datetime,
    location: str,
    description: str,
    web_url: str = DEFAULT_WEB_URL
) -> bool:
    """Send a POST request to add an event via the web application admin route.

    Args:
        event_name: Name of the event.
        event_datetime: Datetime of the event.
        location: Venue location.
        description: Description of the event.
        web_url: Target admin endpoint URL.

    Returns:
        True if the request was successful, False otherwise.
    """
    # Format date for HTML5 datetime-local input (YYYY-MM-DDTHH:MM)
    formatted_date = event_datetime.strftime("%Y-%m-%dT%H:%M")

    payload = {
        "name": event_name,
        "date": formatted_date,
        "location": location,
        "description": description
    }

    encoded_data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(
        web_url,
        data=encoded_data,
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status in (200, 302):
                date_label = event_datetime.strftime("%a %b %d, %Y at %H:%M")
                print(f"[HTTP 200] Successfully added '{event_name}' on {date_label}")
                return True
    except urllib.error.URLError as err:
        print(f"[HTTP ERROR] Failed to post event '{event_name}': {err}")
        return False

    return False


def generate_sql_file(
    events_list: List[Dict[str, Any]],
    output_filepath: str
) -> None:
    """Write SQL INSERT queries for events into a SQL script file.

    Args:
        events_list: List of dictionaries containing event details.
        output_filepath: Target filepath for the SQL script.
    """
    header_comment = "-- Auto-generated recurring events script\n"
    insert_prefix = "INSERT INTO events (name, event_date, location, description) VALUES\n"

    value_rows = []
    for evt in events_list:
        # Escape single quotes in SQL strings
        safe_name = evt["name"].replace("'", "''")
        safe_date = evt["date"].strftime("%Y-%m-%d %H:%M:%S")
        safe_loc = evt["location"].replace("'", "''")
        safe_desc = evt["description"].replace("'", "''")

        row_str = f"('{safe_name}', '{safe_date}', '{safe_loc}', '{safe_desc}')"
        value_rows.append(row_str)

    full_sql = header_comment + insert_prefix + ",\n".join(value_rows) + ";\n"

    with open(output_filepath, "w", encoding="utf-8") as file_handle:
        file_handle.write(full_sql)

    print(f"[SQL EXPORT] Written {len(events_list)} events to '{output_filepath}'")


def insert_events_to_db(events_list: List[Dict[str, Any]]) -> bool:
    """Insert event records directly into PostgreSQL database.

    Args:
        events_list: List of dictionaries containing event details.

    Returns:
        True if inserted successfully, False otherwise.
    """
    if not HAS_PSYCOPG2:
        print("[DB ERROR] psycopg2/psycopg package is not installed.")
        print("Falling back to generating SQL file...")
        return False

    try:
        connection = psycopg2.connect(
            host=DEFAULT_DB_HOST,
            port=DEFAULT_DB_PORT,
            user=DEFAULT_DB_USER,
            password=DEFAULT_DB_PASSWORD,
            dbname=DEFAULT_DB_NAME
        )
        cursor = connection.cursor()

        query = """
            INSERT INTO events (name, event_date, location, description)
            VALUES (%s, %s, %s, %s);
        """

        for evt in events_list:
            cursor.execute(
                query,
                (
                    evt["name"],
                    evt["date"].strftime("%Y-%m-%d %H:%M:%S"),
                    evt["location"],
                    evt["description"]
                )
            )

        connection.commit()
        cursor.close()
        connection.close()

        print(f"[DB SUCCESS] Inserted {len(events_list)} events into PostgreSQL.")
        return True
    except Exception as err:
        print(f"[DB ERROR] Database insertion failed: {err}")
        return False


def main() -> None:
    """Parse CLI arguments and schedule recurring events starting from start date."""
    parser = argparse.ArgumentParser(
        description="Add recurring events (e.g. Colourful Kitchen) starting from a specific date."
    )

    parser.add_argument(
        "--name",
        type=str,
        default=DEFAULT_EVENT_NAME,
        help="Name of the event (default: Colourful Kitchen)"
    )
    parser.add_argument(
        "--start-date",
        type=str,
        default=DEFAULT_START_DATE,
        help="Start date for the first event of the series in YYYY-MM-DD format (default: 2026-09-02)"
    )
    parser.add_argument(
        "--location",
        type=str,
        default=DEFAULT_LOCATION,
        help="Location of the event (default: the bookshop kitchen)"
    )
    parser.add_argument(
        "--description",
        type=str,
        default=DEFAULT_DESCRIPTION,
        help="Event description"
    )
    parser.add_argument(
        "--weekday",
        type=int,
        default=DEFAULT_WEEKDAY,
        help="Day of week (0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun)"
    )
    parser.add_argument(
        "--hour",
        type=int,
        default=20,
        help="Hour of the day in 24-hour format (default: 20 for 8pm)"
    )
    parser.add_argument(
        "--minute",
        type=int,
        default=0,
        help="Minute of the hour (default: 0)"
    )
    parser.add_argument(
        "--occurrences",
        type=int,
        default=20,
        help="Total number of recurring instances (default: 6)"
    )
    parser.add_argument(
        "--interval-weeks",
        type=int,
        default=2,
        help="Interval between events in weeks (default: 2 for fortnightly)"
    )
    parser.add_argument(
        "--mode",
        choices=["http", "sql", "db"],
        default="http",
        help="Execution mode: http (POST to web app), sql (export .sql file), db (direct PostgreSQL)"
    )
    parser.add_argument(
        "--sql-output",
        type=str,
        default="sql/insert_movie.sql",
        help="Path for generated SQL script when --mode=sql"
    )
    parser.add_argument(
        "--url",
        type=str,
        default=DEFAULT_WEB_URL,
        help="Target URL for HTTP POST mode"
    )

    args = parser.parse_args()

    # Parse starting date for the first event of the series
    if args.start_date:
        base_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    else:
        base_date = datetime.now()

    # Calculate first event date on or after base_date matching target weekday
    first_date = get_next_weekday(base_date, args.weekday)

    # Combine first date with target time (e.g. 20:00)
    event_time = time(args.hour, args.minute)
    first_datetime = datetime.combine(first_date.date(), event_time)

    # Generate complete list of recurring datetimes for the series
    scheduled_datetimes = generate_recurring_dates(
        first_event_datetime=first_datetime,
        occurrences=args.occurrences,
        interval_weeks=args.interval_weeks
    )

    # Build event payload dictionary list
    events_data = [
        {
            "name": args.name,
            "date": dt,
            "location": args.location,
            "description": args.description
        }
        for dt in scheduled_datetimes
    ]

    print("=" * 60)
    print(f" Scheduling Series: '{args.name}'")
    print(f" First Event Start Date: {first_datetime.strftime('%Y-%m-%d %H:%M')}")
    print(f" Frequency: Every {args.interval_weeks} weeks on weekday {args.weekday} at {args.hour:02d}:{args.minute:02d}")
    print(f" Total Occurrences: {args.occurrences}")
    print(f" Execution Mode: {args.mode.upper()}")
    print("=" * 60)

    # Execute selected mode
    if args.mode == "http":
        success_count = 0
        for evt in events_data:
            if send_event_via_http(
                event_name=evt["name"],
                event_datetime=evt["date"],
                location=evt["location"],
                description=evt["description"],
                web_url=args.url
            ):
                success_count += 1
        print(f"\n[SUMMARY] Posted {success_count}/{len(events_data)} events starting from {first_datetime.strftime('%Y-%m-%d')}.")

    elif args.mode == "sql":
        generate_sql_file(events_data, args.sql_output)

    elif args.mode == "db":
        insert_events_to_db(events_data)


if __name__ == "__main__":
    main()
