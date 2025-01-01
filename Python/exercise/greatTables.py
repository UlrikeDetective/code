# Import libraries
import polars as pl
from great_tables import GT, md, html, loc, style

# Load dataset
df = pl.read_csv('exercise/cdmx-subway.csv', truncate_ragged_lines=True)

# Create table with great-tables
cdmx = (
    GT(df)
    .tab_header(
        title=md("### Mexico City's Subway Lines and Stations"),
        subtitle=html('''<h4 align="left">
        Mexico City's metro system is a vital artery of the bustling metropolis.
        It is the largest and busiest in Latin America, serving more than 5.5 million
        passengers daily in its 195 stations and 12 lines.</h4>''')
    )
    #.tab_options(table_width="100%")
    .cols_align(align='center', columns=['Line','Inauguration','Total stations'])
    .cols_label(
        Line="Line",
        Northern_Western_terminal="Northern/Western terminal",
        Southern_Eastern_terminal="Southern/Eastern terminal",
        Total_stations="Total stations",
        Color="Color",
        Passenger_track="Passenger track",
        Inauguration="Inauguration",
        Ridership="Ridership"
    )
    .fmt_date(columns='Inauguration', date_style="m_day_year")
    .sub_missing(missing_text="")
    .tab_source_note(source_note=md('''**Jesus L. Monroy**<br>*Economist & Data Scientist*<br><br>'''))
    .tab_source_note(
        source_note=md('''Source: [Wikipedia](https://en.wikipedia.org/wiki/Mexico_City_Metro>Wikipedia)'''))
)
# Display the table
cdmx.show()