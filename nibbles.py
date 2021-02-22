import pygame
import random



pygame.init()

#window settings
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Nibbles')

#game states
running = True
gameOver = False

#game properties
cellSize = 50
posx = (window.get_width() / 2) - cellSize
posy = (window.get_height() / 2) - cellSize
left = False
right = False
up = False
down = False
foodx = round(random.randrange(0, window.get_width() - cellSize) / cellSize) * cellSize
foody = round(random.randrange(0, window.get_height() - cellSize) / cellSize) * cellSize
currentScore = 0


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
    if left:
        posx += -cellSize
    elif right:
        posx += cellSize
    elif up:
        posy += -cellSize
    elif down:
        posy += cellSize
    
    #handles gameover conditions
    if posx >= window.get_width() or posx < 0 or posy >= window.get_height() or posy < 0:
        gameOver = True
    
    if gameOver:
        print('you died')
        break

    #handles food conditions
    if posx == foodx and posy == foody:
        print('food aquired',)
        foodx = round(random.randrange(0, window.get_width() - cellSize) / cellSize) * cellSize
        foody = round(random.randrange(0, window.get_height() - cellSize) / cellSize) * cellSize
        currentScore += 1

    window.fill((0, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (foodx, foody, cellSize, cellSize))
    pygame.draw.rect(window, (255, 0, 255), (posx, posy, cellSize, cellSize)) #draw snake
    pygame.display.update()
    pygame.time.delay(125)

pygame.quit()