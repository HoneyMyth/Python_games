import pygame

pygame.init()

display_width,display_height =  pygame.display.get_desktop_sizes()[0]
print(display_height,display_height)
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Test_rectangles")

rectangle_1 = pygame.FRect(500,300,200,100)
surface_1 = pygame.Surface(rectangle_1.size)

rectangle_2 = pygame.FRect(25,50,40,40)
surface_2 = pygame.Surface(rectangle_2.size)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    display.fill("gray")
    surface_1.fill("red")
    surface_2.fill("purple")
    

    
    rectangle_1.left += .1
    rectangle_2.left += .2
    surface_1.blit(surface_2, rectangle_2) 
    display.blit(surface_1, rectangle_1)

    pygame.display.update()

    pygame.display.update()