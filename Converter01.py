"""
I installed forex-python with the following command: pip install forex-python
"""


from forex_python.converter import CurrencyRates

cr = CurrencyRates()



def convert_currency(amount, from_currency, to_currency):
    try:
        converted_amount = cr.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        return e

currencies = ["EUR", "GBP", "JPY", "CAD", "CHF", "XAF", "AUD", "NZD","NOK", "MXN", "BRL", "ARS", "CLP", "PEN"]

""" 
Now a conversion accepting user input

XAF is the currency code for central Africa Bank.

"""



amount = float(input("Enter the amount to convert: "))




from_currency = "USD"

for to_currency in currencies:
    print("{0} {1} = {2} {3}".format(amount, from_currency, convert_currency(amount, from_currency, to_currency), to_currency))

"""
Some currencies are not supported by forex-python.


"""
