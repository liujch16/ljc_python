import sys
import pygame

def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.tyoe == pygame.QUIT:
            sys.exit()