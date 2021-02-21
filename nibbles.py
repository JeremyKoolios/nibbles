import pygame



pygame.init()

#window settings
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Nibbles')

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.QUIT()