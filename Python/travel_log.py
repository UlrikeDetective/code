class TravelLog:
    def __init__(self):
        self.logs = []

    def add_log(self, destination, country, cost, transport_mode, distance_covered, highlights, visited_places, favorite_things, meals):
        log = {
            "Destination of the day": destination,
            "Country of destination": country,
            "Total Cost": cost,
            "Transport Mode": transport_mode,
            "Distance Covered": distance_covered,
            "Highlights": highlights,
            "Visited Places": visited_places,
            "Favorite Things": favorite_things,
            "Favorite Meals": meals
        }
        self.logs.append(log)

    def display_logs(self):
        for idx, log in enumerate(self.logs, start=1):
            print(f"Travel Log #{idx}:")
            for key, value in log.items():
                print(f"{key}: {value}")
            print("\n")


def main():
    travel_log = TravelLog()

    while True:
        print("\nTravel Log Menu:")
        print("1. Add a new log")
        print("2. Display all logs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            destination = input("Enter destination for the day: ")
            country = input("In what country is the destination? ")
            cost = input("Enter cost for the day: ")
            transport_mode = input("Enter transport mode: ")
            distance_covered = input("Enter distance covered in km: ")
            highlights = input("Enter highlights: ")
            visited_places = input("Enter visited places: ")
            favorite_things = input("Enter favorite things: ")
            meals = input("Enter favorite meal: ")

            travel_log.add_log(destination, country, cost, transport_mode, distance_covered, highlights, visited_places, favorite_things, meals)
            print("Log added successfully!")

        elif choice == "2":
            if not travel_log.logs:
                print("No logs to display.")
            else:
                travel_log.display_logs()

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

