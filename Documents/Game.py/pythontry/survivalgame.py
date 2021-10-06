import pygame
pygame.init()

window = pygame.display.set_mode((800,480))

pygame.display.set_caption('first game')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class charac(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.vel_x = 10
        self.vel_y = 10
        self.jump = False
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, window):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.left:
            window.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x,self.y))

def redrawGameWindow():
    window.blit(bg, (0,0))
    character.draw(window)
    pygame.display.update()

#MAIN LOOP
character = charac(300, 410, 64, 64)
run = True
while run:
    clock.tick(27)
    
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character.x > character.vel:
        character.x -= character.vel
        character.left = True
        character.right = False
    elif keys[pygame.K_RIGHT] and character.x < 500 - character.width - character.vel:
        character.x += character.vel
        character.right = True
        character.left = False
    else:
        character.right = False
        character.left = False
        character.walkCount = 0

    if keys[pygame.K_SPACE]:
        character.jump = True
        character.right = False
        character.left = False
        character.walkCount = 0

    if character.jump == True:
        character.y -= character.vel_y * 4
        character.vel_y -= 1
        if character.vel_y < -10:
            character.jump = False
            character.vel_y = 10

    redrawGameWindow()

pygame.quit()