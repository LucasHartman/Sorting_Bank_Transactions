''' =================================================================================
			
				Define Payment Functions
			
================================================================================= '''



def InkomstenBelasting(inkomen):	
	'''
	input je bruto salaris en bereken hoeveel inkosten belasting moet betalen
	'''

	tax = inkomen/100 * 37.1
	tax = round(tax,2)
	tax = -abs(tax)
	inkomen = inkomen+tax	
	total = [inkomen, tax]
	return total

	




def PersioenAftrek(brutoIncome):
	'''
	input je bruto salaris en bereken hoeveel pensioen kosten word afgettroken
	'''
	pensioen = (brutoIncome/100)* 2.6
	pensioen = round(-abs(pensioen))
	return pensioen






def Dividendbelasting(dividend):
	'''
	input hoeveel belasting je betaal over de divindend inkomen van de maand
	'''	
	dividendBelasting = dividend/100*15
	dividend = round(dividend - dividendBelasting, 2)
	total = [dividend, dividendBelasting]
	return total
	





def Rioolheffing(rioolheffing=-225.84):
	'''
	input de jaar prijs voor rioolheffing en output de maand kosten
	'''
	rioolheffing = round( rioolheffing /12, 2)
	return rioolheffing	






def Afvalstoffenheffing(afvalstoffenheffing=-234.72):
	'''
	input de jaar prijs voor afvalsoffenheffing en output de maand kosten
	'''
	afvalstoffenheffing = round( afvalstoffenheffing /12 ,2)
	return afvalstoffenheffing	






def Watersysteemheffing(watersysteemheffing=-60.10):
	'''
	input de jaar prijs voor watersystemheffing en output de maand kosten
	'''
	watersysteemheffing = round( watersysteemheffing /12 ,2)
	return watersysteemheffing	






def RoadTax(wegenbelasting=-26):
	'''
	input the maand kosten voor wegenbelasting
	zie "SOURCE" voor hoeveel jij moet betalen op basis van de type auto je hebt
	
	SOURCE: https://www.independer.nl/autoverzekering/info/wegenbelasting-berekenen
	'''
	wegenbelasting = -26 # Ford KA
	return wegenbelasting





def  Water(water=-180):
	'''
	input jaar prijs voor waterverbruik en output de maand kosten
	'''
	water = round( water /12 ,2)
	return water
	
	
	


def  Elektriciteit(elektriciteit=-600):
	'''
	input jaar prijs voor elektrichiteitverbruik en output de maand kosten
	'''
	elektriciteit = round( elektriciteit /12 ,2)
	return elektriciteit






def  Gas(gas=-900):
	'''
	input jaar prijs voor gasverbruik en output de maand kosten
	'''
	gas = round( gas /12 ,2)
	return gas
	
	
	
	
	
def Vermogen2022(spaargeld, belegging, schuld):
	'''
	input uw spaargeld, beleeging en schuld en bereken uw
	vermogenbelasting per maand
	
	deze funtie is niet klaar

	'''	
	belasting =0
	bezit = spaargeld + belegging
	
	if (bezit >= 30846):
		rendementSpaargeld = 	spaargeld	/100	*0.09
		rendementBeleggen = 	belegging	/100	*5.33
		rendementSchuld = 	schuld		/100	*-3.03
		totaalRendement = 	rendementSpaargeld + rendementBeleggen + rendementSchuld

		belasting = (totaalRendement-400)	/100	*33 # 33% belasting
		belasting = belasting /12
	return belasting
	


