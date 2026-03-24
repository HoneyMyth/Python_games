from os.path import join
import pygame
import random


pygame.init()

w, h = pygame.display.get_desktop_sizes()[0]
w = 3*w/4
h = 3*h/4

display_surface = pygame.display.set_mode((w, h)) 
pygame.display.set_caption("Star Duels")

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,width,height):
        super().__init__(groups)
        self.image = pygame.image.load(join("..","space_shooter" , "images" , "player.png" )).convert_alpha()
        self.rect = self.image.get_frect(center = (width/2,height/2))
        self.player_speed_multiplier = 1

        self.can_shoot = True
        self.shoot_time = 0
        self.cool_down = 500
        

    def movement(self, dt ):
        keys = pygame.key.get_pressed()

        player_direction = pygame.math.Vector2(0,0)

        player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        if player_direction.magnitude() > 1:
            player_direction = player_direction/player_direction.magnitude()

        self.rect.center += player_direction * self.player_speed_multiplier * dt
    
    def cooldown_check(self):
        if self.can_shoot == False:
            current_time = pygame.time.get_ticks()
            if self.cool_down <= current_time - self.shoot_time:
                self.can_shoot = True
    
    def laser_fire(self):
        keys_just_pressed = pygame.key.get_just_pressed()

        if int(keys_just_pressed[pygame.K_SPACE]) and self.can_shoot:
            print("Fire Laser")
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

class Stars(pygame.sprite.Sprite):
    def __init__(self,groups,width,height):
        super().__init__(groups)
        self.image = pygame.image.load(join(".." , "space_shooter" , "images" , "star.png")).convert_alpha()

        random_w = random.randint(0,round(w))
        random_h = random.randint(0,round(h))
        self.rect = self.image.get_frect(center = (random_w,random_h))

class Laser(pygame.sprite.Sprite):
    def __init__(self,groups,image,rect):
        super().__init__(groups)
        self.image = pygame.image.load(join("..", "space_shooter" , "images" , "laser.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (-100,-100))
        self.laser_speed_multiplier = 1
        self.switch = 0
    
    def shoot(self,player_sprite,dt):
        laser_direction = pygame.math.Vector2(0,0)
        pressed = pygame.key.get_just_pressed()
        
        if pressed[pygame.K_SPACE] and self.rect.y <= 0:
            self.switch = 1
            self.rect.center = player_sprite.rect.center

        if self.switch == 1:
            laser_direction.y = -1
            if self.rect.y <= 0:
                self.switch = 0
                self.rect.center = (-100,-100)

        self.rect.center += laser_direction * dt * self.laser_speed_multiplier

############
path_meteor = join(".." , "space_shooter" , "images" , "meteor.png")
meteor_surface = pygame.image.load(path_meteor).convert_alpha()
meteor_frect = meteor_surface.get_frect(center =  (w/2,h/2))
image = pygame.image.load(join("..", "space_shooter" , "images" , "laser.png")).convert_alpha()
rect = image.get_frect(center = (-100,-100))
############

all_sprites = pygame.sprite.Group()
for i in range(21):
    Stars(all_sprites,w,h)
laser = Laser(all_sprites,image,rect)
player = Player(all_sprites,w,h)

clock = pygame.time.Clock()
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)


while True:

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == meteor_event:
        #     print("Meteor just fell")

    #Fps
    dt = clock.tick(60)

    if dt >= 100:
        dt = 100

    #Logic
    player.movement(dt)
    player.laser_fire()
    player.cooldown_check()

    laser.shoot(player,dt)

    #Display
    display_surface.fill("darkgray")
    all_sprites.draw(display_surface)

    pygame.display.update()    