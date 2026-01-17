# Exercise 3: Add logging to track all API requests
#             import logging
#             logging.basicConfig(level=logging.INFO)
import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

def crypto_price():
    coin = input("Enter coin name (btc-bitcoin / eth-ethereum): ").strip().lower()
    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"

    for i in range(3):
        try:
            logging.info(f"Sending request to: {url}")
            response = requests.get(url, timeout=5)

            logging.info(f"Status code received: {response.status_code}")
            response.raise_for_status()

            data = response.json()

            if "quotes" not in data or "USD" not in data["quotes"]:
                logging.error("Invalid response format")
                print("Data format error")
                return

            price = data["quotes"]["USD"]["price"]
            change = data["quotes"]["USD"]["percent_change_24h"]

            print("\nCoin:", data["name"])
            print("Price:", round(price, 2))
            print("24h Change:", round(change, 2), "%")
            return

        except Exception as e:
            logging.warning(f"Request failed (attempt {i+1}): {e}")
            time.sleep(2)

    logging.error("All retry attempts failed")
    print("Failed after 3 tries")

crypto_price()
