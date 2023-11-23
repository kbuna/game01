import pygame
import sys
import os

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("経営型ゲーム")

font = pygame.font.Font(None, 36)

# 画像の読み込み
def load_image(file_path):
    if os.path.exists(file_path):
        return pygame.image.load(file_path)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

img_title = [
    load_image("act0/image_gl/o1.webp"),
    load_image("act0/image_gl/logo.png")
]

# ゲームの状態を表す変数
game_state = "menu"  # 初めはメニュー画面

# ボタンのクラス
class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, color):
        draw_text(self.text, color, self.rect.centerx, self.rect.centery)

# ボタンの初期設定
start_button = Button("START", screen_width // 6, screen_height // 4 +30, 200, 50)
continue_button = Button("CONTINUE", screen_width // 6, screen_height // 4 + 60, 200, 50)

# 音楽の読み込みと再生
def load_music(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

load_music("act8/sound_gl/bgm.ogg")

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "menu":
                if start_button.rect.collidepoint(event.pos):
                    game_state = "start"
                elif continue_button.rect.collidepoint(event.pos):
                    game_state = "continue"
            elif game_state == "start":
                # START画面でのクリック処理
                pass
            elif game_state == "continue":
                # CONTINUE画面でのクリック処理
                pass

    # ボタンのホバーエフェクト
    start_hover = start_button.rect.collidepoint(pygame.mouse.get_pos())
    continue_hover = continue_button.rect.collidepoint(pygame.mouse.get_pos())

    screen.fill(pygame.Color("white"))

    if game_state == "menu":
        # タイトルロゴ表示
        screen.blit(img_title[0], [0, 0])
        screen.blit(img_title[1], [340, 80])

        start_color = pygame.Color("blue") if start_hover else pygame.Color("black")
        start_button.draw(start_color)

        continue_color = pygame.Color("blue") if continue_hover else pygame.Color("black")
        continue_button.draw(continue_color)

    elif game_state == "start":
        screen.fill(pygame.Color("blue"))
        # START画面の描画や処理を追加
    elif game_state == "continue":
        screen.fill(pygame.Color("yellow"))
        # CONTINUE画面の描画や処理を追加

    pygame.display.flip()

# BGMの停止
pygame.mixer.music.stop()

pygame.quit()
sys.exit()
