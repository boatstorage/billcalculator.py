def tip(bill_amount, tip_percent):
	tip_amount = bill_amount * tip_percent * .01
	return tip_amount
def total_bill(bill_amount, tip_amount):
	bill_and_tip = bill_amount + tip_amount
	return bill_and_tip
def split(bill_and_tip, number_people):
	split_bill = bill_and_tip / number_people
	return split_bill

def main():
	choice = raw_input("choose '1' for calculator tip, choose '2' for split the bill")
	if choice == '1':
		bill_amount = raw_input("what is the bill amount?")
		tip_percent = raw_input("what is the tip percent?")
		tip_amount = float(bill_amount) * float(tip_percent) * .01
		total_bill = float(bill_amount) + float(tip_amount)
		print "the tip amount is $" + str(tip_amount)
		print " the total bill is $" + str(total_bill)
		split_number = raw_input("would you like to split the bill by how many people?")
		cost_per_person = float(total_bill) / float(split_number)
		print "The total per person is $" + str(cost_per_person)
	elif choice == '2':
		bill_amount = raw_input("what is the total bill amount?")
		split_number = raw_input("would you like to split the bill by how many people?")
		print "The cost per person is $" + str(float(bill_amount) / float(split_number))
if __name__ == '__main__':
    	 	main()