import random
from game.Space import *

class Board:
    revealedSpaces = 0
    def __init__(self, size, numMines):
        #set variables
        self.size = size
        self.numMines = numMines
        self.blankSpaces = (size * size) - numMines
        #create Grid
        self.grid = [[Space() for i in range(size)] for j in range(size)]

    def addMine(self, numMines): #add a number of mines to the board randomly
        for x in range(numMines):
            isMine = True
            while isMine:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if self.grid[x][y] != "X":
                    self.grid[x][y] = "X"
                    isMine = False

    def addFlag(self,cords):#adds a flag to the users board
        self.grid[cords[0]][cords[1]] = 'F'
    def firstClick(self,rBoard,cords): #does the same thing as click but if the user
        pass                    #clicks a mine that mine is moved before processing

    def click(self,rBoard,cords):#updates the board via a refrence board following game rules
        pass

    def checkSurroundingSquares(self,rBoard,cords):#Returns the number of mines around cords
        pass

    def shuffleMine(self,cord):#moves a mine at cord to another space not containing a mine
        pass



    def toString(self):
        toReturn = []
        for i in range(self.size):
            toReturn.append("\n")
            for j in range(self.size):
                toReturn.append(self.grid[i][j].toString())
        return ''.join([toReturn[x] for x in range(len(toReturn))])
