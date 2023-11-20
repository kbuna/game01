


#0205 ミニゲームを作る →meteor.pyファイル







#0204 インデックスとタイマー

import tkinter
fnt1 = ("Times New Roman",20)#フォントの定義 小さいサイズ
fnt2 = ("Times New Roman",40)#大きなサイズ
index = 0#インデックス用変数
timer = 0#タイマー用の変数

key = ""#キーの値を代入する変数
def key_down(e):
    global key#キーをグローバル変数とする
    key = e.keysym#キーにkeysymの値を代入

def main():#メイン処理を行う関数
    global index, timer#これらをグローバル変数とする
    canvas.delete("STATUS")#一旦indexとtimerの表示を消す
    timer = timer +1#timerの値を1ずつ増やす
    #timerの値を表示
    canvas.create_text(200,30,text="index"+str(index),fill="white",font=fnt1,tag="STATUS")
    canvas.create_text(400,30,text="timer"+str(timer),fill="cyan",font=fnt1,tag="STATUS")
    #index0の処理（タイトル画面）
    #timerが1ならタイトルの文字を表示
    #スペースが押されたらタイトル文字を消し、キャンバスを青で塗りつぶそ、ゲーム中の文字を表示、indexを変更
    #index1の処理(プレイ画面)
    #Eキーが押されたらゲーム中の文字を消しキャンバスを栗色で塗りつぶしゲームオーバーを表示、indexを変更
    #index2の処理（ゲームオーバー画面）
    #timerが30になったらゲームオーバーの文字を消しindex0timer0
    #100ミリ秒後に再びループ
    if index == 0:
        if timer ==1:
            canvas.create_text(300,150,text="タイトル",fill="white",font=fnt2,tag="TITLE")
            canvas.create_text(300,300,text="Press[SPACE]Key",fill="lime",font=fnt2,tag="TITLE")
        if key == "space":
            canvas.delete("TITLE")
            canvas.create_rectangle(0,0,600,400,fill="blue",tag="GAME")
            canvas.create_text(300,150,text="ゲーム中",fill="white",font=fnt2,tag="GAME")
            index = 1
            timer = 0
    if index == 1:
        if key == "e":
            canvas.delete("GAME")
            canvas.create_rectangle(0,0,600,400,fill="maroon",tag="OVER")
            canvas.create_text(300,150,text="GAMEOVER",fill="red",font=fnt2,tag="OVER")
            index = 2
            timer = 0
    if index == 2:
        if timer == 30:
            canvas.delete("OVER")
            index = 0
            timer = 0
    root.after(100,main)

root = tkinter.Tk()#ウィンドウの部品を作る
root.title("インデックスとタイマー")#ウィンドウのタイトル指定
root.bind("<KeyPress>",key_down)#キーを押したときに実行する関数を指定
canvas = tkinter.Canvas(width=600,height=400,bg="black")#キャンバスの部品を作る
canvas.pack()#キャンバスを配置
main()#メイン処理を実行
root.mainloop()#ウィンドウを表示


#0203d カラフルな線

import tkinter
import math
root = tkinter.Tk()
root.title("三角関数で図形を描く")
canvas = tkinter.Canvas(width=600,height=600,bg="black")
canvas.pack()

COL = ["greenyellow","limegreen","aquamarine","cyan","deepskyblue","blue","blueviolet","violet"]
#10度ずつ角度をずらしながら長さ300ドットの線を引く
#ウィンドウ左上原点(0,0)からcosとsinで計算した(x,y)座標までcreate_line()関数で線を引いている
for d in range(0,360):
    x = 250 * math.cos(math.radians(d))
    y = 250 * math.sin(math.radians(d))
    canvas.create_line(300,300,300+x,300+y,fill=COL[d%8],width=2)
root.mainloop()

#600,600のウィンドウ 中心は300,300 三角関数で計算した距離250ドットの円周上に線を引く



#0203c 三角関数で図形を描く

