CAD_TO_NGN = 965.10 # this means that 1 CAD = 965.10 NGN
USD_TO_NGN = 1374.10 # this means that 1 USD = 1374.10 NGN
NGN_TO_USD = 1 / USD_TO_NGN # this means that 1 NGN = 0.00073 USD
NGN_TO_CAD = 1 / CAD_TO_NGN # this means that 1 NGN = 0.0010 CAD

def naira_to_usd(money_naira):

	""" This function is designed to convert an amount in Nigerian Naira (NGN) to United
	States Dollar (USD) using money_naira (the amount of money to be converted in Ni
	gerian Naira) as a parameter. The function calculates the conversion by multi
	plying the exchange rate const with the money amount in NGN, and returns the result. 
	"""

	naira_to_usd_amount = money_naira * NGN_TO_USD
	return naira_to_usd_amount

def naira_to_cad(money_naira):

	""" This function is designed to convert an amount in Nigerian Naira (NGN) to Cana-
	dian Dollar (CAD) using money_naira (the amount of money to be converted in Ni
	gerian Naira) as a parameter. The function calculates the conversion by multi
	plying the exchange rate const with the money amount in NGN, and returns the result. 
	"""

	naira_to_cad_amount = money_naira * NGN_TO_CAD
	return naira_to_cad_amount

def usd_to_naira(money_usd):

	""" This function is designed to convert an amount in United States Dollar (USD) to Nigerian 
 	Naira using money_usd (the amount of money to be converted in United States Dollar ) as a 	parameter. The function calculates the conversion by multiplying the exchange rate const with 
	the money amount in USD, and returns the result. 
	"""

	usd_to_naira_amount = money_usd * USD_TO_NGN
	return usd_to_naira_amount

def cad_to_naira(money_cad):

	""" This function is designed to convert an amount in Canadian Dollar (CAD) to Nigerian 
 	Naira using money_cad (the amount of money to be converted in Canadian Dollar) as a 	parameter. The function calculates the conversion by multiplying the exchange rate const with 
	the money amount in CAD, and returns the result. 
	"""

	cad_to_naira_amount = money_cad * CAD_TO_NGN
	return cad_to_naira_amount

usd_result = naira_to_usd(5000)
print(f"5000 NGN is {usd_result} USD.")

ngn_from_cad_result = cad_to_naira(500)
print(f"500 CAD is {ngn_from_cad_result} NGN.")

back_to_naira_result = usd_to_naira(usd_result)
print(f"The amount of USD converted back to NGN is {back_to_naira_result} NGN.")