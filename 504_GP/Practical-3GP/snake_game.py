import pygame as py
from random import randrange
window = 600
title_size = 50

range_ =(title_size // 2 , window-title_size // 2, title_size)
get_random_position = lambda: [randrange(*range_),randrange(*range_)]
snake = pg.rect.Rect([0,0,title_size - 2, title_size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time,time_step = 0,150
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([window]*2)
clock = pg.time.Clock()
dirs = {pg.K_UP:1,pg.K_DOWN:1,pg.K_LEFT,pg.K_RIGHT:1,}
while True:
          
