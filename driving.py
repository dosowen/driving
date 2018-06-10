country = input ('what country do you belong:')
age = input ('how old are you:')
age = int (age)
if country == 'Taiwan':
	if age >= 18:
		print ("you can have a driver's license")
	else:
		print ("you cannot have a driver's license")
if country == 'America':
	if age >= 16:
		print ("you can have a driver's license")
	else:
		print ("you cannot have a driver's license")
else:
	print ("you can only choose Taiwan or America")