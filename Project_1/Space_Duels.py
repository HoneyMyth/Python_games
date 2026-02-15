from os.path import join
import pygame
import random

pygame.init()
if pygame.get_init == False:
    print("Issue in Initialising")
    quit()

w, h = pygame.display.get_desktop_sizes()[0]
w = 3*w/4
h = 3*h/4

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



player_direction = pygame.math.Vector2(0,0)
player_speed = 1

while True:

    dt = clock.tick(60)

    if dt>= 100:
        dt = 100

    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_LEFT]) - int(keys[pygame.K_RIGHT])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            print("keydown")
    
    display_surface.fill("darkgray")
    
    for coordinate in coordinates:
        display_surface.blit(star_surface, coordinate)
    
    display_surface.blit(player_surface,player_frect)
    display_surface.blit(laser_surface,laser_frect)
    
    player_frect.center += player_direction * player_speed * dt
    

    #Bouncing of ship
    if player_frect.right>=w or player_frect.left<=0:
        player_direction.x *= -1

    if player_frect.top<=0 or player_frect.bottom>=h:
        player_direction.y *= -1

    
    

    pygame.display.update()    