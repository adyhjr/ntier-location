# Frontend Layer
import business as bns # References classes for city information
import dataaccess as data # References data extracted from csv file

INDEX_FACTORING = 1 # used to correctly display index in csv file

def main():
    """
        This is the main function of the program. It interacts with the user, asking for inputs and displaying results.

        The function first asks the user to input a city name. It then validates the city name and retrieves its latitude
        and longitude. The function then asks the user to input a number for the top/bottom threshold for the number of
        cities to show and validates this input.

        The user is then asked to input a radius value. The function ensures that this value is a positive number and
        within the range of 1 to 1000.

        The function then retrieves the closest and farthest cities to the user's chosen city, based on the top/bottom
        threshold number. The latitude, longitude, and distance from the chosen city for each of these cities are then
        displayed to the user.
    """

    city_instance = bns.City(" ") # instance of city
    city_choice = city_instance.city_input()
    city_latitude = bns.City.city_latitude(city_choice)
    city_longitude = bns.City.city_longitude(city_choice)

    # Print city details to user
    print(f"City choice is {city_choice} (Latitude: {city_latitude}, Longitude: {city_longitude}) found at index {data.CITY_INDEX_DICT[city_choice] + INDEX_FACTORING}")

    top_bottom_num = bns.CitiesList.num_validate(input("Enter top/bottom threshold for number of cities to show: "))
    bns.CitiesList.city_parameter(top_bottom_num)

    is_valid = False
    while not is_valid:
        try:
            radius = float(input("Enter radius: "))
            if radius > 0 and radius <= 1000:
                is_valid = True
            else:
                print("Invalid input. Please enter a positive number and keep within range (1 , 1000).")
        except ValueError:
            print("Invalid input. Please enter a number.")

    closest_cities = bns.CitiesList.get_nearby_cities(city_choice, top_bottom_num)[INDEX_FACTORING - INDEX_FACTORING]
    farthest_cities = bns.CitiesList.get_nearby_cities(city_choice, top_bottom_num)[INDEX_FACTORING]

    print(f"Closest cities to {city_choice}:")
    for city, distance in closest_cities:
        lat = data.CITYINFO_DICT[city]['Latitude']
        lon = data.CITYINFO_DICT[city]['Longitude']
        print(f"{city} (Latitude: {lat}, Longitude: {lon}): Distance from {city_choice}: {distance} km")

    print(f"\nFarthest cities from {city_choice}:")
    for city, distance in farthest_cities:
        lat = data.CITYINFO_DICT[city]['Latitude']
        lon = data.CITYINFO_DICT[city]['Longitude']
        print(f"{city} (Latitude: {lat}, Longitude: {lon}): Distance from {city_choice}: {distance} km")

if __name__ == '__main__':
    main()