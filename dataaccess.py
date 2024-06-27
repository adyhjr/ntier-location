import csv # READING CSV FUNCTIONALITY
"""
This module handles the data access for the city information.

It reads the city data from a CSV file and stores it in two dictionaries:
- CITYINFO_DICT: This dictionary stores the city information with the city name as the key. The value is another
  dictionary that stores the latitude, longitude, and an unknown attribute of the city.
- CITY_INDEX_DICT: This dictionary stores the index of the city in the CSV file with the city name as the key and the
  index as the value.
  
Constants:
- CITYINFO_DICT: A dictionary that stores the city information with the city name as the key. The value is another
  dictionary that stores the latitude, longitude, and an unknown attribute of the city.
- CITY_INDEX_DICT: A dictionary that stores the index of the city in the CSV file with the city name as the key and the
  index as the value.
"""

CITYINFO_DICT = {}
CITY_INDEX_DICT = {}

with open('uscities.csv', mode='r') as file:
    categories = ['City', 'Latitude', 'Longitude', '??']
    city_info = csv.DictReader(file, fieldnames=categories)

    for index, key in enumerate(city_info):
        CITYINFO_DICT[key['City']] = {'Latitude': key['Latitude'], 'Longitude': key['Longitude'], 'UNKNOWN': key['??']}
        CITY_INDEX_DICT[key['City']] = index
