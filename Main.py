import Function
import Table
import Csv

root = '/home/l/Documents/Python/Accounting/csv/test.csv'
reportLoc = "/home/l/Documents/Python/Accounting/report/"


def fiscaalPartner(val):
	'''
	inpust val and spit, only when you have a fiscaal parnter
	'''
	val = round(val/2, 2)
	return val

''' =================================================================================
			
			List of all transeactions lables

Notes:
	- Huurtoeslag: 	Kale huur + service kost, MAX: 752,33 (2021)
	- Vermogen Belasting: 	Pas boven de 30.846,- Euro (2022)
	- RoadTax:		Afhankelijk van de type auto
	
	gemeente bijstand aanvragen
	geen WA is een voorschot niet doen
	UVW choach aanvragen (voor ICT werk)
	 			
================================================================================= '''

income = [
["#Work",0, 2500],
["#WW", 0, 0],
["#Dividend",0, 0],
["#TaxReturn",0, 0],
["#Hypotheek", 0, 0],
["#Huurtoeslag", 0, 		fiscaalPartner(329)] 
]

fixed = [
["#Groceries",0, -300],
["#Barber",0, -35],
["#GoingOut",0, -200],
["#Telecom",0, 		fiscaalPartner(-47.50)],
["#Workout",0, -45], 
["#Rent",0, 			fiscaalPartner(-700)],
["#Transport", 0, -75], 
["#FoodDelivery",0, -50], 
["#Clothes",0, -50], 
["#Stock",0, -50], 
["#Save",0, -200],  # 10
["#Pensioen",0, 0],
["#Miscellaneous",0, -100],
["#APK", 0, -5.25],
["#Water", 0, 			fiscaalPartner(-15)],
["#Elektriciteit", 0, 		fiscaalPartner(-600/12) ],
["#Gas", 0, 			fiscaalPartner(-900/12) ],
["#PCsecurity", 0, 		fiscaalPartner(-50/12)],
["#Servicekosten", 0, 		fiscaalPartner(-48)],
["#HouseKeeping", 0, 		fiscaalPartner(-50)],
["#Mobile", 0, -30],
["#Vacation", 0, -50]
]

insurance = [
["#Care", 0, -109.85],
["#Retirement", 0, -44],
["#Inboedel", 0, -9.50],
["#Opstal", 0, 0], # alleen als je eigen huis hebt
["#Aansprakelijkheid", 0, -5],
["#Auto", 0, -75],
["#Reis", 0, -10] # check online
]

taxes = [
["#IncomeTax", 0, -627.92],
["#DividendTax", 0, 0],
["#RoadTax", 0, -26],
["#Rioolheffing", 0, 		fiscaalPartner(-225.84/12)],
["#Afvalstoffenheffing", 0, 	fiscaalPartner(-234.72/12)],
["#Watersysteemheffing", 0, 	round(fiscaalPartner(-60.10/12),2)],
["#Vermogen", 0, 0],
["#HypotheekRente", 0, 0]
]

stock = [
["#EMPTY", 0, 0]
]




''' =================================================================================
			
					Run Scripts
			
================================================================================= '''

# get data from csv
csvList = Csv.genValList(root)

# input csvList and update all lists
Table.UpdateAllLists(csvList,income, fixed, insurance, taxes, stock)


# Pensioen kosten
retirement = Function.PersioenAftrek(income[1][1])
insurance[1][1] = retirement



# Income tax	
incomeTax = Function.InkomstenBelasting(income[1][1])
#income[1][1] = incomeTax[0]	# update income
taxes[0][1] = incomeTax[1]	# update income tax

# Dividend tax
dividend = Function.Dividendbelasting(income[2][1])
#income[2][1] = dividend[0]
taxes[1][1] = dividend[1]

# Wegenbelasting
roadTax = Function.RoadTax()
taxes[2][1] = roadTax

# Rioolheffing kosten
rioolheffing = Function.Rioolheffing(-225.84)
taxes[3][1] = rioolheffing 

# Afvalstoffenheffing kosten
afvalstoffenheffing = Function.Afvalstoffenheffing(-234.72)
taxes[4][1] = afvalstoffenheffing 

# Watersysteemheffing kosten
watersysteemheffing = Function.Watersysteemheffing(-60.10)
taxes[5][1] = watersysteemheffing 

# Vermogen Tax
vermogen = Function.Vermogen2022(0, 0, 0)
taxes[6][1] = vermogen


# Water Cost
water = Function.Water(0)
fixed[14][1] = water


# Elektriciteit Cost
elektriciteit = Function.Elektriciteit(0)
fixed[15][1] = elektriciteit

# Gas Cost
gas = Function.Gas(0)
fixed[16][1] = gas


# Print Tables
Table.Analytics(income, fixed, insurance, taxes, stock)	

# Print total table
total = Table.TotalSum(income, fixed, insurance, taxes)

# export analytic report (JUN)
Csv.exportReport(income, fixed, insurance, taxes, total, reportLoc, "202106_Report.csv")




