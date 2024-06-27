# Business Layer
# To do: add exceptions for spacing in input
import dataaccess as dta
import math

class City:
    """
        This class represents a city with its name, latitude, and longitude.

        Attributes:
            city_name (str): The name of the city.

        Methods:
            city_input() -> str:
                Interacts with the user to get a valid city name. The city name is validated against the CITYINFO_DICT
                dictionary from the dataaccess module. If the city name is not found in the dictionary, the user is asked
                to enter the city name again. The function returns the valid city name.

            city_latitude(city: str) -> float:
                Returns the latitude of the given city. The latitude is retrieved from the CITYINFO_DICT dictionary
                from the dataaccess module. If the city is not found in the dictionary, the function returns None.

            city_longitude(city: str) -> float:
                Returns the longitude of the given city. The longitude is retrieved from the CITYINFO_DICT dictionary
                from the dataaccess module. If the city is not found in the dictionary, the function returns None.

            city_validation() -> bool:
                Validates the city_name attribute against the CITYINFO_DICT dictionary from the dataaccess module.
                If the city_name is found in the dictionary, the function returns True. Otherwise, it returns False.
    """

    def __init__(self, city_name: str):
        self.city_name = city_name

    def city_input(self) -> str:
        while True:
            city_name = input("Enter city name: ")
            # Since city key in dictionary is capitalized, use this method to format input
            # to be readable as a valid key.
            city_name = city_name.title()  # Use title() instead of capitalize() to handle multi-word city names
            words = city_name.split()
            if all(word.isalpha() for word in words):  # Check if all words are alphabetic
                self.city_name = city_name
                if self.city_validation():
                    return city_name
                else:
                    print("Error: City not found, try again.")
            else:
                print("Error: Input must be string.")
    @staticmethod
    def city_latitude(city) -> float:
        if city in dta.CITYINFO_DICT:
            return float(dta.CITYINFO_DICT[city]['Latitude'])
        else:
            return None

    @staticmethod
    def city_longitude(city) -> float:
        if city in dta.CITYINFO_DICT:
            return float(dta.CITYINFO_DICT[city]['Longitude'])
        else:
            return None




    def city_validation(self):
        if self.city_name in dta.CITYINFO_DICT:
            #print(f"City Found! \n" # INDEXING TO BE ADDED
                  #f"Details:{dta.CITYINFO_DICT[self.city_name]}")
            return True
        else:
            return False


class CitiesList:

    def __init__(self, city_surrounding: int):
        self.city_surrounding = city_surrounding

    @staticmethod
    def city_parameter(value):
        while True:
            if value <= 0 or value > 100:
                print("Error! Value is out range, try again.")
                value = int(input("Enter a value between 1 and 100: "))
            else:
                return value
    @staticmethod
    def num_validate(value):
        while True:
            if value.isdigit():
                return int(value)
            else:
                print("Error! Input must be a number.")
                value = input("Enter a number: ")

    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        CENTRAL_ANGLE = 2 * math.asin(math.sqrt(a))
        RADIUS_EARTH = 6371  # Radius of Earth in kilometers
        return CENTRAL_ANGLE * RADIUS_EARTH

    @staticmethod
    def get_nearby_cities(city, num_cities):
        central_lat = float(dta.CITYINFO_DICT[city]['Latitude'])
        central_lon = float(dta.CITYINFO_DICT[city]['Longitude'])
        distances = []

        for key, value in dta.CITYINFO_DICT.items():
            if key != city:
                lat = float(value['Latitude'])
                lon = float(value['Longitude'])
                dist = CitiesList.calculate_distance(central_lat, central_lon, lat, lon)
                distances.append((key, dist))

        distances.sort(key=lambda x: x[1])
        closest = distances[:num_cities]
        farthest = distances[-num_cities:]
        return closest, farthest
