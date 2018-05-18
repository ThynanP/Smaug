__author__ = 'Thynan'
import pygame, random
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN, FULLSCREEN
from pygame.time import Clock
from pygame.mixer import Sound
from Fase1 import *
def Menu():
    global screen
    clk = Clock()
    screen = pygame.display.set_mode( (1360, 768), FULLSCREEN, 32)
    Men = pygame.image.load("./menu/mn2.png").convert_alpha()
    Men1 = pygame.image.load("./menu/mn1.png").convert_alpha()
    arq1 = pygame.image.load("./menu/arq1.png").convert_alpha()
    arq2 = pygame.image.load("./menu/arq2.png").convert_alpha()
    arq3 = pygame.image.load("./menu/arq3.png").convert_alpha()
    arq4 = pygame.image.load("./menu/arq4.png").convert_alpha()
    arq5 = pygame.image.load("./menu/arq5.png").convert_alpha()
    arq6 = pygame.image.load("./menu/arq6.png").convert_alpha()
    arq7 = pygame.image.load("./menu/arq7.png").convert_alpha()
    arq8 = pygame.image.load("./menu/arq8.png").convert_alpha()
    arq9 = pygame.image.load("./menu/arq9.png").convert_alpha()
    arq10 = pygame.image.load("./menu/arq16.png").convert_alpha()
    arq11 = pygame.image.load("./menu/arq13.png").convert_alpha()
    arq12 = pygame.image.load("./menu/arq18.png").convert_alpha()
    arq13 = pygame.image.load("./menu/arq45.png").convert_alpha()
    arq14 = pygame.image.load("./menu/arq10.png").convert_alpha()
    arq15 = pygame.image.load("./menu/arq11.png").convert_alpha()
    arq16 = pygame.image.load("./menu/arq12.png").convert_alpha()
    arq17 = pygame.image.load("./menu/arq14.png").convert_alpha()
    imgs = [arq1,arq2,arq3,arq4,arq5,arq6,arq7,arq8,arq9,arq10,arq11,arq12,arq13, arq14, arq15, arq16, arq17]
    Bcomecar = pygame.Rect(522, 350, 336, 70) #rect de colisao com os botoes
    Bopcoes = pygame.Rect(536, 510, 270, 71)
    Bquit = pygame.Rect(580, 596, 200, 50)
    while (True):
        x = randint(0, 700)
        y = randint(0, 400)
        img = randint (0,16)
        pygame.draw.rect(screen, [136,136,136], Bopcoes)
        pygame.draw.rect(screen, [136,136,136], Bquit)
        pygame.draw.rect(screen, [136,136,136], Bcomecar)
        screen.blit(Men, (0, 0))
        screen.blit(imgs[img], (x,y))
        screen.blit(Men1, (0, 0))
        pygame.display.update()
        pygame.time.wait(3000)
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN: #teste de colisao
                mouse_pos = pygame.mouse.get_pos()
                if Bcomecar.collidepoint(mouse_pos):
                    Fase1()
                if Bquit.collidepoint(mouse_pos):
                    exit()
                if Bopcoes.collidepoint(mouse_pos):
                    Ops()
    clk.tick(500) #
def Ops():
    global screen
    global audio
    screen = pygame.display.set_mode( (1360, 768), FULLSCREEN, 32)
    Men = pygame.image.load("./menu/mn2.png").convert_alpha()
    op1 = pygame.image.load("./menu/op1.png").convert_alpha()
    ms1 = pygame.image.load("./menu/ms1.png").convert_alpha()
    ms2 = pygame.image.load("./menu/ms2.png").convert_alpha()
    len1 = pygame.image.load("./menu/len1.png").convert_alpha()
    len2 = pygame.image.load("./menu/len2.png").convert_alpha()
    voltar = pygame.image.load("./menu/volt.png").convert_alpha()
    Mus = 0
    Len = 0
    Bmusic = pygame.Rect(780, 392, 182, 70)
    Blegendas = pygame.Rect(718, 474, 360, 70)
    Bcreditos = pygame.Rect(474, 576, 406, 52)
    Bvoltar = pygame.Rect(60, 680, 100, 70)

    while(True):
        screen.blit(Men, (0, 0))
        screen.blit(op1, (0, 0))
        screen.blit(voltar, (60, 680))
        if Mus % 2 == 0:
            screen.blit(ms1, (780, 392))
            pygame.display.update()
        if Mus % 2 != 0:
            screen.blit(ms2, (780, 392))
            audio.stop()
            pygame.display.update()
        if Len % 2 == 0:
            screen.blit(len1, (718, 474))
            pygame.display.update()
        if Len % 2 != 0:
            screen.blit(len2, (718, 474))
            pygame.display.update()
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Bmusic.collidepoint(mouse_pos):
                    audio.play(-1)
                    Mus = Mus + 1
                if Blegendas.collidepoint(mouse_pos):
                    Len = Len + 1
                if Bcreditos.collidepoint(mouse_pos):
                    creditos()
                if Bvoltar.collidepoint(mouse_pos):
                    Menu()
def creditos():
    global screen
    screen = pygame.display.set_mode( (1360, 768), FULLSCREEN, 32)
    credi = pygame.image.load("./menu/credit.png").convert_alpha()
    voltar = pygame.image.load("./menu/volt.png").convert_alpha()
    Bvoltar = pygame.Rect(60, 680, 100, 70)
    while(True):
        screen.blit(credi, (0, 0))
        screen.blit(voltar, (60, 680))
        pygame.display.update()
        for e in pygame.event.get():
            if (e.type == QUIT):
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if Bvoltar.collidepoint(mouse_pos):
                    Ops()
def Inicio():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (1360, 768), FULLSCREEN, 32)
    audio = pygame.mixer.Sound("thy.wav")
    titulo = pygame.image.load("op1.png").convert_alpha()


    glitc = pygame.image.load("glitch.png")
    glitc1 = pygame.image.load("glitcha.jpg")
    glitch = pygame.transform.scale(glitc, (int(1360), int(768)))
    glitch1 = pygame.transform.scale(glitc1, (int(1360), int(768)))
    imgs = [titulo,glitch1,titulo,glitch,titulo,glitch,titulo,titulo,glitch1,titulo,titulo,titulo,glitch1]
    audio.play(-1)
    img = 0
    while (True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.blit(imgs[img], (0,0))
        pygame.display.update()
        pygame.time.wait(250)
        img = img + 1
        if img > 12:
            Menu() #chamando o menu

Inicio()
