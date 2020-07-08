from game.Board import *

class Rules:
    def __init__(self, boardSize, numMines):
        self.board = Board(boardSize, numMines)
        self.numMines = numMines
        self.boardSize = boardSize
        self.win = False
        self.lose = False

    def getWin(self):
        return self.win

    def getLose(self):
        return self.lose

    def getBoard(self):
        return self.board

    def checkGameState(self):#checks to see if the player has won or lost
        #Check to see if all blank spaces have been revealed
        if self.board.getRevealedSpaces() == self.board.getBlankSpaces():
            self.win = True
            return
        #check to see if any mines have been revealed
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                cords = [i, j]
                targetSpace = self.board.getSpace(cords)
                if targetSpace.getRevealed() and targetSpace.getMine():
                    self.lose = True
                    return

    def checkForWin(self):
        pass

    def checkForLoss(self):
        pass

    def quit(self):
        pass

    def addFlag(self, cords):
        self.board.addFlag(cords)

    def revealSpace(self, cords):
        self.board.revealSpace(cords)
