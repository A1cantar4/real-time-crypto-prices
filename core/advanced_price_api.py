import requests
from babel.numbers import format_currency

# Locale by coin
LOCALE_BY_CURRENCY = {
    "brl": "pt_BR",
    "usd": "en_US",
    "eur": "de_DE",
} # When import tkinter, you can add more locales here

# This function will format the price according to the currency code
def format_price(price, currency_code):
    try:
        locale = LOCALE_BY_CURRENCY.get(currency_code.lower(), "en_US")
        return format_currency(price, currency_code.upper(), locale=locale)
    except Exception:
        return f"{currency_code.upper()} {price:,.2f}"

# This function fetches the price of a cryptocurrency in a specified currency
def get_price(coin_id="bitcoin", currency="usd", timeout=10, debug=False):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id.lower(),
        "vs_currencies": currency.lower()
    } # uses specific parameters to avoid problems with the API: coint_id and currency.

    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status() # Verify that the request was successful with http status code 200
        data = response.json() # Convert the response to JSON

        if debug:
            print(f"DEBUG: Resposta da API: {data}")

        return data.get(coin_id.lower(), {}).get(currency.lower()) # Get the price from the JSON response

    except requests.RequestException as e:
        print(f"Erro de conexão com a API: {e}")
    except ValueError as e:
        print(f"Erro nos dados da resposta: {e}")

    return None

# This function fetches a list of coin aliases from the CoinGecko API
def fetch_coin_aliases(debug=False):
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Same as before
        coins = response.json() # Equal in line 30

        # Create a dictionary to hold aliases 
        aliases = {}
        for coin in coins:
            coin_id = coin["id"]
            symbol = coin["symbol"].lower()
            name = coin["name"].lower()

            # 
            if symbol not in aliases:
                aliases[symbol] = coin_id
            if name not in aliases:
                aliases[name] = coin_id
            aliases[coin_id] = coin_id

        if debug:
            print(f"DEBUG: Total de aliases carregados: {len(aliases)}")

        return aliases

    except Exception as e:
        print(f"Erro ao buscar lista de moedas: {e}")
        return {}

# To run the main function when the script is executed directly
def main():
    print("\nExecutando Advanced Price API...")
    print("\n¨¨¨ REAL-TIME CRYPTO PRICES ¨¨¨")

    # Load the list of coin aliases from the API
    print("Carregando lista de moedas da API...")
    COIN_ALIASES = fetch_coin_aliases()

    # Interactive input for coin and currency
    coin_input = input("\nDigite o nome da criptomoeda meu nobre (ex: bitcoin, eth, doge): ").strip().lower()
    currency = input("Cavalheiro, agora digite a moeda (ex: usd, brl, eur): ").strip().lower()

    # normalize the coin input
    coin = COIN_ALIASES.get(coin_input)
    
    # Info message if no coin is found
    if not coin: 
        print("Camarada... Moeda não encontrada exatamente. Tentando encontrar aproximação...")
        coin = next((v for k, v in COIN_ALIASES.items() if coin_input in k), None) 
        # This will find the first match in the aliases
        

    if coin:
        price = get_price(coin, currency) # Returns the price of the coin in the specified currency
        if price is not None: # If not None, it means the price was fetched successfully
            formatted = format_price(price, currency)
            print(f"\nAchei! O preço atual de {coin_input} em {currency.upper()} é: {formatted}")
        else:
            print("Infelizmente, dessa vez não foi possível obter o preço.")
    else:
        print("Hum... Sinto muito, mas... Criptomoeda não reconhecida pela API.")

# Only run the main function if this script is executed directly
if __name__ == "__main__":
    main()
