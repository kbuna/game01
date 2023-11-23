import pygame
import sys

# ゲームの初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("経営シミュレーションゲーム")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フォント
font = pygame.font.Font(None, 36)

# タイトル画像の読み込み
title_image = pygame.image.load("act0/o1.webp")  # 画像のパスを適切に指定してください

# スタート画面の項目
menu_items = ["はじめから", "つづきから", "オプション"]
selected_item = 0  # 選択中の項目

# ゲームの状態
current_state = "start_menu"

# ゲームループ
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # キー入力の処理
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_item = (selected_item + 1) % len(menu_items)
            elif event.key == pygame.K_UP:
                selected_item = (selected_item - 1) % len(menu_items)
            elif event.key == pygame.K_RETURN:
                if menu_items[selected_item] == "はじめから":
                    current_state = "new_game"
                elif menu_items[selected_item] == "つづきから":
                    current_state = "load_game"
                elif menu_items[selected_item] == "オプション":
                    current_state = "options"

    # 画面の描画
    screen.fill(WHITE)

    # タイトル画像の描画
    title_rect = title_image.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title_image, title_rect)

    # スタート画面のボタン描画
    for i, item in enumerate(menu_items):
        color = BLACK if i == selected_item else WHITE
        text = font.render(item, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 300 + i * 50))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

# ゲーム終了
pygame.quit()
sys.exit()