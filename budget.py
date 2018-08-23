yr_income = {}

name = raw_input("Enter your name\n>")
print "How are you, %s? Please enter your monthly income" %name
mth_inc = raw_input("USD $")

yr_income[name] = int(mth_inc)*12


def judge():
	if yr_income[name] <= 35000 :
		print "Damn, %s. You must be living check to check...\nCan I send you some cup noodles?" %name
		nood()
	
			
	elif yr_income[name] <= 40000 :
		print "%s, you should probably live frugally" %name
		exit(0)
			
	elif yr_income[name] <= 70000 :
		print "%s, if you're single, you're probably living comfortably" %name
		exit(0)
		
	elif yr_income[name] <= 100000 :
		print "%s, you probably have some disposible income. Congrats!" %name
		exit(0)
	
	elif yr_income[name] > 100000 :
		print "%s, lucky you" 
		exit(0)
				
	
def nood():
	nood_res = raw_input("Y/N\n>")

	# add loop here for true statements 		
	if "Y" and "y" in nood_res :
		address = raw_input("Please enter your address below:\n>")
		phone = raw_input("Please enter your phone number:\n>")
		
		print "Got it. Will send 12 packs of cup noodles to:\n%s\n%s\n%s\nHave a good day" %(name , phone , address)
		exit(0)
			
	if "N" and "n" in nood_res :
		print "I respect your dignity.\nDumb, but I respect it. Good luck, %s" %name
		exit(0)
	
		
judge()
