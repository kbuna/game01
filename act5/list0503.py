

#pygameで図形を描く

"""
font = pygame.font.Font(None,80)
  フォントを指定して、フォントオブジェクトを作る
sur = font.render(str(tmr),True,WHITE)
  レンダー命令で文字列と色を指定し、文字列を描いたSurfaceを生成。
  2つ目の引数Trueは文字縁が滑らかになる
screen.blit(sur,[300,200])
  blit()命令でsurfaceを画面に転送する

  図形の描画命令
線      pygame.draw.line(surface,color,start_pos,end_pos,width=1)
矩形    pygame.draw.rect(surface,color,rect,width=0)
多角形  pygame.draw.line(surface,color,pointlist,width=0)
円      pygame.draw.line(surface,color,pos,radius,width=0)
楕円    pygame.draw.line(surface,color,rect,width=0)
円弧    pygame.draw.line(surface,color,rect,start_angle,stop_angle,width=1)

・surfaceは描画面です
・colorはRGB値で(R,G,B)
・rectは矩形の左上角の座標と大きさで、[x,y,w,h]
・pointlistは[[x1,y1].[x2,y2],///]というように複数の頂点を指定
・widthは枠線の太さ。width=0は何も指定しなければ塗りつぶした図形に
・円弧のstart_angle(開始角)とstop_angle(終了角)はラジアンで指定
"""

import pygame
import sys

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

def main():
  pygame.init()#pygameモジュールの初期化
  pygame.display.set_caption("pygameの使い方")#タイトル指定
  screen = pygame.display.set_mode((800,600))#描画面を初期化
  clock = pygame.time.Clock()#clockオブジェクトを作成
  font = pygame.font.Font(None,80)#フォントオブジェクトを作成
  tmr = 0#時間管理する変数を宣言

  while True:
    for event in pygame.event.get():#pygameのイベントを繰り返し実行
      if event.type == pygame.QUIT:#ウィンドウのxをクリックしたとき
        pygame.quit()#pygameモジュールの初期化を解除
        sys.exit()#プログラムを終了
    
    screen.fill(BLACK)#指定した色で画面全体を塗りつぶす

    tmr = tmr+1#tmrの値を1増やす
    col = (0,tmr%256,0)#colに色を指定するための値を代入
    pygame.draw.rect(screen,col,[100,100,600,400])#(100,100)から幅600,高さ400の矩形を描く
    sur = font.render(str(tmr),True,WHITE)#Surfaceに文字列を描く
    screen.blit(sur,[300,200])#文字列を描いたSurefaceを画面に転送

    pygame.display.update()#画面を更新
    clock.tick(30)#フレームレートを指定

if __name__ == '__main__':#このプログラムが直接実行されたときに
  main()#main関数を呼び出す
