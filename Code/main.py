#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
flight_search = FlightSearch()
from data_manager import DataManager
data_manager = DataManager()
from flight_data import FlightData
flight_data = FlightData()


sheet_data = data_manager.get_destination_data()


if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
for row in sheet_data:
    city_code = row['iataCode']
    flight_data.price_search(city_code)


data_manager.update_destination_codes()



