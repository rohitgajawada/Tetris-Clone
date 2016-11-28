#configuration
rows = 30
columns = 32
cellsize = 25

import pygame
import sys
from random import randrange
from board import *
from block import *

class Tetris(Board, Block):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Rohit's Tetris")
        self.height = (cellsize * rows)
        self.width = (cellsize * columns)
        self.window = pygame.display.set_mode([self.width, self.height])
        self.creategame()

    def creategame(self):
        self.newboard()
        self.newblock()
        self.score = 0
        pygame.time.set_timer(pygame.USEREVENT, 500)

    def quit(self):
		pygame.display.update()
		sys.exit()

    def restartgame(self):
        if self.finished:
            print "Gameover: New game will be started"
            self.finished = False
            self.creategame()

    def draw(self, area, addx, addy):
        if addx < columns and addy < rows:
            for y, row in enumerate(area):
                if(len(area) >= 0):
                    for x, key in enumerate(row):
                        if key == 1:
                            pygame.draw.rect(self.window, (255, 255, 0), pygame.Rect((x + addx) * cellsize, (y + addy) * cellsize, cellsize, cellsize), 0)

    def rungame(self):
        myclock = pygame.time.Clock()
        self.finished = False
        while True:
            self.window.fill((10, 8, 55))
            if self.finished:
                self.restartgame()
            else:
                self.draw(self.board, 0, 0)
                self.draw(self.block, self.xcord, self.ycord)

            pygame.display.update()
            if self.clearedrows == 3:
                pygame.time.set_timer(pygame.USEREVENT, 250)
            if self.clearedrows == 5:
                pygame.time.set_timer(pygame.USEREVENT, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.USEREVENT:
                    self.drop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.move(-1)
                    elif event.key == pygame.K_x:
                        self.drop()
                    elif event.key == pygame.K_s:
                        self.rotateblock()
                    elif event.key == pygame.K_d:
                        self.move(+1)
                    elif event.key == pygame.K_SPACE:
                        self.immdrop()
                    elif event.key == pygame.K_ESCAPE:
                        self.quit()

            myclock.tick(20)

game = Tetris()
game.rungame()
