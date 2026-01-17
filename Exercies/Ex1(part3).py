import requests

def weather():
    city = input("Enter city name: ").lower()

    city_coords = {
        "delhi": (28.61, 77.23),
        "mumbai": (19.07, 72.87),
        "pune": (18.52, 73.85)
    }

    if city not in city_coords:
        print("City not found")
        return

    latitude, longitude = city_coords[city]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    response = requests.get(url)
    data = response.json()

    print("Temperature:", data["current_weather"]["temperature"], "°C")
    print(f"Longitude of {city}: {longitude}")
    print(f"Latitude of {city}: {latitude}")

weather()
