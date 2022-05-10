import datetime
from flight_search import FlightSearch
import requests

KIWI_API_KEY = 'QIrYDc1bcer0fHmR467EuM6c1G7NLd_l'
FLIGHT_CALL_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'


class FlightData:
    def __init__(self):
        self.price = 'price'
        self.departure_airport_code = 'departure_airport_code'
        self.departure_city = 'BSB'

    def price_search(self, city_code):
        today = datetime.datetime.now()
        today = today.strftime('%d/%m/%Y')
        six_months = datetime.datetime.now() + datetime.timedelta(days=180)
        six_months = six_months.strftime('%d/%m/%Y')
        headers = {
            'apikey': KIWI_API_KEY
        }
        flight_parameters = {
            'fly_from': 'LON',
            'fly_to': city_code,
            'date_from': today,
            'date_to': six_months,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'adults': 1,
            'curr': 'GBP',
            'max_stopovers': 0,
            'max_sector_stopovers': 0,
            'sort': 'price',
            'limit': 1,
        }
        response = requests.get(url=FLIGHT_CALL_ENDPOINT, headers=headers, params=flight_parameters)
        flight_data = response.json()
        city_to = flight_data['data'][0]['cityTo']
        price = flight_data['data'][0]['price']
        print(f'{city_to}: £{price}')
 
    
