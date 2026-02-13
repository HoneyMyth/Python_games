from os.path import join
import pygame
import random

pygame.init()
if pygame.get_init == False:
    print("Issue in Initialising")
    quit()

w, h = pygame.display.get_desktop_sizes()[0]

display_surface = pygame.display.set_mode((w, h)) #used to create surface of code
pygame.display.set_caption("Star Duels")
x = 0
clock = pygame.time.Clock()

############
path_player = join("..","space_shooter" , "images" , "player.png" )
player_surface = pygame.image.load(path_player).convert_alpha()
path_star = join(".." , "space_shooter" , "images" , "star.png")
player_frect = player_surface.get_frect(center = (w/2,h/2))
star_surface = pygame.image.load(path_star).convert_alpha()
path_laser = join("..", "space_shooter" , "images" , "laser.png")
laser_surface = pygame.image.load(path_laser).convert_alpha()
laser_frect = laser_surface.get_frect(center = ((w/2),(h/2) - 37.5 - 17))
############

coordinates = []
for i in range(21):
            random_w = random.randint(0,1000)
            random_h = random.randint(0,600)
            coordinates.append((random_w,random_h))


scaler_x = 1
scaler_y = 1

while True:

    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    display_surface.fill("darkgray")
    
    for i in range(21):
        for j in coordinates:
            display_surface.blit(star_surface,(j[0], j[1]))
    
    display_surface.blit(player_surface,player_frect)
    display_surface.blit(laser_surface,laser_frect)
    
    player_frect.left += scaler_x*2
    if player_frect.right>= w or player_frect.left<= 0:
        scaler_x = scaler_x*-1
        
    player_frect.top += scaler_y*2
    if player_frect.top <= 0 or player_frect.bottom >= h:
        scaler_y = scaler_y*-1


    pygame.display.update()    