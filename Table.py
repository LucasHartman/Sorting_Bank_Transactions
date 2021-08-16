
''' =================================================================================
			
				Define Table Layout Functions
			
================================================================================= '''


def SearchList(listName, hashtag):
	'''
	get value from any nested list 
	
	select a hashtag (first value in the nested list)
	and get the value ( second value in the nest list)
	return value
	'''
	hastagValue = 0
	for x in range(len(listName)):
		try:
			if (listName[x][0] == hashtag):
				hastagValue = listName[x][1]
				print ("found hastag {}: € {}".format(listName[x][0], listName[x][1]))
		except:
			print("hastag ({}) not found or has no value".format(hashtag))	
			
	return hastagValue






def UpdateValue(listName, hashtag, addVal):
	'''
	updating an existing value by adding up
	
	'''
	for x in range(len(listName)):
		if (listName[x][0] == hashtag):
			listName[x][1] = listName[x][1] + addVal
			print ("update hastag {}: € {}".format(listName[x][0], listName[x][1]))

		

# list updater
def UpdateList(cvsList, tableList, x):
		# update list
		for y in range(len(tableList)):
			if (cvsList[x][0] == tableList[y][0]):
				tableList[y][1] = cvsList[x][1]
# update all lists
def UpdateAllLists(cvsList, income, fixed, insurance, taxes, stock):
	for x in range(len(cvsList)):
		UpdateList(cvsList, income, x)
		UpdateList(cvsList, fixed, x)
		UpdateList(cvsList, insurance, x)
		UpdateList(cvsList, taxes, x)
		UpdateList(cvsList, stock, x)




def GenRow(rowLen, val):
	'''
	create a print row
	'''
	lenval = len(str(val))
	#print(lenval)
	
	row = ""
	for x in range(rowLen-lenval):
		row = row+"."
	#print(row+str(val))
	return row+str(val)
	
	'''
	Example
	
	...............EMPTY
	'''





def GenTable(tableName, dataList):
	'''
	generate table with the values of the lists
	'''
	# gen ____________________
	line = ""
	for x in range(80):
		line = line+"_"
		
	# gen table lables
	print("\n\n\n{}".format(tableName))	
	print(line)
	# print top row
	rowName = GenRow(20, "Tag")
	rowData = GenRow(20, "TRANSACTION")
	rowEst = GenRow(20, "ESTIMATION")
	rowBal = GenRow(20, "DIVERGENCE")
	print(rowName+rowData+rowEst+rowBal)		
	print(line)
	
	# plot data into table
	for x in range(len(dataList)):
		print("")
		rowName = GenRow(20, dataList[x][0][1:])
		rowData = GenRow(20, dataList[x][1])
		rowEst = GenRow(20, dataList[x][2])
		rowBal = GenRow(20, round(dataList[x][1]-dataList[x][2],2))
		print(rowName+rowData+rowEst+rowBal)
	print(line)
	
	'''
	Example:
	
	INCOME
	________________________________________________________________________________
	.................Tag.........TRANSACTION..........ESTIMATION..........DIVERGENCE
	________________________________________________________________________________

	...............EMPTY...................0...................0...................0
	________________________________________________________________________________
	'''
	






def Analytics(income, fixed, insurance, taxes, stock):
	'''
	get a print of all values
	'''
	GenTable("INCOME", income)		
	GenTable("FIXED CHARGES", fixed)
	GenTable("INSURANCE", insurance)
	GenTable("TAXES", taxes)
	#GenTable("STOCK", stock)






def TotalSum(income, fixed, insurance, taxes):
	'''
	Sum all lists
	'''
	transIncome = 0
	estIncome = 0
	
	transFixed = 0
	estFixed = 0
	
	transInsurance = 0
	estInsurance = 0
	
	transTaxes = 0
	estTaxes = 0

	# sum Lists
	for x in range(len(income)):
		transIncome = transIncome + income[x][1]
		estIncome = estIncome + income[x][2]
	
	for x in range(len(fixed)):
		transFixed = transFixed + fixed[x][1]
		estFixed = estFixed + fixed[x][2]

	for x in range(len(taxes)):
		transTaxes = transTaxes + taxes[x][1]
		estTaxes = estTaxes + taxes[x][2]
			
	for x in range(len(insurance)):
		transInsurance = transInsurance + insurance[x][1]
		estInsurance = estInsurance + insurance[x][2]

	transList = [ transIncome, transFixed, transInsurance, transTaxes ]
	estList = [ estIncome, estFixed, estInsurance, estTaxes ]

	# print Table	
	sumList = [ 
	["#Income", transIncome, estIncome],
	["#Fixed", transFixed, estFixed],
	["#Insurance", transInsurance, estInsurance],
	["#Taxes", transTaxes, round(estTaxes)],
	["#Total", round(sum(transList),2), round(sum(estList),2)]
	]
	
	GenTable("TOTAL", sumList)
	
	# print list
	#for x in range(len(sumList)):
		#print(sumList[x])
	
	'''
	Example:
	
	['#Income', 1692.5, 2829]
	['#Fixed', -1395.78, -1749.08]
	['#Insurance', -192.35, -256.35]
	['#Taxes', -697.31, -676]
	['#Total', -592.94, 147.96]

	'''
	return sumList
	


	

	
	
