# Simple api request to get the price of a cryptocurrency in real-time.
import requests

def get_price(coin_id="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    return data[coin_id][currency]

def main():
    print("\nExecutando 'Simple Price API'...")
    price = get_price("bitcoin", "usd")
    print(f"\nPreço atual do Bitcoin em dolares é: ${price}")

# This block runs only when the script is executed directly
if __name__ == "__main__":
    main()