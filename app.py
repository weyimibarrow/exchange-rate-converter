"""
app.py — a small Flask web frontend for the currency converter.

This file does NOT contain any conversion logic of its own. It imports and
reuses what already lives in main.py:

  - EXCHANGE_RATES     : the dict built from the live open.er-api.com feed
                         (already fetched and rate-inverted inside main.py)
  - convert_currencies : the existing conversion function, unchanged

The web page just collects user input, hands it to convert_currencies(),
and shows the result (or a friendly error) back on the page.
"""

from flask import Flask, render_template, request

# Reuse the existing converter. Importing main.py runs its top-level code,
# which fetches the live rates and builds EXCHANGE_RATES. The CLI input loop
# is guarded by `if __name__ == "__main__":` in main.py, so it is skipped here.
from main import EXCHANGE_RATES, convert_currencies

app = Flask(__name__)

# Sorted list of valid currency codes, used to fill both dropdowns so the
# user can only ever pick a currency that actually exists in EXCHANGE_RATES.
CURRENCIES = sorted(EXCHANGE_RATES.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    # Remember what the user typed so the form stays filled after submitting.
    form = {"amount": "", "from_currency": "USD", "to_currency": "EUR"}

    if request.method == "POST":
        form["amount"] = request.form.get("amount", "")
        form["from_currency"] = request.form.get("from_currency", "")
        form["to_currency"] = request.form.get("to_currency", "")

        try:
            # Same amount validation idea as the CLI: a bad number raises ValueError.
            amount = float(form["amount"])
        except ValueError:
            error = "Please enter a valid number for the amount (e.g. 1, 100, 30.5)."
        else:
            converted = convert_currencies(
                amount, form["from_currency"], form["to_currency"]
            )
            # convert_currencies returns None on an invalid currency code (KeyError).
            if converted is None:
                error = "Invalid currency code. Please check your selection and try again."
            else:
                result = (
                    f"{amount:.2f} {form['from_currency']} = "
                    f"{converted:.2f} {form['to_currency']}"
                )

    return render_template(
        "index.html",
        currencies=CURRENCIES,
        result=result,
        error=error,
        form=form,
    )


if __name__ == "__main__":
    app.run(debug=True)
