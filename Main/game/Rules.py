from game.Board import *

class Rules:
    def __init__(self, boardSize, numMines):
        self.board = Board(boardSize, numMines)
        self.numMines = numMines
        self.boardSize = boardSize
        self.win = False
        self.lose = False
    def getBoard(self):
        return self.board

    def checkGameState(self):#checks to see if the player has won or lost
        pass

    def checkForWin(self):
        pass

    def checkForLoss(self):
        pass

    def quit(self):
        pass
    def addFlag(self, cords):
        self.board.addFlag(cords)
