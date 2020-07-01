import sys

class UserInterface:#use this to run the game in CMD

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
            while(mines < 1) or (mines > maxNumMines - 2):
                try:
                    mines = int(input("please enter the number of mines"))
                except:
                    print("Please Enter a Positve number")
            return mines

        def askForCords():
            pass

        def help():#should print out an explanation of the rules and how to play
            pass
