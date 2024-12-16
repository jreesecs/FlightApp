# This site or product includes IATA/ICAO List data available from http://www.ip2location.com.
# This site or product includes code samples from https://fr24api.flightradar24.com/docs/examples-and-use-cases

from flightapp.airport_info import AirportInfo

sandbox_only = True
# AirportInfo.get_arrivals('ESSA', sandbox_only)
# AirportInfo.get_coordinates('ESSA', sandbox_only)
AirportInfo.get_furthest_flight('ESSA', sandbox_only)