from game.Board import *
from game.Rules import *
from UI.UserInterface import *

boardSize = UserInterface.askForBoardSize()
numMines = UserInterface.askForMines(boardSize * boardSize)
playGame = True

gBoard = Board(boardSize)
rBoard = Board(boardSize)
rBoard.addMine(numMines)

while playGame:
    Rules.checkGameState(gBoard,rBoard)
    print("game board")
    UserInterface.updateBoard(gBoard)
    print("Refrence board")
    UserInterface.updateBoard(rBoard)
    playGame = UserInterface.userInput(gBoard, rBoard)

print("Thanks for Playing")
