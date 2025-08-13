from geopy.geocoders import OpenCage

API_KEY = '1777f3f5374e44e5903e8b3f4ded0ceb'

geolocator = OpenCage(api_key=API_KEY)

def get_lat_lng_from_address(address):
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example usage
pickup_address = "Makati City, Philippines"
dropoff_address = "Quezon Memorial Circle, Quezon City, Philippines"

pickup_lat, pickup_lng = get_lat_lng_from_address(pickup_address)
dropoff_lat, dropoff_lng = get_lat_lng_from_address(dropoff_address)

print("Pickup:", pickup_lat, pickup_lng)
print("Drop-off:", dropoff_lat, dropoff_lng)