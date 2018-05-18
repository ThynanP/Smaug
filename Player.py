__author__ = 'amilton'
import pygame
from Sprites import *

lado = 0
numTiro = 0
velxTiro = 0
xTiro = 0
tiro = pygame.Rect(20,20,20,20)
V_hp = 100
Player = {
    'x' : 0,
    'y': 280,
    'velX' : 0,
    'velY' : 1,
    'Pulo':0,
    'ContPulo': 0,
    'spriteSheet' : pygame.image.load("./sprite.png"),
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





def Tiro():
    global xTiro
    global velxTiro
    global lado
    global tiro
    Player['x']
    global numTiro
    if numTiro == 4:
        numTiro == 0
        xTiro = Player['x']

    if lado == 0:
        Bala()
        velxTiro = 5
    if lado == 1:
        Bala()
        velxTiro = -5
    if xTiro > 800:
        xTiro = Player['x']

