# Exercise 2: Create a function that validates crypto response
#             Check that 'quotes' and 'USD' keys exist before accessing
import requests
import time

def crypto_price():
    coin = input("Enter coin name (btc-bitcoin / eth-ethereum): ").strip().lower()
    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"

    for i in range(3):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if "quotes" not in data or "USD" not in data["quotes"]:
                print("Data format error")
                return

            price = data["quotes"]["USD"]["price"]
            change = data["quotes"]["USD"]["percent_change_24h"]

            print("\nCoin:", data["name"])
            print("Price:", round(price, 2))
            print("24h Change:", round(change, 2), "%")
            return

        except Exception:
            print("Request failed, trying again...")
            time.sleep(2)

    print("Failed after 3 tries")

crypto_price()
