import sys

class UserInterface:#use this to run the game in CMD

        def __init__(self):
            x=0

        def displayDevBoard(board):#displays dev board to player
            print(board.toString())

        def displayGameBoard(board):#displays game board to player
            size = board.getSize()
            toReturn = []
            cords = [0,0]
            for i in range(size):
                cords[0] = i
                toReturn.append("\n")
                for j in range(size):
                    cords[1] = j
                    targetSpace = board.getSpace(cords)
                    toDisplay = str(UserInterface.displaySpace(targetSpace))
                    toReturn.append(toDisplay)
            return print(''.join([toReturn[x] for x in range(len(toReturn))]))

        def displaySpace(space):#returns a string of what a space should display
            #returns flag
            if space.getFlag() == True:
                return "F"
            #Returns Default
            if space.getRevealed() == False:
                return "#"
            if space.getRevealed() == True:
                #Returns Mine
                if space.getMine() == True:
                    return "X"
                #Returns number of surrounding Mines
                else:
                    return space.getNumOfSurroundingMines()

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

        def userInput(rules):
            switcher = input("What would you like to do?")
            if switcher == "flag":
                return UserInterface.userFlag(rules)
            elif switcher == "reveal":
                return UserInterface.userReveal(rules)
            elif switcher == "quit":
                return UserInterface.userQuit(rules)

        def userFlag(rules):
            rules.addFlag(UserInterface.getCords())
            return True

        def userReveal(rules):
            rules.revealSpace(UserInterface.getCords())
            return True

        def userQuit(rules):
            return False

        def checkGameState(rules):
            rules.checkGameState()
            if rules.getWin():
                UserInterface.gameWin()
                return False
            if rules.getLose():
                UserInterface.gameLose()
                return False
            return True

        def gameWin():
            print("you win!")

        def gameLose():
            print("you lose!")

        def help():#should print out an explanation of the rules and how to play
            pass
