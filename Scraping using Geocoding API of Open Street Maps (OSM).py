#import nominatim api
from geopy.geocoders import Nominatim
#activate nominatim geocoder
locator = Nominatim(user_agent="myGeocoder")
#type any address text
location = locator.geocode("Patan")
#print lattitude and longitude of the address
from geopy.distance import geodesic
location3 = locator.geocode("Dhar")
location4 = locator.geocode("Ujjain")
a= (location3.latitude, location3.longitude)
b=(location4.latitude, location4.longitude)
print(geodesic(a, b).km)
#the API output has multiple other details as a json like altitude, lattitude, longitude, correct raw addres, etc.
#printing all the informaton
location = locator.geocode("Dhar")
location.raw,location.point,location.longitude,location.latitude,location.altitude,location.address
#trying another address
location2 = locator.geocode("Dhule")
location1 = locator.geocode(input())
location2 = locator.geocode(input())
from geopy.distance import geodesic
a = (location1.longitude,location1.latitude )
b = (location2.longitude, location2.longitude)
print(geodesic(a, b).km)
