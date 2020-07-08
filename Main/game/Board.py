import random
from game.Space import *

class Board:
    def __init__(self, size, numMines):
        #set variables
        self.size = size
        self.numMines = numMines
        self.blankSpaces = (size * size) - numMines
        self.revealedSpaces = 0
        #create Grid
        self.grid = [[Space() for i in range(size)] for j in range(size)]
        #add mines to Board
        self.addMine(numMines)
        #calculate num of surrounding mines for all spaces
        for i in range(size):
            for j in range(size):
                targetSpace = [i, j]
                self.setNumOfSurroundingMines(targetSpace)

    def addMine(self, numMines): #add a number of mines to the board randomly
        for x in range(numMines):
            isMine = True
            while isMine:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if self.grid[x][y].getMine() == False :
                    self.grid[x][y].setMine()
                    isMine = False

    def addFlag(self,cords):#adds a flag to the users board
        self.grid[cords[0]][cords[1]].setFlag()
    def firstClick(self,rBoard,cords): #does the same thing as click but if the user
        pass                    #clicks a mine that mine is moved before processing

    def revealSpace(self,cords):#updates the board via a refrence board following game rules
        self.grid[cords[0]][cords[1]].setRevealed()

    def getSize(self):
        return self.size

    def setNumOfSurroundingMines(self,cords):
            listOfSpaces = self.getSurroundingSpaces(cords)
            numOfMines = 0
            targetSpace = self.getSpace(cords)
            #check each space in the list
            for space in listOfSpaces:
                #if there is a mine there add it to the num of mines
                if space.getMine():
                    numOfMines = numOfMines + 1
            targetSpace.setNumOfSurroundingMines(numOfMines)


    def getSurroundingSpaces(self,cords):#Returns a list of all surrounding Spaces
        listSpaces = []
        targetSpace = self.getSpace(cords)
        spaceToLookAt = [0, 0]

        #this will search a 3x3 grid centered on but excludes the target space
        for i in range(-1, 3):
            spaceToLookAt[0] = cords[0] + i
            for j in range(-1, 3):
                spaceToLookAt[1] = cords[1] + j
                #confirms that were not looking at the target space
                if i != 0 and j !=0:
                    #confirms x is in bounds
                    if spaceToLookAt[0] >= 0 and spaceToLookAt[0] < self.size:
                        #confirms y is in bounds
                        if spaceToLookAt[1] >= 0 and spaceToLookAt[1] < self.size:
                            #adds the space were looking at to the list to return
                            listSpaces.append(self.getSpace(spaceToLookAt))
        return listSpaces

    def shuffleMine(self,cord):#moves a mine at cord to another space not containing a mine
        pass
    def getSpace(self,cord):#return a space object at a cord
        return self.grid[cord[0]][cord[1]]



    def toString(self):
        toReturn = []
        for i in range(self.size):
            toReturn.append("\n")
            for j in range(self.size):
                toReturn.append(self.grid[i][j].toString())
        return ''.join([toReturn[x] for x in range(len(toReturn))])
