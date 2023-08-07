import pygame
import random

pygame.init()
width,height = 800,600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooting Game")

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

character_size = 50
character_speed = 5
character = pygame.Rect(width // 2 - character_size // 2, height-character_size,character_size,character_size)

bullet_size = 10
bullets = []

enemy_radius = 20
enemies = []

score = 0

clock = pygame.time.Clock()

running = True
while running:
          for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                              running = False
                    if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_SPACE:
                                        bullet = pygame.Rect(character.centerx - bullet_size // 2, character.top,bullet_size,bullet_size)
                                        bullet.append(bullet)
