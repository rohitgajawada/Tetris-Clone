#configuration
rows = 30
columns = 32
cellsize = 25

import pygame
import sys
from random import randrange

class Board():
    def deleterow(self, row):
        # print "inside deleterow"
        del self.board[row]
        newrow = [0 for i in xrange(columns)]
        self.board.insert(0, newrow)

    def checkrowfull(self):
        for i, row in enumerate(self.board):
            if 0 not in row:
                self.deleterow(i)
                self.clearedrows += 1
                self.updatescore(2)

    def updatescore(self, val):
        if val == 1:
            self.score += 10
        elif val == 2:
            self.score += 100
        print "Score is: ", self.score

    def newboard(self):
        self.score = 0
        self.clearedrows = 0
        self.board = [[0 for i in xrange(columns)] for j in xrange(rows)]

    def stick(self):
        # print "-----"
        for y, row in enumerate(self.block):
            for x, ind in enumerate(row):
                self.board[self.ycord + y - 1][self.xcord + x] += ind

    def checkposition(self, board, myblock, addx, addy):
        for y, row in enumerate(myblock):
            for x, item in enumerate(row):
                if (y + addy) >= rows or (x + addx) >= columns:
                    return True
                elif item > 0 and board[y + addy][x + addx] > 0:
                    return True
        return False
