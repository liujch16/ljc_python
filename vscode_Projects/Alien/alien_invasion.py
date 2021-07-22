import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()#初始化pygame
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height)
        )#screen为一被创建的窗口，.set_mode()内的参数为此窗口的长宽
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()#使用sys()退出
        
        screen.fill(ai_setting.bg_color)#在每次活动后刷新screen
        ship.blitme()
        pygame.display.flip()
        
run_game()