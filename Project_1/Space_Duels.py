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
    def __init__(self,all_sprites,width,height):
        super().__init__(all_sprites)
        self.image = pygame.image.load(join("..","space_shooter" , "images" , "player.png" )).convert_alpha()
        self.rect = self.image.get_frect(center = (width/2,height/2))
        self.mask = pygame.mask.from_surface(self.image)
        self.all_sprites = all_sprites

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
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            laser = Laser(self.all_sprites,laser_sprites,image_laser,self.rect.midbottom)

class Stars(pygame.sprite.Sprite):
    def __init__(self,groups,width,height):
        super().__init__(groups)
        self.image = pygame.image.load(join(".." , "space_shooter" , "images" , "star.png")).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        random_w = random.randint(0,round(w))
        random_h = random.randint(0,round(h))
        self.rect = self.image.get_frect(center = (random_w,random_h))

class Laser(pygame.sprite.Sprite):
    def __init__(self,all_sprites,laser_sprites,image,pos):
        super().__init__(all_sprites,laser_sprites)
        self.image = image
        self.rect = self.image.get_frect(midbottom = pos)
        self.pos = pos
        self.laser_speed_multiplier = 1
    
    def update(self,dt):
        self.rect.y -= self.laser_speed_multiplier*dt
        if self.rect.y <= -100:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self,all_sprites,meteor_sprites,image,w,h):
        super().__init__(all_sprites,meteor_sprites)
        self.image = image
        self.rect = image.get_frect(center = (random.randint(0,round(w)),0))
        self.mask = pygame.mask.from_surface(self.image)
        self.meteor_speed = .25
        self.direction = pygame.Vector2(random.uniform(-.5,.5),1)

    def update(self,dt):
        self.rect.center += self.direction * dt * self.meteor_speed
        if self.rect.top > h:
            self.kill()
        


############
meteor_surface = pygame.image.load(join(".." , "space_shooter" , "images" , "meteor.png")).convert_alpha()
image_laser = pygame.image.load(join("..", "space_shooter" , "images" , "laser.png")).convert_alpha()
############

meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
for i in range(21):
    Stars(all_sprites,w,h)
player = Player(all_sprites,w,h)
clock = pygame.time.Clock()

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,750)


points = 0
while True:

    #Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == meteor_event:
            meteor = Meteor(all_sprites,meteor_sprites,meteor_surface,w,h)


    #Fps
    dt = clock.tick(60)
    if dt >= 100:
        dt = 100

    #Logic
    player.movement(dt)
    player.laser_fire()
    player.cooldown_check()
    all_sprites.update(dt)

    for laser in laser_sprites:
        if pygame.sprite.spritecollide(laser,meteor_sprites,True,pygame.sprite.collide_mask):
            laser.kill()
            points += 1
    
    for meteors in meteor_sprites:
        if pygame.sprite.spritecollide(player,meteor_sprites,True,pygame.sprite.collide_mask):
            pygame.time.wait(1000)
            print(points)
            exit()

    
    #Display
    display_surface.fill("darkgray")
    all_sprites.draw(display_surface)

    pygame.display.update()    