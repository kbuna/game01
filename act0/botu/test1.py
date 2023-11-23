import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウのサイズ設定
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# タイトルとアイコン設定
pygame.display.set_caption("ゲームのタイトル")
icon = pygame.image.load("act0/o1.webp")  # アイコン画像をロード
pygame.display.set_icon(icon)

# 背景画像のロード
bg_image = pygame.image.load("act0/o1.webp")

# メインループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 背景の描画
    screen.blit(bg_image, (0, 0))

    # タイトルの描画
    font = pygame.font.Font(None, 74)
    text = font.render("ゲームのタイトル", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width/2, 100))
    screen.blit(text, text_rect)

    # メニューの表示
    # ...

    # 画面を更新
    pygame.display.update()

# 退出処理
pygame.quit()
