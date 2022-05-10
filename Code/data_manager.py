import requests

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/0031fb1f29b819287f7ac6b45bf3f526/flightDeals/prices/'

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEETY_PRICES_ENDPOINT}/{city["id"]}',
                json=new_data
            )