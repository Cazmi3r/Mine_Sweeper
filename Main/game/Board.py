class Board:
    def __init__(self, size): #creates a grid filled with 0
        self.grid = [[0 for i in range(1)] for j in range(size)]

    def addMine(self): #add a number of mines to the board randomly
        pass

    def addFlag(self,cords):#adds a flag to the users board
        pass

    def firstClick(self,rBoard,cords): #does the same thing as click but if the user
        pass                    #clicks a mine that mine is moved before processing

    def click(self,rBoard,cords):#updates the board via a refrence board following game rules
        pass

    def checkSurroundingSquares(self,rBoard,cords)#Returns the number of mines around cords
        pass


    def toString(self):
        for r in self.grid:
            for c in self.grid:
                print(c, end = " ")
            print()
