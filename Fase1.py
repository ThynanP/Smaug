__author__ = 'Professor'
import pygame
from pygame.locals import *
import math
from math import *
from Player import *
from Sprites import *



pygame.init()

screen = pygame.display.set_mode((800, 600))

enemyx = 420
enemyy = 250
velenemyx = 1
velenemyy = 1
enemyRun = 0
red = 0
green = 255
red_Enemy = 0
green_Enemy = 255
V_hp = 100
enemy_hp = 50
End = "Game Over"
Game = True
numTiro = 0

def ControlePlayer():
    global lado
    global numTiro
    global screen
    for i in pygame.event.get():
        if i.type==QUIT:
            exit()
        if i.type==KEYDOWN:
            if i.key==K_RIGHT:
                Player['animacao'] = 'paraDireitaAndando'
                Player['velX'] = 1
                lado = 0
            if i.key==K_LEFT:
                Player['animacao'] = 'paraEsquerdaAndando'
                Player['velX'] = -1
                lado = 1
            if i.key== K_UP and Player['ContPulo'] == 0 and lado == 0:
                Player['animacao'] = 'PuloDireita'
                Player['Pulo'] = -3
                Player['ContPulo'] = 1
            if i.key== K_UP and Player['ContPulo'] == 0 and lado == 1:
                Player['animacao'] = 'PuloEsquerda'
                Player['Pulo'] = -3
                Player['ContPulo'] = 1
            if i.key== K_SPACE:
                bala = pygame.draw.rect(screen, (255,255,255), [xTiro, Player['y'], 20, 20])
                Tiro()
                numTiro = numTiro + 1
                pygame.display.update()


        if i.type==KEYUP:
            if i.key==K_RIGHT:
                Player['animacao'] = 'paraDireitaParado'
                Player['velX'] = 0
                lado = 0
            if i.key==K_LEFT:
                Player['animacao'] = 'paraEsquerdaParado'
                Player['velX'] = 0
                lado= 1
            if i.key==K_UP:
                Player['Pulo'] = 0

def Enemey_Andando(max,min):
    global enemyx
    global enemyy
    global velenemyx
    global velenemyy
    enemyx = enemyx +velenemyx
    enemyy = enemyy +velenemyy
    if enemyx < min:
        velenemyx = 0.3
    if enemyx > max:
        velenemyx = -0.3
def Enemy_Seguindo():
    global enemyx
    global enemyy
    global velenemyx
    global velenemyy
    Player['x']
    enemyx = enemyx +velenemyx
    enemyy = enemyy +velenemyy
    if Player['x'] < enemyx:
        velenemyx = -0.3
    elif Player['x'] > enemyx:
        velenemyx = 0.3
def Dano():
    global enemy_hp
    global red_Enemy
    global green_Enemy
    if enemy_hp !=0:
        red_Enemy = red_Enemy  + 2
        green_Enemy = green_Enemy - 2
        enemy_hp = enemy_hp - 0.45
while True:
    fonte = pygame.font.Font("arial.ttf", 20)
    Inthp = int(V_hp)
    Player['x'] = Player['x'] + Player['velX']
    Player['y'] = Player['y'] + Player['velY']
    Player['y'] = Player['y'] + Player['Pulo']
    if Game == True:
        screen.fill([0,0,0])
        playerCos = pygame.draw.rect(screen, (70,50,50), [Player['x'], Player['y'], 100, 100])
        pintarSprite( Player, screen, (Player['x'], Player['y']) )
        plataforma = pygame.draw.rect(screen, (100,100,100), [0, 500, 800, 200])
        plataforma1 = pygame.draw.rect(screen, (150,150,150), [400, 400, 800, 200])
        bloco = pygame.draw.rect(screen, (200,200,200), [400, 405, 1, 195])
        enemy = pygame.draw.rect(screen, (200,200,200), [int(enemyx), int(enemyy), 100, 150])
        HP = pygame.draw.rect(screen, (0+int(red),0+int(green),0), [100, 50, 200, 25])
        Enemy_HP = pygame.draw.rect(screen, (0+int(red_Enemy),0+int(green_Enemy),0), [enemyx, enemyy - 30, 100, 15])
        Life = fonte.render(str(Inthp), True, (255,255,255))
        Life_enemy = fonte.render(str(enemy_hp), True, (255,255,255))
        screen.blit(Life, (305,40))
        screen.blit(Life_enemy, (enemyx + 110,enemyy - 30))
        xTiro = xTiro + velxTiro
        pygame.display.update()
        distancia = enemyx - Player['x']
        math.fabs(distancia)
        if distancia < 10:
            Enemy_Seguindo()
        elif distancia > 30:
            Enemey_Andando(500,402)
        if enemy_hp < 1:
            enemyy = -500
        if playerCos.colliderect(bloco):
            Player['x'] = Player['x']-2
            Player['velX'] =0
        if playerCos.colliderect(plataforma) or playerCos.colliderect(plataforma1):
            Player['velY'] = 0
            Player['Pulo'] = 0
        else:
            Player['velY'] = 1
        if enemy.colliderect(bloco):
            enemyx = enemyx - 2
            velenemyx = 0
        if enemy.colliderect(plataforma) or enemy.colliderect(plataforma1):
            velenemyy = 0
        else:
            velenemyy = 1

    if playerCos.colliderect(enemy):
        if Inthp !=0:
            red = red  + 0.25
            green = green - 0.2
            V_hp = V_hp - 0.1
    ControlePlayer()

    if Player['velY'] == 0:
        Player['ContPulo'] = 0
    if Player['y'] < 150:
        Player['Pulo'] = 1


