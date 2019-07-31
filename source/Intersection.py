import pygame
import math

class Intersection():
    def __init__(self, headX, headY, direction, resolution):
        # nach vorne vom start aus
        self.Color1 = (210, 0, 210)
        # nach links
        self.Color2 = (250, 120, 0)
        # nach rechts
        self.Color3 = (60, 250, 60)

        self.Color4 = (160, 160, 160)
        self.Color5 = (120, 250, 0)
        self.resolution = resolution

        # matrix for collision detection and lines
        self.distance = 1
        #self.rectWidth = 1
        self.visionStart = [[headX + 20, headY + 10], [headX + 10, headY], [headX + 10, headY + 20], [headX + 20, headY + 20], [headX + 20, headY - 0]]
        self.visionEnd = [[headX + self.distance, headY + 10], [headX + 10, headY - self.distance],
                          [headX + 10, headY + self.distance], [headX + self.distance, headY + 60], [headX + self.distance, headY - 60]]

    def update(self, rectFood, headX, headY, direction, _display_surf):

        # FIXME 1. fix direction which are asilant. Problem: probaply the + 300
        # TODO: 2. if nessecarry add more direction


        # nach vorne vom start aus
        #self.visionStart[0][0], self.visionStart[0][1] = headX + 20, headY + 10
        #self.visionEnd[0][0], self.visionEnd[0][1] = headX + self.distance, headY + 10
        #rect1 = pygame.Rect(headX + 20, headY + 10, self.rectWidth, self.distance)

        # nach links
        #self.visionStart[1][0], self.visionStart[1][1] = headX + 10, headY
        #self.visionEnd[1][0], self.visionEnd[1][1] = headX + 10, headY - self.distance
        #rect2 = pygame.Rect(headX + 10, headY, self.rectWidth, self.distance)

        # nach rechts
        #self.visionStart[2][0], self.visionStart[2][1] = headX + 10, headY + 20
        #self.visionEnd[2][0], self.visionEnd[2][1] = headX + 10, headY + self.distance
        #rect3 = pygame.Rect(headX + 10,headY + 20, self.rectWidth, -self.distance)

        #change the distance
        for i in range(1, self.resolution[0], 1):
            self.distance = i

        #'''
        # direction 0 = nach rechts
        # direction 1 = nach links
        # direction 2 = nach oben
        # direction 3 = nach unten
            if direction == 0:
                # pygame.Rect(self.rectPlayer[0].left + self.step, self.rectPlayer[0].top, self.bsize,self.bsize)
                self.visionStart[0][0], self.visionStart[0][1] = headX + 20, headY + 10
                self.visionEnd[0][0], self.visionEnd[0][1] = headX + self.distance, headY + 10

                self.visionStart[1][0], self.visionStart[1][1] = headX + 10, headY - 0
                self.visionEnd[1][0], self.visionEnd[1][1] = headX + 10, headY - self.distance

                self.visionStart[2][0], self.visionStart[2][1] = headX + 10, headY + 20
                self.visionEnd[2][0], self.visionEnd[2][1] = headX + 10, headY + self.distance

                self.visionStart[3][0], self.visionStart[3][1] = headX + 20, headY + 20
                self.visionEnd[3][0], self.visionEnd[3][1] = headX + self.distance, headY + 200

                self.visionStart[4][0], self.visionStart[4][1] = headX + 20, headY - 0
                self.visionEnd[4][0], self.visionEnd[4][1] = headX + self.distance, headY - 200

            elif direction == 1:
                # pygame.Rect(self.rectPlayer[0].left - self.step, self.rectPlayer[0].top, self.bsize,self.bsize)
                self.visionStart[0][0], self.visionStart[0][1] = headX, headY + 10
                self.visionEnd[0][0], self.visionEnd[0][1] = headX - self.distance, headY + 10

                self.visionStart[1][0], self.visionStart[1][1] = headX + 10, headY + 20
                self.visionEnd[1][0], self.visionEnd[1][1] = headX + 10, headY + self.distance

                self.visionStart[2][0], self.visionStart[2][1] = headX + 10, headY + 0
                self.visionEnd[2][0], self.visionEnd[2][1] = headX + 10, headY - self.distance

                self.visionStart[3][0], self.visionStart[3][1] = headX - 0, headY + 0
                self.visionEnd[3][0], self.visionEnd[3][1] = headX - self.distance, headY - 200

                self.visionStart[4][0], self.visionStart[4][1] = headX - 0, headY + 20
                self.visionEnd[4][0], self.visionEnd[4][1] = headX - self.distance, headY + 200

            elif direction == 2:
                # pygame.Rect(self.rectPlayer[0].left, self.rectPlayer[0].top - self.step, self.bsize,self.bsize)
                self.visionStart[0][0], self.visionStart[0][1] = headX + 10, headY
                self.visionEnd[0][0], self.visionEnd[0][1] = headX + 10, headY - self.distance

                self.visionStart[1][0], self.visionStart[1][1] = headX, headY + 10
                self.visionEnd[1][0], self.visionEnd[1][1] = headX - self.distance, headY + 10

                self.visionStart[2][0], self.visionStart[2][1] = headX + 20, headY + 10
                self.visionEnd[2][0], self.visionEnd[2][1] = headX + self.distance, headY + 10

                self.visionStart[3][0], self.visionStart[3][1] = headX + 20, headY + 0
                self.visionEnd[3][0], self.visionEnd[3][1] = headX + 200, headY - self.distance

                self.visionStart[4][0], self.visionStart[4][1] = headX + 0, headY + 0
                self.visionEnd[4][0], self.visionEnd[4][1] = headX - 200, headY - self.distance

            elif direction == 3:
                # pygame.Rect(self.rectPlayer[0].left, self.rectPlayer[0].top + self.step, self.bsize,self.bsize)
                self.visionStart[0][0], self.visionStart[0][1] = headX + 10, headY + 20
                self.visionEnd[0][0], self.visionEnd[0][1] = headX + 10, headY + self.distance

                self.visionStart[1][0], self.visionStart[1][1] = headX + 20, headY + 10
                self.visionEnd[1][0], self.visionEnd[1][1] = headX + self.distance, headY + 10

                self.visionStart[2][0], self.visionStart[2][1] = headX, headY + 10
                self.visionEnd[2][0], self.visionEnd[2][1] = headX - self.distance, headY + 10

                self.visionStart[3][0], self.visionStart[3][1] = headX + 20, headY + 20
                self.visionEnd[3][0], self.visionEnd[3][1] = headX + 200, headY + self.distance

                self.visionStart[4][0], self.visionStart[4][1] = headX + 0, headY + 20
                self.visionEnd[4][0], self.visionEnd[4][1] = headX - 200, headY + self.distance


        #'''
            for i2 in range(0, len(self.visionEnd)):
                #print("i: ", str(i2))
                #print("x, y:", str(self.visionEnd[i2][0]), str(self.visionEnd[i2][1]))
                #print("food: ", str(rectFood))
                #print(" ")
                if rectFood.collidepoint(self.visionEnd[i2][0], self.visionEnd[i2][1]):
                    #print(str(i2))
                    #dist = math.sqrt((x1-x2)**2 + (y1-y2)**2))
                    #dist = math.sqrt((self.visionEnd[i2][0] - self.visionStart[i2][0]) ** 2 + (self.visionEnd[i2][1] - self.visionStart[i2][1]) ** 2)
                    dist = round(math.hypot(self.visionEnd[i2][0] - self.visionStart[i2][0], self.visionEnd[i2][1] - self.visionStart[i2][1]))
                    print("distance " + str(i2) + ": " + str(dist))

    def draw(self, _display_surf):
        #pygame.draw.rect(_display_surf, self.Color1, rect1)
        #pygame.draw.rect(_display_surf, self.Color2, rect2)
        #pygame.draw.rect(_display_surf, self.Color3, rect3)
        pygame.draw.line(_display_surf, self.Color1, (self.visionStart[0][0], self.visionStart[0][1]), (self.visionEnd[0][0], self.visionEnd[0][1]), 5)
        pygame.draw.line(_display_surf, self.Color2, (self.visionStart[1][0], self.visionStart[1][1]), (self.visionEnd[1][0], self.visionEnd[1][1]), 5)
        pygame.draw.line(_display_surf, self.Color3, (self.visionStart[2][0], self.visionStart[2][1]), (self.visionEnd[2][0], self.visionEnd[2][1]), 5)
        pygame.draw.line(_display_surf, self.Color4, (self.visionStart[3][0], self.visionStart[3][1]), (self.visionEnd[3][0], self.visionEnd[3][1]), 5)
        pygame.draw.line(_display_surf, self.Color5, (self.visionStart[4][0], self.visionStart[4][1]), (self.visionEnd[4][0], self.visionEnd[4][1]), 5)


