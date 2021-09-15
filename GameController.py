import gui
import TicTacToe

class GameController:
	def __init__(self, gameSize, m):
		self.tictactoe = TicTacToe.ttt(gameSize)
		self.multiplayer = m

	
	def startGame(self):
		gui.GUIController.disGameWindow(self.tictactoe.grid, self.tictactoe.gridSize)


	def drawNextMove(self, index):
		self.grid[index[0]][index[1]] = self.turn

		if (self.turn == "X"): self.turn="O"
		else: self.turn="X"

		winner = self.findWinner()

		if (winner == None):
			gui.GUIController.disGameWindow(gui.GUIController(), self.gridSize)

	