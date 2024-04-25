import phonenumbers
from phonenumbers import (timezone,geocoder,carrier)
 
number = input("Enter the phone number with country code : ")
 
# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)
 
# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print(f"timezone : {timeZone}")
 
# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print(f"location : {geolocation}")
 
# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print(f"service provider : {service}")
