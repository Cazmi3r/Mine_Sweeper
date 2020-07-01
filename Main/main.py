from game.Board import *
from game.Rules import *
from game.UserInterface import *

boardSize = UserInterface.askForBoardSize()
numMines = UserInterface.askForMines(boardSize * boardSize)

gBoard = Board(boardSize)
rBoard = Board(boardSize)
UserInterface.updateBoard(gBoard)