import tkinter
import math
root = tkinter.Tk()
root.title("三角関数で線を引く")
canvas = tkinter.Canvas(width=400,height=400,bg="white")
canvas.pack()
#10度ずつ角度をずらしながら長さ300ドットの線を引く
#ウィンドウ左上原点(0,0)からcosとsinで計算した(x,y)座標までcreate_line()関数で線を引いている
for d in range(0,90,10):
    a = math.radians(d)
    x = 300 * math.cos(a)
    y = 300 * math.sin(a)
    canvas.create_line(0,0,x,y,fill="blue")
root.mainloop()

#0203b 三角関数の計算ソフト

import tkinter
import math
def trigo():
    try:
        d = float(entry.get())
        a = math.radians(d)
        s = math.sin(a)
        c = math.cos(a)
        t = math.tan(a)
        label_s["text"] = "sin" +str(s)
        label_c["text"] = "cos" +str(c)
        label_t["text"] = "tan" +str(t)
    except:
        print("角度を度の値で入力してください")
root = tkinter.Tk()
root.geometry("300x200")
root.title("三角関数の値")

entry = tkinter.Entry(width=10)
entry.place(x=20,y=20)
button = tkinter.Button(text="計算",command=trigo)
button.place(x=110,y=20)
label_s = tkinter.Label(text="sin")
label_s.place(x=20,y=60)
label_c = tkinter.Label(text="sin")
label_c.place(x=20,y=100)
label_t = tkinter.Label(text="sin")
label_t.place(x=20,y=140)

root.mainloop()





#0203a 三角関数 sin,cos,tanの値を求める
"""
度      ラジアン
0       0rad
90      (π/2)rad
180     πrad
270     (π*1.5)rad
360     (π*2)rad
"""
import math
d = 45#度
a = math.radians(d)#ラジアンに変換
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print("sin "+str(s))
print("cos "+str(c))
print("tan "+str(t))



#0202a ヒットチェック2

import tkinter
import math

def hit_check_circle():
    dis = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if dis <= r1 + r2:
        return True
    return False


def mouse_move(e):
    global x1, y1
    x1 = e.x
    y1 = e.y
    col = "green"
    if hit_check_circle() == True:
        col = "lime"
    canvas.delete("CIR1")
    canvas.create_oval(x1-r1, y1-r1, x1+r1, y1+r1, fill=col, tag="CIR1")

root = tkinter.Tk()
root.title("円によるヒットチェック")
canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()
canvas.bind("<Motion>", mouse_move)

#青い矩形の左上角x,y座標、矩形の幅、矩形の高さ
x1=50
y1=50
r1=40
canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill="green",tag="CIR1")
#赤い矩形の同上
x2=300
y2=200
r2=80

canvas.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill="orange")

root.mainloop()




# list 0201a

import tkinter

def hit_check_rect():
    dx = abs((x1+w1/2) - (x2+w2/2))
    dy = abs((y1+h1/2) - (y2+h2/2))
    #青の中心座標-赤の中心座標 xと横幅、yと高さ
    if dx <= w1/2+w2/2 and dy <= h1/2+h2/2:
        return True
    #青の横幅の半分＋赤の横幅の半分を足した数が、
    #青と赤の中心の値
    return False
  #abs()で絶対値を求められる
  #dxに2の矩形の中心間のx方向の距離を代入
  #dyにはy方向
  #矩形が重なる条件をifで判定


def mouse_move(e):
    global x1, y1
    x1 = e.x - w1/2
    y1 = e.y - h1/2
    col = "blue"
    if hit_check_rect() == True:
        col = "cyan"
    canvas.delete("RECT1")
    canvas.create_rectangle(x1, y1, x1+w1, y1+h1, fill=col, tag="RECT1")

root = tkinter.Tk()
root.title("矩形によるヒットチェック")
canvas = tkinter.Canvas(width=600, height=400, bg="white")
canvas.pack()
canvas.bind("<Motion>", mouse_move)

#青い矩形の左上角x,y座標、矩形の幅、矩形の高さ
x1=50
y1=50
w1=120
h1=60
canvas.create_rectangle(x1,y1,x1+w1,y1+h1,fill="blue",tag="RECT1")
#赤い矩形の同上
x2=300
y2=100
w2=120
h2=160
canvas.create_rectangle(x2,y2,x2+w2,y2+h2,fill="red")

root.mainloop()