class Space():
    def __init__(self):
            self.mine = False
            self.flag = False
            self.numOfSurroundingMines = 0
            self.revealed = False

    def getRevealed(self):
        return self.revealed

    def setRevealed(self):
        self.revealed = True

    def getMine(self):
        return self.mine

    def setMine(self):#toggles if a mine is located here
        if self.mine:
            self.mine = False
        else:
            self.mine = True

    def getFlag(self):
        return self.flag

    def setFlag(self):#toggles if a flag is located here returns true if it worked
        if self.revealed == False:#game shouldn't let you put flags on revealed spaces
            if self.flag:
                self.flag = False
                return True
            else:
                self.flag = True
                return True
        return False #if the code gets here the usser tried to flag a revealed space

    def setNumOfSurroundingMines(self, numOfMines):
        self.numOfSurroundingMines = numOfMines

    def getNumOfSurroundingMines(self):
        return self.numOfSurroundingMines

    def toString(self):
        toReturn =["[",
        "M:",str(self.mine),"|",
        "F:", str(self.flag), "|",
        "numM:", str(self.numOfSurroundingMines), "|",
        "R:", str(self.revealed),
        "]"]
        return ''.join([toReturn[x] for x in range(len(toReturn))])
