from game.Board import *
from game.Rules import *
from UI.UserInterface import *
#ask the user for game setup
boardSize = UserInterface.askForBoardSize()
numMines = UserInterface.askForMines(boardSize * boardSize)
#setup the boards
gBoard = Board(boardSize)
rBoard = Board(boardSize)
rBoard.addMine(numMines)
#setup the Rules
rules = Rules(gBoard, rBoard)
#additional variables
playGame = True
devMode = False
#main game loop
if devMode:
    while playGame:
        print("game board")
        UserInterface.updateBoard(gBoard)
        print("Refrence board")
        UserInterface.updateBoard(rBoard)
        playGame = UserInterface.userInput(gBoard, rBoard)
        rules.checkGameState()
else:
    while playGame:
        UserInterface.updateBoard(gBoard)
        playGame = UserInterface.userInput(gBoard, rBoard)
        rules.checkGameState()
#game over
print("Thanks for Playing")
