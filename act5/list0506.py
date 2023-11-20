

#同時キー入力を行う
#pygame.key.get_pressed()を使う


"""
key=pygame.key.get_pressed()という1行の記述で、全てのキーの状態を取得できる。
この命令を用いて、カーソルキーとスペースキーを同時に判定するプログラム。
keyはタプルになる。値を変更できないリスト。

----
K_  UP,DOWN,LEFT,RIGHT    SPACE  

エンター  RETURN
ESC ESCAPE
A-Z a-z
0-9 0-9
SHIFT RSHIFT LSHIFT
fun F0-12



"""

import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
BROWN = (192,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)


def main():
  pygame.init()#pygameモジュールの初期化
  pygame.display.set_caption("pygameの使い方")#タイトル指定
  screen = pygame.display.set_mode((960,720))#描画面を初期化
  clock = pygame.time.Clock()#clockオブジェクトを作成
  font = pygame.font.Font(None,80)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    
    screen.fill(BLACK)

    key = pygame.key.get_pressed()#keyに全てのキーの状態を代入
    #各種キーの値を描いたSurfaceを生成
    txt1 = font.render(f"UP{key[pygame.K_UP]} DOWN{key[pygame.K_DOWN]}",True,WHITE,GREEN)
    txt2 = font.render(f"LEFT{key[pygame.K_LEFT]} RIGHT{key[pygame.K_RIGHT]}",True,WHITE,BLUE)
    txt3 = font.render(f"SPACE{key[pygame.K_SPACE]} Z{key[pygame.K_z]}",True,WHITE,BROWN)

    screen.blit(txt1,[200,100])#文字列を描いたSurfaceを画面に転送
    screen.blit(txt2,[200,300])
    screen.blit(txt3,[200,500])

    pygame.display.update()#画面を更新する
    clock.tick(30)#フレームレートを指定

if __name__ == '__main__':#このプログラムが直接実行されたときに
  main()#main関数を呼び出す
