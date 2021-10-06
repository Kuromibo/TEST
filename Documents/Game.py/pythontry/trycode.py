import pygame
from random import randint
pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.caption('wordgame')

gamerunning = True

class character():
    def __init__(self, name, hp, attack, profession, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.profession = profession
        self.gold = gold

class monster():
    def __init__(self, type, hp):
        self.type = type
        self.hp = hp
        

player = character('kuromi', 100, 100, 'knight', 1000)
enemy = monster('goblin', True)

#main loop
while gamerunning == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
    print ('---' * 8)
    print('please select action')
    print('1) HUNT')
    print('2) OPEN SHOP')
    print('3) EXIT GAME')

    Player_Choice = input()

    if Player_Choice == '1':
        print('you have found a goblin')
        if player.attack >= 100:
            enemy.hp = False
            if enemy.hp == False:
                print('you have slain an enemy!')
    elif Player_Choice == '2':
        print('choose an item')
        print('cloth armor')
        print('potion')
        print('short sword')
        print('long sword')
    elif Player_Choice == '3':
        gamerunning = False
    else:
        print('invalid input')

pygame.quit()