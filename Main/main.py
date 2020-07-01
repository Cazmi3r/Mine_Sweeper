from game.Board import *
from game.Rules import *
from game.UserInterface import *

gBoard = Board(UserInterface.askForBoardSize())
UserInterface.updateBoard(gBoard)
