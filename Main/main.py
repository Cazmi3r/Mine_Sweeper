from game.Board import *
from game.Rules import *
from UI.UserInterface import *

boardSize = UserInterface.askForBoardSize()
numMines = UserInterface.askForMines(boardSize * boardSize)

gBoard = Board(boardSize)
rBoard = Board(boardSize)
rBoard.addMine(numMines)
print("game board")
UserInterface.updateBoard(gBoard)
print("Refrence board")
UserInterface.updateBoard(rBoard)
UserInterface.userInput(gBoard)

print("game board")
UserInterface.updateBoard(gBoard)
print("Refrence board")
UserInterface.updateBoard(rBoard)
