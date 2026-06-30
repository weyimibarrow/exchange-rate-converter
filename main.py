EXCHANGE_RATES = {"USD": 1, "NGN": 0.00072, "CAD": 0.70, "GBP": 1.33}

def convert_currencies(amount_to_convert, from_currency, to_currency):
    amount_in_usd = amount_to_convert * EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd / EXCHANGE_RATES[to_currency]
    return converted_amount



EXCHANGE_RATES["EUR"] = 1.14