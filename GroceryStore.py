# Note, this could all be done allot nicer (ex. trough OOP, functions, arrays etc.), 
# however, as this is meant to teach conditionals, it's been written to use them as much as possible (which is quite noticable).
# Also, if you're already going ahead by judging this code, you shouldn't be here in first place. This code is for beginners.

# You conclude that I do not visit the grocery store too often.

import os # To get name of operating system

# Cleaning function (OS/Platform specfic). We'll get to functions later
def clearConsole() :
	# Check if windows
	if os.name == 'nt':
		os.system('cls')   # Execute cls command

	else:				   # Assume OS follows POSIX (Unix, GNU/Linux etc...)
		os.system('clear') # Execute clear command

# Initialize variables
exit = False 		 									# Indicates wether used has exited store or not
credits = 1000		 									# Initialize with a total of 1000 credits

# Grocery counters
cheese  	 = 0
salami  	 = 0
yogurt  	 = 0
oranges 	 = 0
potatoes 	 = 0
canned_soup      = 0
orange_juice     = 0
milk 		 = 0

# Stay in store until user exits it
while exit == False: # may alos be written as while !exit:
	clearConsole()

	print("--- Welcome to CTXz grocery store ---\n")

	print("Credits:", credits, '\n')

	print("Cheese\t\t 100 Credits")
	print("Salami\t\t 100 Credits")
	print("Yogurt\t\t 70 Credits")
	print("Oranges\t\t 20 Credits")
	print("Potatoes\t 20 Credits")
	print("Canned Soup\t 40 Credits")
	print("Orange Juice\t 100 Credits")
	print("Milk\t\t 150 Credits\n")

	choice = input("Please choose a grocery: ")

	# User has chosen to purchase cheese
	if choice == "Cheese":

		if credits >= 100:
			credits -= 100
			cheese += 1
			print("Purchased cheese")

		else:
			print("Hmm looks like you're missing", 100 - credits, "credits to purchase cheese")

	elif choice == "Salami":

		if credits >= 100:
			credits -= 100
			salami += 1
			print("Purchased salami")

		else:
			print("Hmm looks like you're missing", 100 - credits, "credits to purchase salami")

	elif choice == "Yogurt":

		if credits >= 70:
			credits -= 70
			yogurt += 1
			print("Purchased yogurt")

		else:
			print("Hmm looks like you're missing", 70 - credits, "credits to purchase yogurt")

	elif choice == "Oranges":

		if credits >= 20:
			credits -= 20
			oranges += 1
			print("Purchased oranges")

		else:
			print("Hmm looks like you're missing", 20 - credits, "credits to purchase oranges")

	elif choice == "Potatoes":

		if credits >= 20:
			credits -= 20
			potatoes += 1
			print("Purchased potatoes")

		else:
			print("Hmm looks like you're missing", 20 - credits, "credits to purchase potatoes")

	elif choice == "Canned Soup":

		if credits >= 40:
			credits -= 40
			canned_soup += 1
			print("Purchased canned soup")

		else:
			print("Hmm looks like you're missing", 40 - credits, "credits to purchase canned soup")

	elif choice == "Orange Juice":

		if credits >= 100:
			credits -= 100
			orange_juice += 1
			print("Purchased orange juice")

		else:
			print("Hmm looks like you're missing", 100 - credits, "credits to purchase orange juice")

	elif choice == "Milk":

		if credits >= 150:
			credits -= 150
			milk += 1
			print("Purchased milk")

		else:
			print("Hmm looks like you're missing", 150 - credits, "credits to purchase milk")

	else:
		print("Sorry, we don't sell", choice)


	answered = False

	while answered == False: # may also be written as while !answered:
		
		decision = input("Continue shopping (yes/no): ")
		
		if decision == "no" or decision == "No" or decision == 'n':
			exit = True
			answered = True

		elif decision == "yes" or decision == "Yes" or decision == 'y':
			answered = True

# Print what user has bought
purchased = "You've bought "
if cheese > 0: # may also be written as if cheese >= 1: or even if cheese:
	purchased += str(cheese) + " piece"
	if cheese > 1:
		purchased += 's' # Plural
	
	purchased += " of cheese, "

if salami > 0:
	purchased += str(salami) + " piece"
	if salami > 1:
		purchased += 's' # Plural
	
	purchased += " of salami, "

if yogurt > 0:
	purchased += str(yogurt) + " yogurt"
	if yogurt > 1:
		purchased += 's'

	purchased += ', '

if oranges > 0:
	purchased += str(oranges) + " orange"
	if oranges > 1:
		purchased += 's'
	
	pruchased += ', '

if potatoes > 0:
	purchased += str(potatoes) + " package"
	if potatoes > 1: 
		purchased += 's'
		
	purchased += " of potatoes, "

if canned_soup > 0:
	purchased += str(canned_soup) + " soupcan"
	if canned_soup > 1:
		purchased += 's'

	purchased += ', '

if orange_juice > 0:
	purchased += str(orange_juice) + " bottle"
	if orange_juice > 1:
		purchased += 's'
	
	purchased += " of orange juice, "

if milk > 0:
	purchased += str(milk) + " bottle"
	if milk > 1:
		purchased += 's'
	
	purchased += " of milk, "

purchased = purchased[0:len(purchased)-2] # Get rid of ', '

print(purchased)
