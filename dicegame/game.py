#intro
#this is a 2-player dice game
import random

cumulativeScore=0

def menuChoice():
	print("Option 1: Display rules")
	print("Option 2: Start new game")
	print("Option 3: Quit")
	print("What would you like to do?")
	choice=input();
	while choice != 1 and choice != 2 and choice != 3:
		print("That is not a valid choice")
		print("Please enter a number between 1 and 3")
		choice=input()
	return choice
	
#subroutine to display rules

def displayRules():
	print("The rules of the game are as follows:")
	print("Players take turns to throw two dice.")
	print("If the throw is a 'double', i.e. two 2s, two 3s, etc.,")
	print("the player's score reverts to zero and their turn ends.")
	print("(etc.)")
	
def playerTurn(player,score):
	print("Your turn, "+player)
	anotherGo="Y"
	scoreThisTurn=0
	Dice=[1,2,3,4,5,6]
	while anotherGo=="y" or anotherGo=="Y":
		#generate dice
		die1=random.choice(Dice)
		die2=randowm.choice(Dice)
		print("You rolled "+die1+" and "+die2)
		if die1 == die2:
			scoreThisTurn=0
			cumulativeScore=0
			print("Bad luck! Press any key to continue")
			#Press any key to continue
			anotherGo="N"
		else:
			scoreThisTurn=scoreThisTurn+die1+die2
			cumulativeScore=cumulativeScore+scoreThisTurn
			print("Your score this turn is "+scoreThisTurn)
			print(player+", Your cumulative score is "+cumulativeScore)
			if cumulativeScore >=50:
				anotherGo="N"
			else:
				print("Another go? (Answer Y or N)")
				anotherGo=input()
	return cumulativeScore

#subroutine to play game
def playGame():
	score1=0
	score2=0
	print("Enter Player 1's name: ")
	player1=input()
	print("Enter Player 2's name: ")
	player2=input()
	while score1 < 50 and score2 < 50:
		score1=playerTurn(player1,score1)
		if score1 >= 50:
			print("You win!")
		else:
			score2=playerTurn(player2,score2)
			if score2 >=50:
				print("You win!")

#main program starts here
option=menuChoice()
while option != 3:
	if option == 1:
		displayRules()
	else:
		playGame()
	option=menuChoice()
print("Goodbye!")

			

		