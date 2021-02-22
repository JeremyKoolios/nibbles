import pygame
import random



pygame.init()

#window settings
screenWidth = 800
screenHeight = 800
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Nibbles')

#game states
running = True
gameOver = False

#game properties
cellSize = 50
posx = (screenWidth / 2) - cellSize
posy = (screenHeight / 2) - cellSize
left = False
right = False
up = False
down = False

def randCoord(screenWidth, screenHeight):
    randx = round(random.randrange(0, screenWidth - cellSize) / cellSize) * cellSize
    randy = round(random.randrange(0, screenHeight - cellSize) / cellSize) * cellSize

    return randx, randy

foodx, foody = randCoord(screenWidth, screenHeight)

currentScore = 0
snakeLength = 1


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
    if posx >= screenWidth or posx < 0 or posy >= screenHeight or posy < 0:
        gameOver = True
    
    if gameOver:
        print('you died')
        break

    #handles food conditions
    if posx == foodx and posy == foody:
        snakeLength += 1
        currentScore += 1
        print('current score:', currentScore)
        foodx, foody = randCoord(screenWidth, screenHeight)

    window.fill((0, 255, 127))
    pygame.draw.rect(window, (255, 0, 0), (foodx, foody, cellSize, cellSize)) #draw food
    pygame.draw.rect(window, (0, 0, 255), (posx, posy, cellSize, cellSize)) #draw snake
    pygame.display.update()
    pygame.time.delay(125)

pygame.quit()