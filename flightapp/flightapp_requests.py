import requests

class FlightAppRequests:

    BASE_URL = 'https://fr24api.flightradar24.com/api'
    SANDBOX_URL = 'https://fr24api.flightradar24.com/api/sandbox'
    TOKEN = ''
    SANDBOX_TOKEN = 'Bearer 9d388cc9-9a6a-46e7-9374-3587089ff0ef|6cGIdgpOfuzFZRpHU0vRFC8hPD0nh8NX5cZaJNJee27fdf05'

    def build_request(endpoint, params, sandbox):
        headers = {
            'Accept': 'application/json',
            'Accept-Version': 'v1'
        }
        if sandbox:
            url = f"{FlightAppRequests.SANDBOX_URL}{endpoint}"
            headers['Authorization'] = FlightAppRequests.SANDBOX_TOKEN
        else:
            url = f"{FlightAppRequests.BASE_URL}{endpoint}"
            headers['Authorization'] = FlightAppRequests.TOKEN

        # print (url)
        # print (headers)
        return requests.get(url, headers=headers, params=params)

