travel_log = []

def add_new_country(name, times_visited, cities_visited, highlights, favorite_things, meals):
    new_country = {}
    new_country['country'] = name
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    new_country['highlights'] = highlights
    new_country['favorite_things'] = favorite_things
    new_country['meals'] = meals
    travel_log.append(new_country)

country = input("Add a country: ")
visits = int(input("How many times have you visited that country? "))
list_of_cities = eval(input("Name the cities you visited in that country? (Enter as a list): ")) # create list from formatted string
highlights = input("Enter highlights: ")
favorite_things = input("Enter favorite things: ")
meals = input("Enter meals: ")

add_new_country(country, visits, list_of_cities, highlights, favorite_things, meals)
print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times.")
print(f"My favorite city was {travel_log[-1]['cities'][0]}.")
