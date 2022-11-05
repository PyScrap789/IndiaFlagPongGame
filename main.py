import pygame, sys

pygame.init()

def ChakraLogic():
    global chakraSpeedX, chakraSpeedY

    chakraRect.x += chakraSpeedX
    chakraRect.y += chakraSpeedY

    if chakraRect.top <= 0 or chakraRect.bottom >= screenHeight:
        chakraSpeedY *= -1
    if chakraRect.left <= 0:
        chakraSpeedX *= -1
    if chakraRect.right >= screenWidth:
        chakraSpeedX *= -1

    if chakraRect.colliderect(player) or chakraRect.colliderect(opponent):
        chakraSpeedX *= -1

def PlayerLogic():
    global playerSpeed

    player.y += playerSpeed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def OpponentLogic():
    global opponentSpeed

    if opponent.top >= chakraRect.top:
        opponent.y -= opponentSpeed
    if opponent.bottom <= chakraRect.bottom:
        opponent.y += opponentSpeed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight

screenWidth = 1280
screenHeight = 720

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Bharat Pong")
clock = pygame.time.Clock()

chakra = pygame.image.load('chakra.png').convert_alpha()
scaledChakra = pygame.transform.scale(chakra, (120, 120))
chakraRect = pygame.Rect(screenWidth / 2 - 60, screenHeight / 2 - 60, 120, 120)
chakraSpeedX = 7
chakraSpeedY = 7

flag = pygame.image.load('india.png').convert_alpha()
scaledFlag = pygame.transform.scale(flag, (1280, 720))
flagRect = pygame.Rect(0, 0, 1920, 1080)

player = pygame.Rect(screenWidth - 10, screenHeight / 2 - 75, 10, 150)
playerSpeed = 0

opponent = pygame.Rect(0, screenHeight / 2 - 75, 10, 150)
opponentSpeed = 7

while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed = 7
            if event.key == pygame.K_UP:
                playerSpeed = -7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed = 0
            if event.key == pygame.K_UP:
                playerSpeed = 0

    ChakraLogic()
    PlayerLogic()
    OpponentLogic()

    screen.blit(scaledFlag, flagRect)
    pygame.draw.aaline(screen, pygame.color.Color('black'), (screenWidth / 2, 0), (screenWidth / 2, screenHeight))
    screen.blit(scaledChakra, chakraRect)
    pygame.draw.rect(screen, pygame.color.Color(0, 0, 255), player)
    pygame.draw.rect(screen, pygame.color.Color(0, 0, 255), opponent)

    pygame.display.flip()
    clock.tick(60)