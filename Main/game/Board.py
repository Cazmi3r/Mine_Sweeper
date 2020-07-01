import random

class Board:
    def __init__(self, size): #creates a grid filled with 0
        #self.grid = [0 for j in range(size)]
        #self.grid = [[0 for i in range(1)] for j in range(size)]
        self.grid = [['^' for i in range(size)] for j in range(size)]
        self.size = size

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
        for row in self.grid:
            print(row)
