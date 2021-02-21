import pygame



pygame.init()

#window settings
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Nibbles')

running = True

posx = 350
posy = 350
left = False
right = False
up = False
down = False

#infinitely loops wihle game is running
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left, right, up, down = True, False, False, False
            elif event.key == pygame.K_RIGHT:
                left, right, up, down = False, True, False, False
            elif event.key == pygame.K_UP:
                left, right, up, down = False, False, True, False
            elif event.key == pygame.K_DOWN:
                left, right, up, down = False, False, False, True
    if left == True:
        posx += -50
    elif right == True:
        posx += 50
    elif up == True:
        posy += -50
    elif down == True:
        posy += 50
    
    window.fill((0, 255, 255))
    pygame.draw.rect(window, (255, 0, 255), (posx, posy, 50, 50))
    pygame.display.update()
    pygame.time.delay(125)


pygame.quit()