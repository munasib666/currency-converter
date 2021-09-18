
import requests

class Currency_convertor:

	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()
		self.rates = data["rates"]
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


if __name__ == "__main__":

	# YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
	url = str.__add__('http://data.fixer.io/api/latest?access_key=', '2543b918fad7c6f3235b351c79362cb4')
	c = Currency_convertor(url)
	from_country = input("From Country: ")
	to_country = input("TO Country: ")
	amount = int(input("Amount: "))
	c.convert(from_country, to_country, amount)
