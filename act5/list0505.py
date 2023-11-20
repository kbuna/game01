

#画像の回転と拡大縮小表示

"""
回転            img_r =pygame.transform.rotate(img,回転角)
拡大縮小        img_s =pygame.transform.scale(img,[幅,高さ])
回転＋拡大縮小  img_rz =pygame.transform.rotozoom(img,回転角,大きさの比率)

変数名は自由
回転角は度(degree)で指定する
大きさの比率は1.0が等倍、幅高さを倍にしたければ2.0

scale()rotate()は描画速度を優先する命令で、回転や拡大縮小後の画像に粗が目立つことがある
ここではrotozoom()で滑らかな画像を描画している

・画像の表示位置について
このプログラムでは、宇宙船は常に画面中央に表示される
    ang = (ang+1)%360 #回転角度を加算する
    img_rz = pygame.transform.rotozoom(img_sship,ang,1.0)#回転した宇宙船の画像を作る
    x = 480 - img_rz.get_width()/2#表示するx座標を計算する
    y = 360 - img_rz.get_height()/2#表示するy座標を計算する
    screen.blit(img_rz,[x,y])#回転した宇宙船の画像を描画する

変数ang を毎フレーム1ずつ加算する。359まで増えたあと0に戻り、また加算していく
img_rzは、angの角度で回転させた画像。
img_rz.get_width()で、その画像の幅、height()で高さを取得する。幅と高さの値はドット数。

このプログラムのウィンドウサイズは幅960x高さ720ドット。
よって中心座標は、480,360になる。
画像を表示するx座標を、回転した画像の幅の半分を、480から引いた値として、
y座標を、回転した画像の高さの半分を、360から引いた値にすることで、
宇宙船の位置が常に画面中央になる
"""

import pygame
import sys

img_galaxy = pygame.image.load("act5/image/galaxy.png")
img_sship = pygame.image.load("act5/image/starship.png")


def main():
  pygame.init()#pygameモジュールの初期化
  pygame.display.set_caption("pygameの使い方")#タイトル指定
  screen = pygame.display.set_mode((960,720))#描画面を初期化
  clock = pygame.time.Clock()#clockオブジェクトを作成
  ang =0 #回転角度を管理する変数angを宣言

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
    
    ang = (ang+1)%360 #回転角度を加算する
    img_rz = pygame.transform.rotozoom(img_sship,ang,1.0)#回転した宇宙船の画像を作る
    x = 480 - img_rz.get_width()/2#表示するx座標を計算する
    y = 360 - img_rz.get_height()/2#表示するy座標を計算する
    screen.blit(img_rz,[x,y])#回転した宇宙船の画像を描画する

    pygame.display.update()#画面を更新する
    clock.tick(30)#フレームレートを指定

if __name__ == '__main__':#このプログラムが直接実行されたときに
  main()#main関数を呼び出す
