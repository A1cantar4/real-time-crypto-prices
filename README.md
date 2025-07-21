# Crypto Price Checker

Real-time cryptocurrency price checker using the CoinGecko API — featuring both simple and advanced modes.  
Developed by [A1cantar4](https://github.com/A1cantar4)

---

## Project Structure

```
.
├── core/
│   ├── advanced_price_api.py   # Advanced query with aliases, multi-currency support, and locale formatting
│   └── simple_price_api.py     # Basic real-time price check
├── old/
│   └── old_simple_api_request  # Legacy version
├── main.py                     # Interactive menu for module selection
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## How to Use

### 1. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run the main script:
```bash
python main.py
```

You will be prompted to choose between:

- `1. Advanced Price API`: supports aliases, multiple currencies, and localized formatting.
- `2. Simple Price API`: quick check of Bitcoin price in USD.

---

## Features

### Advanced Mode (`core/advanced_price_api.py`)
- Uses CoinGecko API.
- Search by **name**, **symbol**, or **coin ID**.
- Supported currencies: **BRL**, **USD**, **EUR**.
- Localized price formatting (e.g., `R$ 172.456,98` or `$20,003.21`).
- Debug mode for developers.

### Simple Mode (`core/simple_price_api.py`)
- Straightforward query.
- Fetches only **Bitcoin → USD** price.

---

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - `requests`
  - `babel` (for locale-based formatting)

---

## Example Output

```
Olá chefe, choose which module you want to run: 
1. Advanced Price API
2. Simple Price API

Enter the number, captain: 1

Running Advanced Price API...
¨¨¨ REAL-TIME CRYPTO PRICES ¨¨¨
Loading coin list from API...

Type the cryptocurrency name (e.g. bitcoin, eth, doge): doge
Now type the currency (e.g. usd, brl, eur): brl

Found it! The current price of doge in BRL is: R$0,76
```

---

## Author

**A1cantar4**  
GitHub: [https://github.com/A1cantar4](https://github.com/A1cantar4)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file if applicable.