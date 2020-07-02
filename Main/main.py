from game.Board import *
from game.Rules import *
from UI.UserInterface import *
#ask the user for game setup
boardSize = UserInterface.askForBoardSize()
numMines = UserInterface.askForMines(boardSize * boardSize)
#setup the board
rules = Rules(boardSize, numMines)
#additional variables
playGame = True
#main game loop
while playGame:
    UserInterface.displayDevBoard(rules.getBoard())
    rules.checkGameState()
    playGame = False
#game over
print("Thanks for Playing")
