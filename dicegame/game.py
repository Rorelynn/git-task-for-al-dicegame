#intro
#this is a 2-player dice game
def menuChoice():
	print("Option 1: Display rules")
	print("Option 2: Start new game")
	print("Option 3: Quit")
	print("What would you like to do?")
	choice=input();
	while (choice != 1 and choice != 2 and choice != 3):
		print("That is not a valid choice")
		print("Please enter a number between 1 and 3")
		choice=input()
	return choice
		