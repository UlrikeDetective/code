travel_log = []

def add_new_country(name, times_visited, cities_visited, highlights):
    new_country = {}
    new_country['country'] = name
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    new_country['highlights'] = highlights
    travel_log.append(new_country)

country = input("Add a country: ")
visits = int(input("How many times have you visited that country? "))
list_of_cities = eval(input("Name the cities you visited in that country? (Enter as a list): ")) # create list from formatted string ['London', 'Bristol']
highlights = input("Enter highlights: ")


add_new_country(country, visits, list_of_cities, highlights)
print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favorite city was {travel_log[-1]['cities'][0]}.")
