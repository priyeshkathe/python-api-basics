import requests
import json
import os
from datetime import datetime

# Exercise 1: Cities
CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "pune": (18.5204, 73.8567),
    "jaipur": (26.9124, 75.7873),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}

CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}

# Exercise 5: API Key Support

OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY")


def get_weather(city_name):
    city = city_name.lower().strip()

    if city not in CITIES:
        print("City not found.")
        return None

    lat, lon = CITIES[city]

    
    if OPENWEATHER_API_KEY:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
    else:
       
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("Weather API error:", e)
        return None


def display_weather(city):
    data = get_weather(city)
    if not data:
        return

    print("\nWeather Report")
    print("-" * 30)

    if "current_weather" in data:
        cw = data["current_weather"]
        print("Temperature:", cw["temperature"], "°C")
        print("Wind Speed:", cw["windspeed"], "km/h")
    else:
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")


def get_crypto_price(coin):
    coin_id = CRYPTO_IDS.get(coin.lower(), coin.lower())
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception:
        return None


def display_crypto(coin):
    data = get_crypto_price(coin)
    if not data:
        print("Crypto not found.")
        return

    usd = data["quotes"]["USD"]
    print("\n", data["name"])
    print("Price:", round(usd["price"], 2))
    print("24h Change:", round(usd["percent_change_24h"], 2), "%")

  
    # Exercise 4: Save to JSON
    with open("results.json", "w") as f:
        json.dump(data, f, indent=2)



# Exercise 2: Compare Cryptos
def compare_cryptos():
    coins = input("Enter crypto names (comma separated): ").split(",")

    print("\nComparison Table")
    print("-" * 50)
    print(f"{'Coin':<15}{'Price($)':<15}{'24h %'}")

    for coin in coins:
        data = get_crypto_price(coin.strip())
        if data:
            usd = data["quotes"]["USD"]
            print(f"{data['symbol']:<15}{usd['price']:<15.2f}{usd['percent_change_24h']:.2f}")



# Exercise 3: POST Request

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My Post",
        "body": "Content",
        "userId": 1
    }

    res = requests.post(url, json=payload)
    print("\nPOST Response:")
    print(res.json())



def dashboard():
    print("\nReal-World API Dashboard")
    print(datetime.now())

    while True:
        print("\n1. Weather")
        print("2. Crypto Price")
        print("3. Compare Cryptos")
        print("4. Create POST")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            print("Cities:", ", ".join(CITIES.keys()))
            city = input("City: ")
            display_weather(city)

        elif choice == "2":
            print("Cryptos:", ", ".join(CRYPTO_IDS.keys()))
            coin = input("Crypto: ")
            display_crypto(coin)

        elif choice == "3":
            compare_cryptos()

        elif choice == "4":
            create_post()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    dashboard()
