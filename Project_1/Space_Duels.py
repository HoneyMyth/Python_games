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
laser_frect = laser_surface.get_frect(center = (-100 , -100))
path_meteor = join(".." , "space_shooter" , "images" , "meteor.png")
meteor_surface = pygame.image.load(path_meteor).convert_alpha()
meteor_frect = meteor_surface.get_frect(center =  (w/2,h/2))
############

coordinates = []
for i in range(21):
            random_w = random.randint(0,1000)
            random_h = random.randint(0,600)
            coordinates.append((random_w,random_h))



player_direction = pygame.math.Vector2(0,0)
laser_direction = pygame.math.Vector2(0,0)
player_speed_multiplier = 1
laser_speed_multiplier = 1

temp_laser_coordinates = (-100,-100)

while True:

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Fps
    dt = clock.tick(60)

    if dt >= 100:
        dt = 100

    #Key press
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    if int(keys[pygame.K_SPACE]):
        laser_direction.y = -1
        laser_frect.center = player_frect.center

    #Logic
    if player_direction.magnitude() > 1:
        player_direction = player_direction/player_direction.magnitude()

    if laser_frect.y >= meteor_frect.top:
        print("Hit")

    player_frect.center += player_direction * player_speed_multiplier * dt
    laser_frect.center += laser_direction * laser_speed_multiplier * dt
    
    
    #Display
    display_surface.fill("darkgray")
    
    for coordinate in coordinates:
        display_surface.blit(star_surface, coordinate)
    
    display_surface.blit(laser_surface,laser_frect)
    display_surface.blit(player_surface,player_frect)
    display_surface.blit(meteor_surface,meteor_frect)
    
    
    


    


    pygame.display.update()    