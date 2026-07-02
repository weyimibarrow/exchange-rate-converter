import requests
response = requests.get("https://open.er-api.com/v6/latest/USD")
print(f"Status: {response.status_code}")
data = response.json()

raw_rates = data["rates"]
inverted_rates = {}
for currency, rate in raw_rates.items():
    inverted_rates[currency] = 1 / rate


EXCHANGE_RATES = inverted_rates 


def convert_currencies(amount_to_convert, from_currency, to_currency):
    amount_in_usd = amount_to_convert * EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd / EXCHANGE_RATES[to_currency]
    return converted_amount

example_1 = convert_currencies(50, "EUR", "AUD")
example_2 = convert_currencies(200, "UGX", "USD")
print(example_1)
print(example_2)