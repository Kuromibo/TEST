import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))

pygame.display.set_caption('PONG GAME')

class Ball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_x = 10
        self.vel_y = 10

class Paddle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10 

#main loop
ball = Ball(390, 290, 10, 10)
PaddleA = Paddle(10, 270, 10, 60)
PaddleB = Paddle(780, 270, 10, 60)
game = True
while game is True:
    match = True
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and PaddleA.y > 0:
        PaddleA.y -= PaddleA.vel
    elif keys[pygame.K_s] and PaddleA.y < 600 - PaddleA.height:
        PaddleA.y += PaddleA.vel
    
    if keys[pygame.K_UP] and PaddleB.y > 0:
        PaddleB.y -= PaddleB.vel
    elif keys[pygame.K_DOWN] and PaddleB.y < 600 - PaddleA.height:
        PaddleB.y += PaddleB.vel

    if match == True:
        ball.y = ball.y - ball.vel_y
        ball.x = ball.x + ball.vel_x
        if ball.y <= 0:
            ball.vel_y * -1

    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,255), (ball.x, ball.y, ball.width, ball.height)) 
    pygame.draw.rect(win, (255,255,255), (PaddleA.x, PaddleA.y, PaddleA.width, PaddleA.height))
    pygame.draw.rect(win, (255,255,255), (PaddleB.x, PaddleB.y, PaddleB.width, PaddleB.height))
    pygame.display.update()

pygame.quit()
