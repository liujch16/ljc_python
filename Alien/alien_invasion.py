import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()#初始化pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
        )#screen为一被创建的窗口，.set_mode()内的参数为此窗口的长宽
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()