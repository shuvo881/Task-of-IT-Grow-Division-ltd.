import requests

def get_location_info(api_key, address):
    # Google Maps Geocoding API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"

    # Parameters for the API request
    params = {
        'address': address,
        'key': api_key,
    }

    try:
        # Sending a GET request to the API
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Check if the request was successful

        # Parse the JSON response
        data = response.json()

        # Check if the response contains results
        if data['status'] == 'OK':
            # Extract relevant information
            location = data['results'][0]['formatted_address']
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']

            return {
                'location': location,
                'latitude': latitude,
                'longitude': longitude,
            }
        else:
            print(f"Error: {data['status']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Google API key
    api_key = 'YOUR_API_KEY'

    # Replace '1600 Amphitheatre Parkway, Mountain View, CA' with the address you want to query
    address = '1600 Amphitheatre Parkway, Mountain View, CA'

    # Get location information
    location_info = get_location_info(api_key, address)

    # Print the results
    if location_info:
        print("Location:", location_info['location'])
        print("Latitude:", location_info['latitude'])
        print("Longitude:", location_info['longitude'])
