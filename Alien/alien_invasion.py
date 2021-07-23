from button import Button
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
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
    #创建一个外星人编组
    aliens = Group()
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:    
            ship.update()
            #更新子弹的位置
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
            play_button)
        
run_game()