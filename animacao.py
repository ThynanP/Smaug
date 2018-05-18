__author__ = 'Thynan'

import pygame
from pygame.time import Clock
from pygame.locals import QUIT, Rect, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYUP, FULLSCREEN
from pygame.constants import KEYDOWN
from math import trunc
pygame.init()
screen1 = pygame.display.set_mode( (1360, 768), FULLSCREEN, 32)
cenario = pygame.image.load("./cen.jpg").convert_alpha()
clk = Clock()

def pintarSprite(sprite, surface, pos):
    nomeDaLista = sprite['animacao']
    listaAnimacao = sprite[nomeDaLista]
    sprite['frameDelay'] += 1
    if sprite['frameDelay'] > sprite['frameDelayMax']:
        sprite['frameDelay'] = 0
        sprite['frameListaIndice'] += 1
    if sprite['frameListaIndice'] >= len(listaAnimacao):
        sprite['frameListaIndice'] = 0


    frameIndice = listaAnimacao[ sprite['frameListaIndice'] ]
    lin = trunc(frameIndice / sprite['spriteSheetColumns'])
    col = frameIndice % sprite['spriteSheetColumns']
    y = lin * sprite['spriteSheetHeight']
    x = col * sprite['spriteSheetWidth']
    frame = sprite['spriteSheet'].subsurface(

   Rect( (x, y),
              (sprite['spriteSheetWidth'], sprite['spriteSheetHeight']) ))
    surface.blit( frame, pos )

Warrior = {
    'x' : 25,
    'y' : 264,
    'velX' : 0,
    'velY' : 0,
    'spriteSheet' : pygame.image.load("./sprite.png").convert_alpha(),
    'spriteSheetColumns' : 9,
    'spriteSheetWidth' : 100,
    'spriteSheetHeight' : 100,
    'frameDelay' : 0,
    'frameDelayMax' : 10,
    'frameListaIndice' : 0,
    'PuloDireita' : [36,37,38,39,40,41,42,43,44],
    'PuloEsquerda' : [45,46,47,48,49,50,51,52,53],
    'paraEsquerdaAndando' : [9, 10, 11, 12, 13, 14,15, 16, 17],
    'paraDireitaAndando'  : [0, 1, 2, 3, 4, 5, 6, 7, 8],
    'paraEsquerdaParado' : [27,28,29,30,31,32,33,34,35],
    'paraDireitaParado' : [18,19, 20, 21, 22, 23, 24, 25, 26],
    'animacao' : 'paraDireitaParado'
}
ColiPla1 = pygame.Rect(0, 566, 256, 202)
lado = 0
pulo = 0
while (True):
    altPla = 564
    x = Warrior['x']
    y = Warrior['y']

    ColiPlayer = pygame.Rect(x, y, 100, 100)
    colisor = (Warrior['y'] + 100, Warrior['x'])
    Warrior['x'] += Warrior['velX']
    Warrior['y'] += Warrior['velY']
    screen1.blit(cenario, (0,0))
    pygame.draw.rect(screen1, [136,136,136], ColiPlayer)
    pintarSprite( Warrior, screen1, (Warrior['x'], Warrior['y']) )
    pygame.draw.rect(screen1, [136,136,136], ColiPla1)
    pygame.display.update()
    if ColiPlayer.colliderect(ColiPla1):
        Warrior['velY'] = 0
    if Warrior['y'] < altPla:
        Warrior['y'] = Warrior['y'] + 1
    if altPla == Warrior['y'] + 100:
        if lado == 0:
            Warrior['animacao'] = 'paraDireitaParado'
        if lado == 1:
            Warrior['animacao'] = 'paraEsquerdaParado'
    for e in pygame.event.get():
        if (e.type == QUIT):
            exit()
        elif (e.type == KEYDOWN):
            if (e.key == K_UP) and lado == 0:
                Warrior['animacao'] = 'PuloDireita'
                Warrior['velY'] = -3
                pulo = 1
            elif (e.key == K_UP) and lado == 1:
                Warrior['animacao'] = 'PuloEsquerda'
                Warrior['velY'] = -3
                pulo = 1
            if (e.key == K_LEFT) and pulo == 0:
                Warrior['animacao'] = 'paraEsquerdaAndando'
                Warrior['velX'] = -1
                lado = 1
            elif (e.key == K_RIGHT) and pulo == 0:
                Warrior['animacao'] = 'paraDireitaAndando'
                Warrior['velX'] = 1
                lado = 0


        elif (e.type == KEYUP):
            if (e.key == K_LEFT):
                Warrior['animacao'] = 'paraEsquerdaParado'
                Warrior['velY'] = 0
                Warrior['velX'] = 0
            elif (e.key == K_RIGHT):
                Warrior['animacao'] = 'paraDireitaParado'
                Warrior['velX'] = 0
            elif (e.key == K_UP):
                pulo = 0
                Warrior['velY'] = 0
    pygame.display.update()
    clk.tick(100)