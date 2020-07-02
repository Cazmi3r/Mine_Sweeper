import sys

class UserInterface:#use this to run the game in CMD

        def __init__(self):
            x=0

        def updateBoard(gBoard):#displays board to player
            gBoard.toString()

        def askForBoardSize():
            #error handling
            boardSize = 0
            while boardSize < 2:
                try:
                    boardSize = int(input("please enter the board size"))
                except:
                    print("Please Enter a Positve number")
            return boardSize

        def askForMines(maxNumMines):
            #error handling
            mines = 0
            while(mines < 1) or (mines > maxNumMines - 2):#stops mines from being negative and
                try:                                      #stops mines from ending the game as it starts
                    mines = int(input("please enter the number of mines"))
                except:
                    print("Please Enter a Positve number")
            return mines

        def getCords():#gets Cords from user and converts it to an arry of [x,y]
            toReturn = input("where at?")
            toReturn = toReturn.split(',')
            toReturn[0] = int(toReturn[0])
            toReturn[1] = int(toReturn[1])
            toReturn[0] = toReturn[0] - 1
            toReturn[1] = toReturn[1] - 1
            return toReturn

        def userInput(gBoard):
            switcher = input("What would you like to do?")
            if switcher == "flag":
                return UserInterface.userFlag(gBoard)
            elif switcher == "click":
                return UserInterface.userClick()
            elif switcher == "quit":
                return UserInterface.userQuit()

        def userFlag(gBoard):
            gBoard.addFlag(UserInterface.getCords())
            return True

        def userClick():
            return True

        def userQuit():
            return False

        def help():#should print out an explanation of the rules and how to play
            pass
