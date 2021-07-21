import sys#使用模块sys()来退出游戏
import pygame

from settings import Setting

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()#初始化背景设置
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_width))#调用pygame.display.set_mode()来创建一个名为screen的显示窗口，实参(1200, 800)
    #是一个元组，指定了游戏窗口的尺寸
    pygame.display.set_caption("Alien Invasion")
    bg_color = (ai_settings.bg_color)
    #开始游戏的主循环
    while True:#包含一个事件循环以及管理屏幕更新的代码

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#当检测到pygame.QUIT事件后使用sys.exit()方法退出
                sys.exit()
        #用背景色填充屏幕，screen.fill()接受一个使用rgb值表示的颜色实参
        screen.fill(bg_color)
        #让最近绘制的屏幕可见
        pygame.display.flip()#使最近绘制的屏幕可见，在每次执行while循环时都绘制一个空屏幕并擦掉旧屏幕

run_game()
