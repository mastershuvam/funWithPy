import phonenumbers
from phonenumbers import geocoder, carrier

# Replace this with the phone number you want to check
phone_number = phonenumbers.parse("+91987XXXXXX")  # Example Indian number

# Get the location (state/region)
location = geocoder.description_for_number(phone_number, "en")

# Get the carrier (service provider)
service_provider = carrier.name_for_number(phone_number, "en")

print("📍 Location (State):", location)
print("🏢 Carrier (Author):", service_provider)
