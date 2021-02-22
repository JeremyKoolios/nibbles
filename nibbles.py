import pygame
import random

pygame.init()

def writeText(msg = '', location = (0, 0), fontSize = 20):
    pygame.font.init()
    gameFont = pygame.font.SysFont('Arial', fontSize, True)
    textSurface = gameFont.render(msg, True, [0,0,255])
    window.blit(textSurface, location)

#window settings
screenWidth = 800
screenHeight = 800
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Nibbles')

#colors
colorSnake = (0, 0, 255)
colorApple = (255, 0, 0)
colorBackground = (0, 255, 127)

#game states
running = True
startScreen = True
inGame = False
gameOver = False

#game properties
cellSize = 50
growRate = 1 #controls how many cells the snake grows per apple

posx = [(screenWidth / 2) - cellSize, (screenWidth / 2) - 2 * cellSize]
posy = [(screenHeight / 2) - cellSize, (screenWidth / 2) - cellSize]

currentScore = 0

left = False
right = True
up = False
down = False

def drawSnake():
    for i in range(len(posx)):
        pygame.draw.rect(window, colorSnake, (posx[i], posy[i], cellSize, cellSize))

def growSnake():
    for i in range(growRate):
        posx.append(posx[0])
        posy.append(posy[0])

def randCoord(screenWidth, screenHeight):
    randx = round(random.randrange(0, screenWidth - cellSize) / cellSize) * cellSize
    randy = round(random.randrange(0, screenHeight - cellSize) / cellSize) * cellSize

    return randx, randy

foodx, foody = randCoord(screenWidth, screenHeight)






#infinitely loops wihle game is running
while running:
    while startScreen:
        window.fill(colorBackground)
        writeText('Nibbles', (265, 300), 100)
        writeText('Press any key to start', (278, 400), 30)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                startScreen = False
                inGame = True

            if event.type == pygame.QUIT:
                pygame.quit()
    
    while inGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            
            #handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if right:
                        break
                    else:
                        left, right, up, down = True, False, False, False
                elif event.key == pygame.K_RIGHT:
                    if left:
                        break
                    else:
                        left, right, up, down = False, True, False, False
                elif event.key == pygame.K_UP:
                    if down:
                        break
                    else:
                        left, right, up, down = False, False, True, False
                elif event.key == pygame.K_DOWN:
                    if up:
                        break
                    else:
                        left, right, up, down = False, False, False, True

        #gets stnake moving in snake-like pattern
        if left:
            posx.pop()
            posx.insert(0, posx[0] - cellSize)
            posy.pop()
            posy.insert(0, posy[0])
        elif right:
            posx.pop()
            posx.insert(0, posx[0] + cellSize)
            posy.pop()
            posy.insert(0, posy[0])
        elif up:
            posx.pop()
            posx.insert(0, posx[0])
            posy.pop()
            posy.insert(0, posy[0] - cellSize)
        elif down:
            posx.pop()
            posx.insert(0, posx[0])
            posy.pop()
            posy.insert(0, posy[0] + cellSize)
        
        #handles gameover conditions
        if posx[0] >= screenWidth or posx[0] < 0 or posy[0] >= screenHeight or posy[0] < 0:
            gameOver = True
            inGame = False
        for i in range(1, len(posx) - 1):
            if posx[0] == posx[i] and posy[0] == posy[i]:
                gameOver = True
                inGame = False

        #handles food conditions
        if posx[0] == foodx and posy[0] == foody:
            growSnake()
            currentScore += 1
            foodx, foody = randCoord(screenWidth, screenHeight)
            for i in range(len(posx) - 1): #makes sure food does not generate inside of snake
                while foodx == posx[i] and foody == posy[i]:
                    foodx, foody = randCoord(screenWidth, screenHeight)

        window.fill(colorBackground)
        pygame.draw.rect(window, colorApple, (foodx, foody, cellSize, cellSize)) #draw food
        drawSnake() #draw snake
        pygame.display.update()
        pygame.time.delay(125)

    while gameOver:
        window.fill(colorBackground)
        writeText('Game Over', (190, 200), 100)
        writeText('Your score: ' + str(currentScore), (340, 310), 25)
        writeText('press any key to restart', (295, 370), 25)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                posx = [(screenWidth / 2) - cellSize, (screenWidth / 2) - 2 * cellSize]
                posy = [(screenHeight / 2) - cellSize, (screenWidth / 2) - cellSize]
                currentScore = 0
                left = False
                right = True
                up = False
                down = False
                foodx, foody = randCoord(screenWidth, screenHeight)
                inGame = True
                gameOver = False

            if event.type == pygame.QUIT:
                pygame.quit()

pygame.quit()