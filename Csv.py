import csv



def CSVtags(root):
	'''
	input the path to your csv file and output is list of all the unique tags
	'''

	# Initialize List
	tag_set = set()
	valueM_list = []
	dateM_list = []


	# loop file: Create Tag_list
	file = open(root)
	for line in file:

		# get tag
		row = line.strip().replace('"','').split(';')
		#print(row[-1])

		# break loop
		if (row[-1] == ''):
			break

		# Create set list
		tag_set.add(row[-1])

	# Convert set to list
	tag_list = list(tag_set)
	tag_list.remove('Tag')

	#for x in tag_list:
		#print(x)
	
	'''
	Example:
	
	#Rent
	#Workout
	#Miscellaneous
	#Groceries
	#Care
	#FoodDelivery
	#GoingOut
	#Taxes
	#Barber
	#WW
	#Stock
	#Telecom
	'''
	return tag_list
	





def genValList(root):
	'''
	input the root to the csv file and
	output a nested list with the tag and the sum of all tag values
	'''

	# generate tag list
	tagList = CSVtags(root)
	
	# create empty nested list
	nestedList=[]  
	for x in range(len(tagList)):
   		nestedList.append([])
   
   	# convert tagList to nestedList
	for x in range(len(tagList)):
		nestedList[x].append(tagList[x])
		#print(nestedList)
	
	# iterate csv file
	file = open(root)
	for line in file:

		# fix values, positive or negative
		alist = line.strip().replace('"','').split(';')
		afbij = alist[5] 
		val = alist[6]
		valB = val.replace(",", ".")

		# create negative value
		if (afbij == "Af"):
			val =  -abs(float(valB))
		# create positive value
		if (afbij == "Bij"):
			val = float(valB)
		
		tag = alist[-1]
		#print(tag)
		#print(afbij)
		#print(val)
	
		# sort value to nested tag list
		for x in range(len(tagList)):
			if (tag == tagList[x] ):
				#print("true")
				nestedLen = (len(nestedList[x]))
				#print(nestedLen)	
				nestedList[x].append(val)	
	
	# print nestedList
	#for x in range(len(nestedList)):
		#print(nestedList[x])
		
		
	# create empty nested list
	nestedListB=[]  
	for x in range(len(tagList)):
		nestedListB.append([])
	
	
	# sum up values
	for x in range(len(nestedList)):
		tag = nestedList[x][0]
		nestedList[x].pop(0)
		val = sum(nestedList[x])
		nestedListB[x].append(tag)
		nestedListB[x].append(round(val,2))
		

	# print nestedList
	#for x in range(len(nestedListB)):
		#print(nestedListB[x])
		
	'''
	Example:
	
	['#WW', 1692.5]
	['#Workout', -43.0]
	['#Taxes', 107.0]
	['#Stock', -51.01]
	['#Rent', -350.5]
	['#Telecom', -23.24]
	['#Barber', -27.0]
	['#Groceries', -351.76]
	['#Miscellaneous', -130.77]
	['#Care', -148.35]
	['#GoingOut', -359.05]
	['#FoodDelivery', -59.45]

	'''	
	return nestedListB



def exportReport(income, fixed, insurance, taxes, total, root, fileName):
	'''
	Input all lists and  
	output a unique csv file with all the lists of values
	'''
	rowIncome = "Income",""
	rowFixed = "fixed",""
	rowInsurance = "insurance",""
	rowTaxes = "taxes",""
	rowTotal = "total",""
	
	# open the file in the write mode
	f = open(root+fileName, 'w')

	# create the csv writer
	writer = csv.writer(f)

	# write a row to the csv file
	writer.writerow(rowIncome)
	for x in range(len(income)):
		writer.writerow(income[x])
		
	writer.writerow(rowFixed)
	for x in range(len(fixed)):
		writer.writerow(fixed[x])
		
	writer.writerow(rowInsurance)
	for x in range(len(insurance)):
		writer.writerow(insurance[x])
		
	writer.writerow(rowTaxes)
	for x in range(len(taxes)):
		writer.writerow(taxes[x])
		
	writer.writerow(rowTotal)
	for x in range(len(total)):
		writer.writerow(total[x])
		
	print("\nfile: {}, saved to disk".format(fileName))


	# close the file
	f.close()
