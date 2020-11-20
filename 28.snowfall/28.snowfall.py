# -----------------------------
# Program by Samodelkin
# -----------------------------

import pygame
import random
import sys

MAX_X = 1600
MAX_Y = 1200
MAX_SNOW = 120
SNOW_SIZE = 100

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.speed = random.randint(1, 4)
        self.speed_y = random.randint(1, 4)
        self.speed_x = random.randint(-1, 1) / 4
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" +str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed_y
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)
        self.x = self.x + self.speed_x
        if self.x >= MAX_X:
            self.x = (0 - SNOW_SIZE)
        elif self.x <= 0:
            self.x = MAX_X
        #i = random.randint(1, 3)
        #if i == 1: # move right
         #   self.x += 1
          #  if self.x > MAX_X:
           #     self.x = (0 - SNOW_SIZE)
        #elif i == 2: # move left
         #   self.x -= 1
          #  if self.x < (0 - SNOW_SIZE):
           #     self.x = MAX_X


    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))

def check_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()



#----------------MAIN--------------------
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
snowfall = []


initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    pygame.display.flip()