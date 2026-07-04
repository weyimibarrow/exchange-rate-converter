import requests
try:
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    if response.status_code != 200:
        print("Oh no! Something's gone wrong. Please try again later.")
        exit()
    data = response.json()
except requests.exceptions.ConnectionError:
    print("Error: We're not able to connect to the exchange rates server right now. Try again later, thank you!")
    exit()

raw_rates = data["rates"]
inverted_rates = {}
for currency, rate in raw_rates.items():
    inverted_rates[currency] = 1 / rate


EXCHANGE_RATES = inverted_rates 


def convert_currencies(amount_to_convert, from_currency, to_currency):
    try:
        amount_in_usd = amount_to_convert * EXCHANGE_RATES[from_currency]
        converted_amount = amount_in_usd / EXCHANGE_RATES[to_currency]
        return converted_amount
    except KeyError as e:
        return None
    

# gathering user input for the currency conversion
# This block only runs when main.py is executed directly (the CLI).
# When main.py is imported (e.g. by app.py), it is skipped so the
# converter logic above can be reused without asking for input.
if __name__ == "__main__":
    while True:
        try:
            amount_to_convert = float(input("Enter the amount you want to convert here: "))
            from_currency = input("Select the currency you want to convert from: ")
            to_currency = input("Select the currency you want to convert to: ")
            result = convert_currencies(amount_to_convert, from_currency, to_currency)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number e.g (1, 2, 100, 30.5, etc).")

    if result is None:
        print("Sorry! You've entered an invalid currency code or amount. Please check your input and try again.")
    else:
        print(f"The result is {result:.2f} {to_currency}.")