f = int(input("Amount -> 120:\t   "))
while True:
	try:
		i = int(input("Discount(%) -> 40: "))
		print("\t\t", f*(100-i)/100)
	except:
		break
