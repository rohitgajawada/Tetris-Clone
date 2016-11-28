#configuration
rows = 30
columns = 32
cellsize = 25

allblocks = []
allblocks.insert(0, [[1, 1], [1, 1]] )
allblocks.insert(1, [[1, 1, 1, 1]] )
allblocks.insert(2, [[1, 1, 0], [0, 1, 1]] )
allblocks.insert(3, [[0, 1, 1], [1, 1, 0]] )
allblocks.insert(4, [[0, 1, 0], [1, 1, 1]] )
allblocks.insert(5, [[1, 1, 1], [0, 0, 1]] )

import pygame
import sys
from random import randrange
from board import *

class Block(Board):
    def drop(self):
        if self.finished == False:
            self.ycord += 1
            #print self.xcord, self.ycord
            if self.checkposition(self.board, self.block, self.xcord, self.ycord):
                self.stick()
                self.newblock()
                self.updatescore(1)
                self.checkrowfull()
                return True
        return False

    def immdrop(self):
        if self.finished == False:
            while(self.drop() == False):
                pass

    def rotateblock(self):
        if self.finished == False:
            if(self.score >= 0 and self.xcord > 0 and self.ycord > 0):
                newblock = [[ self.block[j][i] for j in range(len(self.block))] for i in range(len(self.block[0]) -1, -1, -1)]

            if self.checkposition(self.board, newblock, self.xcord, self.ycord) == False:
                self.block = newblock

    def newblock(self):
        self.block = allblocks[randrange(6)]
        #self.block = allblocks[1]
        self.xcord= int((columns / 2) - 1 - len(self.block[0]) / 2)
        self.ycord = 0
        self.nextblock = allblocks[randrange(6)]
        if self.checkposition(self.board, self.block, self.xcord, self.ycord):
            self.finished = True

    def move(self, addx):
		if self.finished == False:
		    newxcord = self.xcord + addx
		    if newxcord < 0:
		        newxcord = 0
		    elif newxcord > columns - len(self.block[0]):
		        newxcord = columns - len(self.block[0])
		    if self.checkposition(self.board, self.block, newxcord, self.ycord) == False:
		        self.xcord = newxcord
