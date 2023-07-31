import pygame as pg
from random import randrange

window = 600
title_size = 50
range_ = (title_size // 2, window - title_size // 2, title_size)
get_random_position = lambda: [randrange(*range_), randrange(*range_)]

snake_radius = title_size // 2
snake = pg.Rect(0, 0, snake_radius * 2, snake_radius * 2)
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

time, time_step = 0, 110

foods = [pg.Rect(0, 0, snake_radius * 2, snake_radius * 2) for _ in range(3)]
for food in foods:
    food.center = get_random_position()

pg.init()  # Initialize Pygame

screen = pg.display.set_mode([window] * 2)
clock = pg.time.Clock()

font = pg.font.Font(None, 36)  # Set the font and size
text = font.render("faizan", True, (255, 0, 0))  # Render the text with red color

def draw_snake():
    for segment in segments:
        segment_rect = pg.Rect(segment[0], segment[1], snake_radius * 2, snake_radius * 2)
        pg.draw.circle(screen, 'goldenrod', segment_rect.center, snake_radius)


def draw_foods():
    for food in foods:
        food_rect = pg.Rect(food[0], food[1], snake_radius * 2, snake_radius * 2)
        pg.draw.circle(screen, 'purple', food_rect.center, snake_radius)


dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and dirs[pg.K_UP]:
                snake_dir = (0, -title_size)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
            if event.key == pg.K_DOWN and dirs[pg.K_DOWN]:
                snake_dir = (0, title_size)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
            if event.key == pg.K_LEFT and dirs[pg.K_LEFT]:
                snake_dir = (-title_size, 0)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}
            if event.key == pg.K_RIGHT and dirs[pg.K_RIGHT]:
                snake_dir = (title_size, 0)
                dirs = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

    screen.fill('wheat')

    self_eating = any(snake.colliderect(segment) for segment in segments[:-1])

    if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating:
        snake.center, snake_dir = get_random_position(), (0, 0)
        length = 1
        segments = [snake.copy()]

    for food in foods:
        if snake.colliderect(food):
            food.center = get_random_position()
            length += 1

    draw_foods()
    draw_snake()

    screen.blit(text, (window // 2 - text.get_width() // 2, window // 2 - text.get_height() // 2))  # Draw the text on the screen

    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(120)
