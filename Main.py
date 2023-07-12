
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920,1080))

pygame.display.set_caption('The chosen one')

clock = pygame.time.Clock( )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    draw_bg()

    #Chỉ số máu ng chơi
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    
    pygame.display.update()
    
    clock.tick(60)

    #Chào Long
    