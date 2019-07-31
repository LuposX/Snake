import pygame
import time


class Player:
    direction = 0
    bsize = 30

    updateCount = 0
    updateCountMax = 2
    def __init__(self, length):
        self.length = length
        self.rectPlayer = []
        self.playerColor = (100, 170, 250)
        self.rectBorder = 0
        self.bsize = 20
        self.rectPlayer.append(pygame.Rect(200, 200, self.bsize, self.bsize))
        for l in range(0, length):
            self.rectPlayer.append(pygame.Rect(-300, -300, self.bsize, self.bsize))
            self.tailExtension = 1
            self.step = 20
            self.standartstep = 20
            self.speedafterfood = 20
            self.currTime = 0

    def append(self):
        if len(self.rectPlayer) < self.length:
            for l in range(0, (self.length - int(len(self.rectPlayer))) + 1):
                self.rectPlayer.append(pygame.Rect(-300, -300, self.bsize, self.bsize))


    def update(self, resolution):
        self.append()
        # rect.left = x cordinates
        # rect.top = y cordinates
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            # check if hit border
            if self.rectPlayer[0].left >= resolution[0]:
                self.rectPlayer[0] = pygame.Rect(0,  self.rectPlayer[0].top, self.bsize, self.bsize)
            elif self.rectPlayer[0].left <= 0:
                self.rectPlayer[0] = pygame.Rect(resolution[0], self.rectPlayer[0].top, self.bsize, self.bsize)

            if self.rectPlayer[0].top >= resolution[1]:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left, 0, self.bsize, self.bsize)
            elif self.rectPlayer[0].top <= 0:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left, resolution[1], self.bsize, self.bsize)

            # rect.left = x cordinates
            # rect.top = y cordinates
            # update position
            for l in range(self.length - 1, 0, -1):
                # print("self.x[" + str(l) + "] = self.x[" + str(l - 1) + "]")
                self.rectPlayer[l] = pygame.Rect(self.rectPlayer[l - 1].left, self.rectPlayer[l - 1].top, self.bsize, self.bsize)

            # rect.left = x cordinates
            # rect.top = y cordinates
            # update head
            if self.direction == 0:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left + self.step, self.rectPlayer[0].top, self.bsize, self.bsize)
            elif self.direction == 1:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left - self.step, self.rectPlayer[0].top, self.bsize, self.bsize)
            elif self.direction == 2:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left, self.rectPlayer[0].top - self.step, self.bsize, self.bsize)
            elif self.direction == 3:
                self.rectPlayer[0] = pygame.Rect(self.rectPlayer[0].left, self.rectPlayer[0].top + self.step, self.bsize, self.bsize)

    def draw(self, _display_surf):
        self.append()
        for l in range(0, self.length):
            pygame.draw.rect(_display_surf, self.playerColor, self.rectPlayer[l], self.rectBorder)

    def moveRight(self):
        if not self.direction == 1:
            self.direction = 0

    def moveLeft(self):
        if not self.direction == 0:
            self.direction = 1

    def moveUp(self):
        if not self.direction == 3:
            self.direction = 2

    def moveDown(self):
        if not self.direction == 2:
            self.direction = 3
