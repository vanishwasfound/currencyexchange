import requests


from_currency = input("Enter the currency you want to CONVERT FROM: ").upper()
to_currency = input("Enter the currency you want to CONVERT TO: ").upper()
amount = float(input("Enter the amount you want to convert: "))


response = requests.get(f"https://api.frankfurter.app/latest?base={from_currency}")
data = response.json()


if to_currency in data['rates']:
    rate = data['rates'][to_currency]
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
else:
    print(f"Conversion rate for {to_currency} not found.")
