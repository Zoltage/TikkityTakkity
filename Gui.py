from tkinter import *
from tkinter import font
from main import *
import sys
import TicTacToe


window = Tk()
window.config(padx=15, pady=15)

class GUIController:
	def __init__(self):
		self.backgroundColor = "#3b3b3b"
		self.titleColor = "#64ffff"
		self.frameColor = "#3b3b3b"

		self.buttonTextColor = "#64ffff"
		self.buttonColor = "#646464"
		self.buttonPressedColor = "#333333"
		self.buttonHovorColor = "#b0b0b0"

		# Single = 0, multiplayer = 1
		self.buttonList = [[None, self.buttonColor], [None, self.buttonColor]]	

		self.tictactoe = None
		self.minimax = None

		self.gameMode = None
		self.sliderValue = 3
		self.gridSlider = 3

	def resetVariables(self):
		# Single = 0, multiplayer = 1
		self.buttonList = [[None, self.buttonColor], [None, self.buttonColor]]	

		self.tictactoe = None

		self.gameMode = None

		self.sliderValue = 3
		self.gridSlider = 3

	#Displaying the home window, is the first window called
	def disHome(self):
		# Is called at the beginning of each window function to clear the window before we draw on it again
		self.clearScreen()

		# Reset all values
		self.resetVariables()

		# Creating the frames
		topFrame = Frame(window)
		middleFrames = Frame(window, pady=10, relief=RIDGE, bd=2)
		middleFrameTop = Frame(middleFrames, padx=15, pady=0)
		middleFrameMid = Frame(middleFrames, padx=15, pady=0)
		middleFrameBot = Frame(middleFrames, padx=15, pady=0)
		bottomFrame = Frame(window)

		# Display the title
		Label(topFrame, text="Tic Tac Toe", bg=self.backgroundColor, fg=self.titleColor, font=("System", 35)).grid(column=0, row=0, pady=15)


		# Displaying Single Player Button
		self.buttonList[0][0] = Button(middleFrameTop, text="Single Player", bg=self.buttonList[0][1], fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 command=lambda x="s": self.setGameMode(x))
		self.buttonList[0][0].grid(column=0, row=0, padx=2, pady=2)

		# Displaying Multiplayer Button
		self.buttonList[1][0] = Button(middleFrameTop, text="Multiplayer", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 command=lambda x="m": self.setGameMode(x))
		self.buttonList[1][0].grid(column=0, row=1, padx=2, pady=2)

		# Changing the button colors when the mouse is hovored over
		for button in self.buttonList:
			self.onHover(button[0], self.buttonHovorColor, button[1])

		# Displaying the slider to change the game grid size
		Label(middleFrameBot, text="Enter Board Size:", bg=self.frameColor, fg=self.titleColor,).grid(column=0, row=0)
		
		self.gridSlider = Scale(middleFrameBot, from_=3, to=21, orient=HORIZONTAL, bg=self.frameColor, fg=self.buttonTextColor,
		activebackground=self.backgroundColor, troughcolor=self.buttonColor,
		 variable=self.sliderValue, command=self.updateSliderValue)
		self.gridSlider.grid(column=0, row=1, sticky="nsew", padx=20, pady=2)

		self.gridSlider.config()

		# Display the exit button
		Button(bottomFrame, text="Exit", bg="red", fg=self.buttonTextColor, width=10, command=lambda: sys.exit(), relief=GROOVE).grid(column=0, row=0, padx=5, pady=15, sticky="nsew")

		# Displaying the start button
		sB = Button(bottomFrame, text="Start", bg="#4ABF36", activebackground="#62FA47", fg=self.buttonTextColor, 
		width=10, relief=GROOVE, command=lambda: self.gameWindow((self.gridSlider.get(), True)))
		sB.grid(column=1, row=0, padx=5, pady=15, sticky="nsew")
		self.onHover(sB, "#56F222", "#4ABF36")

		# Displaying the frames
		topFrame.grid(column=0, row=0)
		middleFrames.grid(column=0, row=1)
		middleFrameTop.grid(column=0, row=0)
		middleFrameMid.grid(column=0, row=1)
		middleFrameBot.grid(column=0, row=2)
		bottomFrame.grid(column=0, row=2)
		
		# Setting the background colors
		topFrame.configure(bg=self.backgroundColor)
		middleFrames.configure(bg=self.frameColor)
		middleFrameTop.configure(bg=self.frameColor)
		middleFrameMid.configure(bg=self.frameColor)
		middleFrameBot.configure(bg=self.frameColor)
		bottomFrame.configure(bg=self.backgroundColor)
		window.configure(bg=self.backgroundColor)

		window.mainloop()
  
	# Displaying the game window
	def gameWindow(self, p):

		gridSize = p[0]
		initial = p[1]

		if (initial):
			self.tictactoe = TicTacToe.ttt(gridSize)

		# Clear the current window
		self.clearScreen()

		topFrame = Frame(window)
		gameFrame = Frame(window, padx=15, pady=15)
		gridBackgroundFrame = Frame(gameFrame)
		bottomFrame = Frame(window)

		frames = []
		self.buttonList = []
		for i in range(gridSize):
			(i)
			frames.append([])
			self.buttonList.append([])
			for j in range(gridSize):
				px = ((j != 0) * 2,  (j != gridSize-1) * 2)
				py = ((i != 0) * 2,  (i != gridSize-1) * 2)
				frames[i].append(Frame(gridBackgroundFrame, bg=self.frameColor,
				 width=int(400/gridSize), height=int(400/gridSize)))
				frames[i][j].pack_propagate(False)
				frames[i][j].grid(row=i, column=j, padx=px, pady=py)

				self.buttonList[i].append(Button(frames[i][j], text=" ",
				 bg=self.frameColor, fg=self.buttonTextColor, relief=FLAT,
				 command=lambda p=(i, j): self.buttonClick(p)))
				self.buttonList[i][-1].pack(expand=True, fill=BOTH)


		# Displaying the score and who's turn it is
		Label(topFrame, text="Player 1", bg=self.frameColor, fg=self.titleColor, padx=5).grid(column=0, row=0, sticky="nsew")
		Label(topFrame, text="", bg=self.backgroundColor, padx=10).grid(column=1, row=0, sticky="nsew")
		Label(topFrame, text="Player 2", bg=self.frameColor, fg=self.titleColor, padx=5).grid(column=2, row=0, sticky="nsew")

		# Displaying the exit button
		Button(bottomFrame, text="Exit", bg="red", fg=self.buttonTextColor, width=10,
		 command=lambda: sys.exit(), relief=GROOVE).grid(column=0, row=0, padx=5, pady=15, sticky="nsew")

		# Displaying the home button
		sB = Button(bottomFrame, text="Home", bg="#4ABF36", activebackground="#62FA47", fg=self.buttonTextColor,
		 width=10, relief=GROOVE, command=self.disHome)
		sB.grid(column=1, row=0, padx=5, pady=15, sticky="nsew")
		self.onHover(sB, "#56F222", "#4ABF36")


		topFrame.grid(column=0, row=0, pady=15)
		gameFrame.grid(column=0, row=1)
		gridBackgroundFrame.grid(column=0, row=0)
		bottomFrame.grid(column=0, row=2, pady=5, sticky="n")
		# Drawing Background 
		topFrame.configure(bg=self.backgroundColor)
		gameFrame.configure(bg=self.frameColor)
		gridBackgroundFrame.configure(bg=self.buttonColor)
		bottomFrame.configure(bg=self.backgroundColor)

		window.mainloop()

		# Called when the user clicks a grid in the game board

	# Called when a grid button is clicked
	def buttonClick(self, index):
		self.buttonList[index[0]][index[1]]['font'] = self.findFontSize(self.tictactoe.gridSize)
		self.buttonList[index[0]][index[1]]['text'] = ("X" if self.tictactoe.turn==1 else "O")

		self.tictactoe.updateGameGrid(index)

		if (self.tictactoe.winner != None):
			if (self.tictactoe.winner == 1):
				messagebox.showinfo("Winner", "Player 1 Wins!!")
			elif (self.tictactoe.winner == -1): 
				messagebox.showinfo("Loser", "Player 2 Wins!!")
			elif (self.tictactoe.winner == 0):
				messagebox.showinfo("Tie", "This match has resulted in a tie")

			self.disHome()
			

		if (self.gameMode == "s"):
			if (self.tictactoe.turn == -1):
				# Random choice for computer
				self.buttonClick(self.tictactoe.randomIndex())

	# Function to change properties of button on hover
	def onHover(self, button, colorOnHover, colorOnLeave):
		# Adjusting backgroung of the widget
		# Background on entering widget
		button.bind("<Enter>", func=lambda e: button.config(
			background=colorOnHover))
	
		# Background color on leaving widget
		button.bind("<Leave>", func=lambda e: button.config(
			background=colorOnLeave))

	# Clears the screen
	def clearScreen(self):
		for widget in window.winfo_children():
			widget.destroy()

	def findFontSize(self, size):
		s = 22
		if (size==3): s = 80
		elif (5 <= size <= 9): s = 40
		elif (11 <= size <= 15): s = 25
		else: s = 18

		f = font.Font(family="Roboto", size=s)
		return f

	def updateSliderValue(self, variable):
		temp = int(variable)
		if (temp%2==0):
			self.gridSlider.set(temp+1)

	def setGameMode(self, m):

		if (m == "s"):
			if (self.gameMode == None):
				self.buttonList[0][1] = self.buttonPressedColor
				self.gameMode = m
			elif (self.gameMode == "s"):
				self.buttonList[0][1] = self.buttonColor
				self.gameMode = None
				
			self.buttonList[0][0].configure(bg=self.buttonList[0][1])
			self.onHover(self.buttonList[0][0], self.buttonHovorColor, self.buttonList[0][1])
		else:
			if (self.gameMode == None):
				self.buttonList[1][1] = self.buttonPressedColor
				self.gameMode = m
			elif (self.gameMode == "m"):
				self.buttonList[1][1] = self.buttonColor
				self.gameMode = None


			self.buttonList[1][0].configure(bg=self.buttonList[1][1])
			self.onHover(self.buttonList[1][0], self.buttonHovorColor, self.buttonList[1][1])
		
	def displayLetter(self):
		if (self.tictactoe.turn == 1):
			return "X"
		elif (self.tictactoe.turn == -1): 
			return "O"
		else:
			return " "