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
    print("\n")
    print("Dev Board")
    UserInterface.displayDevBoard(rules.getBoard())
    print("\n")
    print("Game Board")
    UserInterface.displayGameBoard(rules.getBoard())
    rules.checkGameState()
    print("\n")
    playGame = UserInterface.userInput(rules)
#game over
print("Thanks for Playing")
