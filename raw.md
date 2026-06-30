


def convert_currencies(amount_to_convert,from_currency,to_currency):
amount_in_usd = amount_to_convert * EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd / EXCHANGE_RATES[to_currency]
    return converted_amount
example_amount_converted = convert_currencies(10, "USD", "CAD")
print(example_amount_converted)
example_convert_2 = convert_currencies(100, "USD", "USD")
print(example_convert_2)
example_convert_3 = convert_currencies(50, "GBP", "CAD")
print(example_convert_3)

example_convert_4 = convert_currencies(example_convert_3, "CAD", "GBP")
print(example_convert_4)