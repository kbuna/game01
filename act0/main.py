import pygame
import sys
import math
import random
from pygame.locals import *

BLACK = (  0,   0,   0)
SILVER= (192, 208, 224)
RED   = (255,   0,   0)
CYAN  = (  0, 224, 255)

# 画像の読み込み
img_galaxy = pygame.image.load("act0/image_gl/o1.webp")
img_title = [
    pygame.image.load("act0/image_gl/o1.webp"),
    pygame.image.load("act0/image_gl/logo.png")
]

# SEを読み込む変数
se_barrage = None
se_damage = None
se_explosion = None
se_shot = None

idx = 0
tmr = 0
score = 0
hisco = 10000
new_record = False
bg_y = 0

ss_x = 0
ss_y = 0
ss_d = 0
ss_shield = 0
ss_muteki = 0
key_spc = 0
key_z = 0


def get_dis(x1, y1, x2, y2): # 二点間の距離を求める
    return( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )


def draw_text(scrn, txt, x, y, siz, col): # 立体的な文字の表示
    fnt = pygame.font.Font(None, siz)
    cr = int(col[0]/2)
    cg = int(col[1]/2)
    cb = int(col[2]/2)
    sur = fnt.render(txt, True, (cr,cg,cb))
    x = x - sur.get_width()/2
    y = y - sur.get_height()/2
    scrn.blit(sur, [x+1, y+1])
    cr = col[0]+128
    if cr > 255: cr = 255
    cg = col[1]+128
    if cg > 255: cg = 255
    cb = col[2]+128
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr,cg,cb))
    scrn.blit(sur, [x-1, y-1])
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x, y])

def main(): # メインループ
    global idx, tmr, score, new_record, bg_y, ss_x, ss_y, ss_d
    global se_barrage, se_damage, se_explosion, se_shot

    pygame.init()#pygameの初期化
    pygame.display.set_caption("経営型ゲーム")#タイトルを作成
    
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))#画面を作成


    clock = pygame.time.Clock()#クロックオブジェクトを作成
    #SEを格納
    se_barrage = pygame.mixer.Sound("act8/sound_gl/barrage.ogg")
    se_damage = pygame.mixer.Sound("act8/sound_gl/damage.ogg")
    se_explosion = pygame.mixer.Sound("act8/sound_gl/explosion.ogg")
    se_shot = pygame.mixer.Sound("act8/sound_gl/shot.ogg")


    #クリック追加テスト部分
    font = pygame.font.Font(None, 36)
    def draw_text(text, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # ゲームの状態を表す変数
    game_state = "menu"  # 初めはメニュー画面

    # ボタンの初期設定
    start_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
    continue_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 20, 200, 50)



    running = True
    
    while running:
        tmr = tmr + 1 #タイマー増やす

        for event in pygame.event.get():
            if event.type == QUIT:#Quitを感知したら全部終了
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                        if game_state == "menu":
                            if start_button_rect.collidepoint(event.pos):
                                game_state = "start"
                            elif continue_button_rect.collidepoint(event.pos):
                                game_state = "continue"
                        elif game_state == "start":
                            # START画面でのクリック処理
                            pass
                        elif game_state == "continue":
                            # CONTINUE画面でのクリック処理
                            pass

        # タイトル画面の背景のスクロール
        bg_y = (bg_y+16)%720
        screen.blit(img_galaxy, [0, 0])
        key = pygame.key.get_pressed()
        

            if game_state == "menu": # タイトル
                #タイトルロゴ表示
                screen.blit(img_title[1], [340, 80])

                if start_button_rect.collidepoint(event.pos):
                        game_state = "start"
                elif continue_button_rect.collidepoint(event.pos):
                        game_state = "continue"
                pygame.mixer.music.load("act8/sound_gl/bgm.ogg")
                pygame.mixer.music.play(-1)

            # ゲームプレイ中
            if game_state == "start":
                # START画面でのクリック処理
                pass
            if game_state == "continue":
                # CONTINUE画面でのクリック処理
                pass


        #画面上部スコア表示
        #draw_text(screen, "SCORE "+str(score), 200, 30, 50, SILVER)
        #draw_text(screen, "HISCORE "+str(hisco), 760, 30, 50, CYAN)


        # ボタンのホバーエフェクト
        start_hover = start_button_rect.collidepoint(pygame.mouse.get_pos())
        continue_hover = continue_button_rect.collidepoint(pygame.mouse.get_pos())

        screen.fill(pygame.Color("white"))

        if game_state == "menu":
            start_color = pygame.Color("blue") if start_hover else pygame.Color("black")
            draw_text("START", start_color, screen_width // 2, screen_height // 2 - 25)

            continue_color = pygame.Color("yellow") if continue_hover else pygame.Color("black")
            draw_text("CONTINUE", continue_color, screen_width // 2, screen_height // 2 + 75)
        elif game_state == "start":
            screen.fill(pygame.Color("blue"))
            # START画面の描画や処理を追加
        elif game_state == "continue":
            screen.fill(pygame.Color("yellow"))
            # CONTINUE画面の描画や処理を追加

        pygame.display.flip()



        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
