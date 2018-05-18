__author__ = 'amilton'

import pygame
from pygame.locals import *
import math
from math import *

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
