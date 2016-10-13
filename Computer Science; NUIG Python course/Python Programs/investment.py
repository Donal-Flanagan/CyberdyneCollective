def investment():
	print "This program will output the years required for an investment to double at a given interest rate"
	prin = input("Input the initial investment(principal) here: ")
	apr  = input("Input the annual interest rate here in the format 0.XX: ")
	apr=1+apr
	years = 0
	final=0
	newprin=prin
	while final<(prin*2):
		newprin = newprin*apr
		final=newprin
		years = years + 1
		print "Year", years, ", investment value =", final
	print "It will take", years, "years for the investment's value to double."
	investment()
