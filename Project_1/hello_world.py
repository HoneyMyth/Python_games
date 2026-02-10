from os.path import join
import pygame

pygame.init()
w, h = 1000, 600
display_surface = pygame.display.set_mode((w, h)) #used to create surface of code
pygame.display.set_caption("Star Duels")

running = True 
#used in while loop


ship = pygame.image.load("../space_shooter/images/player.png")
#ship being imported 

x = 0
path = join("..","space_shooter" , "images" , "player.png" )
ship = pygame.image.load(path).convert_alpha()



while running:

    for event in pygame.event.get():
        #pygame.event.get() returns a list of objects, the things taking place in the code 
        #event represents an item in the list
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    display_surface.fill("darkgray")
    x += .2
    display_surface.blit(ship,(x,0))
    pygame.display.update()    