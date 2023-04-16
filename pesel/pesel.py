true = 'PESEL is correct'
false = 'PESEL IS INCORRECT'
checksum = 0
check = 0
years = {
'18':['81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92'],
'19':['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
'20':['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
'21':['41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'],
'22':['61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72'],
}
months = {
'01':['81', '01', '21', '41', '61'], 
'02':['82', '02', '22', '42', '62'], 
'03':['83', '03', '23', '43', '63'], 
'04':['84', '04', '24', '44', '64'], 
'05':['85', '05', '25', '45', '65'], 
'06':['86', '06', '26', '46', '66'], 
'07':['87', '07', '27', '47', '67'], 
'08':['88', '08', '28', '48', '68'], 
'09':['89', '09', '29', '49', '69'], 
'10':['90', '10', '30', '50', '70'], 
'11':['91', '11', '31', '51', '71'], 
'12':['92', '12', '32', '52', '72'],
}

def sex(dig):
	if dig % 2 == 0:
		print('Female')
	else:
		print('Male')

def kasztany(dig, dictionary):
	for key, lists in dictionary.items():
		for word in lists:
			if word == dig:
				wanted = key
	return wanted

pesel = input('Enter PESEL:')

if len(pesel) == 11:
	print('Length is correct')
	last = int(pesel[10])
	S = int(pesel[0])*1 + int(pesel[1])*3 + int(pesel[2])*7 + int(pesel[3])*9 \
	+ int(pesel[4])*1 + int(pesel[5])*3 + int(pesel[6])*7 + int(pesel[7])*9 \
	+ int(pesel[8])*1 + int(pesel[9])*3
	checksum = S % 10
	if checksum == 0:
		if checksum == last:
			print(true)
		else:
			print(false)
	else:
		checksum = 10 - checksum
		if checksum == last:
			print(true)
		else:
			print(false)
	print('-' * 23)
	sex(int(pesel[9]))
	print(pesel[4]+pesel[5], '.', kasztany(pesel[2]+pesel[3], months), '.', \
	kasztany(pesel[2]+pesel[3], years), \
	pesel[0]+pesel[1], sep='') #birth date - DD.MM.YYYY
else:
	print('Length is incorrect')