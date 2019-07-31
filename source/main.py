import pygame
import time
import random
from _thread import start_new_thread
from pygame.locals import *
from pygame_snake import Food
from pygame_snake import Player
from pygame_snake import Intersection

class game:
    def __init__(self):
        self.resolution = (800, 500)
        self._running = True
        self._display_surf = None
        self.startLength = 4

        # init of classes
        self.player = Player.Player(self.startLength)
        self.food = Food.Food(self.resolution)
        self.intersection = Intersection.Intersection(self.player.rectPlayer[0].left, self.player.rectPlayer[0].top, self.player.direction, self.resolution)

        self.initTime = time.time()
        self.updateCount = 0
        self.updateCountMax = 2
        self.clock = pygame.time.Clock()
        self.maxTailExtensions = 4
        self.forVariable = self.startLength
        self.tempRectPlayer = []
        self.tempFor = False

    def on_init(self):
        pygame.init()
        self.fontPoints = pygame.font.Font(None, 25)
        self._display_surf = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Snake!")
        self._running = True

    def iscollision2(self, Food_X, Food_Y, Player_X, Player_Y, player_bsize, food_bsize):
        for i in range(0, len(Player_X)):
            if Food_X >= Player_X[i] and Food_X <= Player_X[i] + player_bsize:
                if Food_Y >= Player_Y[i] and Food_Y <= Player_Y[i] + player_bsize:
                    return True
                else:
                    return False
            else:
                return False

    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

    def on_cleanup(self):
        pygame.quit()

    def render(self, _display_surf):
        _display_surf.fill((0, 0, 0))
        self.player.draw(_display_surf)
        self.food.draw(_display_surf)

        # point score
        self.pointscoreTemp = self.fontPoints.render("Points: " + str(self.food.points), True, pygame.Color('green'))
        _display_surf.blit(self.pointscoreTemp, (10, 10))

        # speed
        self.speedTemp = self.fontPoints.render("Speed: " + str(self.player.step), True, pygame.Color('green'))
        _display_surf.blit(self.speedTemp, (10, 30))

        # alive
        self.aliveTemp = self.fontPoints.render("Alive: " + str(round(time.time() - self.initTime)) + "s", True, pygame.Color('green'))
        _display_surf.blit(self.aliveTemp, (10, 50))

        # draws fps counter
        self.fps = self.fontPoints.render("Fps: " + str(int(self.clock.get_fps())), True, pygame.Color('green'))
        _display_surf.blit(self.fps, (10, 70))

        # fittnes average point score
        if (round(time.time() - self.initTime)) != 0:
            self.temp3 = self.food.points / (round(time.time() - self.initTime))
        else:
            self.temp3 = 0
        self.fps = self.fontPoints.render("Fittness: " + str(round(self.temp3, 3)), True, pygame.Color('green'))
        _display_surf.blit(self.fps, (10, 90))

        self.intersection.draw(_display_surf)
        pygame.display.flip()

    @staticmethod
    def changeSpeed(self):
        print("---------------------New thread---------------------")

        while (((int(round(time.time() * 1000)) - self.player.currTime) <= 1500)):
            self.player.step = self.player.speedafterfood
        self.player.step = self.player.standartstep  # sets speed back


    def loop(self):
        #if int(self.clock.get_fps()) <= 8:
            #print("under 8fps")

        self.player.append()
        self.player.update(self.resolution)
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            for i in range(0, len(self.player.rectPlayer)):
                if self.food.rectFood.colliderect(self.player.rectPlayer[i]):
                    self.food.points = self.food.points + 1
                    self.food.x = random.randint(50, (self.resolution[0] - 50))
                    self.food.y = random.randint(50, (self.resolution[1] - 50))
                    self.rectFood = pygame.Rect(self.food.x, self.food.y, 20, 20)

                    for i2 in range(0, len(self.player.rectPlayer)):
                         if self.rectFood.colliderect(self.player.rectPlayer[i]):
                            self.food.x = random.randint(50, (self.resolution[0] - 50))
                            self.food.y = random.randint(50, (self.resolution[1] - 50))
                            self.rectFood = pygame.Rect(self.food.x, self.food.y, 20, 20)

                    self.player.length = self.player.length + self.player.tailExtension
                    self.player.currTime = time.time()
                    self.player.currTime = int(round(time.time() * 1000))
                    if self.player.tailExtension <= self.maxTailExtensions:
                        self.player.tailExtension += 1
                        self.forVariable += 2
                        if len(self.player.rectPlayer) - 1 < self.forVariable:
                            self.forVariable = self.forVariable -1
                        else:
                            self.forVariable += 1

        self.player.append()
        self.intersection.update(self.food.rectFood, self.player.rectPlayer[0].left, self.player.rectPlayer[0].top, self.player.direction, self._display_surf)

        for i in range(self.startLength, len(self.player.rectPlayer), 1):
            try:
                if self.player.rectPlayer[0].colliderect(self.player.rectPlayer[i]):
                    self.food.points = 0
                    self.initTime = time.time()
                    self.player.tailExtension = 0
                    self.player.length = self.startLength

                    # save our rect player in temp
                    for l1 in range(0, self.startLength):
                        self.tempRectPlayer.append(self.player.rectPlayer[l1])

                    # deletes our rect player list
                    self.player.rectPlayer[:] = []

                    # resets our tail on start length size
                    for l2 in range(0, self.startLength):
                        self.player.rectPlayer.append(self.tempRectPlayer[l2])

                    # deletes our rect player list temp
                    self.tempRectPlayer[:] = []
                    print("game over")
                    break
            except:
               print("An exception has occured")
        self.tempFor = True


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

                # keys = lambda tempEvent: True if event.type == pygame.KEYDOWN else False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()

                    elif event.key == pygame.K_LEFT:
                        self.player.moveLeft()

                    elif event.key == pygame.K_UP:
                        self.player.moveUp()

                    elif event.key == pygame.K_DOWN:
                        self.player.moveDown()

            self.loop()
            self.render(self._display_surf)
            self.clock.tick(12)
        self.on_cleanup()


if __name__ == "__main__":
    thegame = game()
    thegame.execute()
