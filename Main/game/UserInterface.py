import sys

class UserInterface:#use this to run the game in CMD

        def updateBoard(gBoard):#displays board to player
            gBoard.toString()

        def askForBoardSize():
            #error handling
            boardSize = 0
            while boardSize < 1:
                try:
                    boardSize = int(input("please enter the board size"))
                except:
                    print("Please Enter a Positve number")
            return boardSize

        def askForMines():
            pass

        def askForCords():
            pass

        def help():#should print out an explanation of the rules and how to play
            pass
