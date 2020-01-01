import random
from enum import Enum

running = True

class rpsGame:
	def __init__(self):
		self.userChoice = items.NULL
		self.aiChoice = items.NULL
		self.winner = entity.NULL

	def setUserChoice(self, choice):
		self.userChoice = items(int(choice))

	def getUserChoice(self):
		return items(self.userChoice).name

	def generateAiChoice(self):
		self.aiChoice = items(random.randint(1, 3))

	def getAiChoice(self):
		return items(self.aiChoice).name

	def calculateWinner(self):
		if self.userChoice == items.ROCK:
			if self.aiChoice == items.ROCK: self.winner = entity.NONE
			if self.aiChoice == items.PAPER: self.winner = entity.AI
			if self.aiChoice == items.SCISSORS: self.winner = entity.PLAYER
		if self.userChoice == items.PAPER:
			if self.aiChoice == items.ROCK: self.winner = entity.PLAYER
			if self.aiChoice == items.PAPER: self.winner = entity.NONE
			if self.aiChoice == items.SCISSORS: self.winner = entity.AI
		if self.userChoice == items.SCISSORS:
			if self.aiChoice == items.ROCK: self.winner = entity.AI
			if self.aiChoice == items.PAPER: self.winner = entity.PLAYER
			if self.aiChoice == items.SCISSORS: self.winner = entity.NONE

	def getWinner(self):
		if self.winner == entity.NONE:
			winner = "Draw!"
		elif self.winner == entity.PLAYER:
			winner = "Player Wins!"
		elif self.winner == entity.AI:
			winner = "AI Wins!"
		return winner

	def compareWinner(self):
		if self.winner == entity.PLAYER:
			comp = " > "
		elif self.winner == entity.AI:
			comp = " < "
		else:
			comp = " = "
		return comp

class items(Enum):
	NULL = 0
	ROCK = 1
	PAPER = 2
	SCISSORS = 3

class entity(Enum):
	NULL = 0
	PLAYER = 1
	AI = 2
	NONE = 3


def main():
	# Initialize rpsGame class
	game = rpsGame()

	print("Rock Paper Scissors!")
	print("=======================")
	while running:
		print("")
		print("1 - Rock")
		print("2 - Paper")
		print("3 - Scissors")
		game.setUserChoice(input(">"))
		print("")
		print("AI is thinking...")
		game.generateAiChoice()
		print("")
		game.calculateWinner()
		print(game.getUserChoice(), game.compareWinner(), game.getAiChoice())
		print(game.getWinner())
	#end


if __name__ == "__main__":
	main()
