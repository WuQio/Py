# coding:utf-8
import os
import pygame
from pygame.locals import *

pygame.init()
text = 'Zeppelin'
font = pygame.font.SysFont('Consolas', 100)
ftext = font.render(text, True, (255, 0, 0), (255, 255, 255))
pygame.image.save(ftext, 'zhongwen.jpg')
