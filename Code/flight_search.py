import requests

KIWI_API_KEY = 'QIrYDc1bcer0fHmR467EuM6c1G7NLd_l'
KIWI_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    
    def get_destination_code(self, city_name):

        header = {
            'apikey': KIWI_API_KEY,
        }
        parameters = {
            'term': city_name,
            'active_only': True
        }
        response = requests.get(
            url=KIWI_ENDPOINT,
            headers=header,
            params=parameters,
        )
        data = response.json()
        code = data['locations'][0]['code']
        return code
                

