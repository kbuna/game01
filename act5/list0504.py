

#pygameで画像を描く

"""
Pygameのキー入力について
キー入力を判定する方法は２つある。ここではイベントとして入力を受け取っている。

if event.type == pygame.KEYDOWN:
  if event.key == pygame.キーボード定数:
    処理

  キーを押すイベントが発生したときに、どのキーが押されているかを調べる
  もう一つの方法は0506で。

"""

import pygame
import sys

img_galaxy = pygame.image.load("act5/image/galaxy.png")


def main():
  pygame.init()#pygameモジュールの初期化
  pygame.display.set_caption("pygameの使い方")#タイトル指定
  screen = pygame.display.set_mode((960,720))#描画面を初期化
  clock = pygame.time.Clock()#clockオブジェクトを作成

  while True:
    for event in pygame.event.get():#pygameのイベントを繰り返し実行
      if event.type == pygame.QUIT:#ウィンドウのxをクリックしたとき
        pygame.quit()#pygameモジュールの初期化を解除
        sys.exit()#プログラムを終了
      if event.type == pygame.KEYDOWN:#キーを押すイベントが発生したとき
        if event.key == pygame.K_F1:#F1キーならフルスクリーンモード
          screen = pygame.display.set_mode((960,720),pygame.FULLSCREEN)
        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:#F2キーかESCなら通常表示
          screen = pygame.display.set_mode((960,720))

    
    screen.blit(img_galaxy,[0,0])#画像を描画する
    pygame.display.update()#画面を更新する
    clock.tick(30)#フレームレートを指定

if __name__ == '__main__':#このプログラムが直接実行されたときに
  main()#main関数を呼び出す
