from flightapp.flightapp_requests import FlightAppRequests
from geopy.distance import great_circle
import pandas as pd

class AirportInfo:

    SORTED_FLIGHTS = list()
    DESTINATION_COORDS = ''

    def get_arrivals_full(icao, sandbox):
        AirportInfo.SORTED_FLIGHTS.clear()
        params = dict()
        endpoint = '/live/flight-positions/full'
        params['airports'] = f'inbound:{icao}'
        response = FlightAppRequests.build_request(endpoint, params, sandbox)
        # print(response.status_code)

        if response.ok:
            flights = response.json().get('data', [])
            # Filter out flights without an ETA
            flights_with_eta = [flight for flight in flights if flight.get('eta') is not None]
            # Order flights by ETA
            AirportInfo.SORTED_FLIGHTS = sorted(flights_with_eta, key=lambda x: x.get('eta'))
            print("Flights arriving at ESSA:", end="\n")
            for flight in AirportInfo.SORTED_FLIGHTS:
                print(flight, end="\n")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_coordinates(icao, sandbox):
        #Read from csv to get coords
        df = pd.read_csv('resources/iata-icao.csv', index_col ="icao")
        airport_data = df.loc[icao]
        AirportInfo.DESTINATION_COORDS = (airport_data['latitude'], airport_data['longitude'])
        print(AirportInfo.DESTINATION_COORDS)

    def get_furthest_flight(icao, sandbox):
        # Ensure correct Flight and Airport Data is retrieved
        AirportInfo.get_arrivals_full(icao, sandbox)
        AirportInfo.get_coordinates(icao, sandbox)

        # Function to calculate the great circle distance
        def calculate_distance(coord1, coord2):
            return great_circle(coord1, coord2).kilometers

        farthest_flight = None
        max_distance = 0
        # Calculate the distance for each flight
        for flight in AirportInfo.SORTED_FLIGHTS:
            origin_coords = (flight['lat'], flight['lon'])  # Current position of the flight
            # Calculate distance from origin to ESSA
            distance = calculate_distance(origin_coords, AirportInfo.DESTINATION_COORDS)
            if distance > max_distance:
                max_distance = distance
                farthest_flight = flight
        print(
            f"The farthest flight is from {farthest_flight['orig_icao']} to ESSA with a distance of {max_distance:.6} km.")
