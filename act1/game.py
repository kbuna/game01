




#1015 マウスポインタの座標を用いる

import tkinter
def mouse_click(e):
   px = e.x
   py = e.y
   print(f"マウスポインタ座標は{px},{py}")
   mx = int(px/48)
   my = int(py/48)
   if 0 <= mx and mx <= 6 and 0 <= my and my <= 4:
      n = map_data[my][mx]
      print("ここにあるマップチップは"+CHIP_NAME[n])
# map_data[][]  my=0  =0～47

root = tkinter.Tk()
root.title("マップデータ")
canvas = tkinter.Canvas(width=336,height=240)
canvas.pack()
canvas.bind("<Button>",mouse_click)
CHIP_NAME=["草","花","森","海"]
img =[
   tkinter.PhotoImage(file="chip0.png"),
   tkinter.PhotoImage(file="chip1.png"),
   tkinter.PhotoImage(file="chip2.png"),
   tkinter.PhotoImage(file="chip3.png")
]
map_data = [
   [0,1,0,2,2,2,2],
   [3,0,0,0,2,2,2],
   [3,0,0,1,0,0,0],
   [3,3,0,0,0,0,1],
   [3,3,3,3,0,0,0]
]

for y in range(5):
   for x in range(7):
      n = map_data[y][x]
      canvas.create_image(x*48+24,y*48+24,image=img[n])

root.mainloop()




#1014マップを表示する


import tkinter

root = tkinter.Tk()
root.title("マップデータ")
canvas = tkinter.Canvas(width=336,height=240)
canvas.pack()

img =[
   #上から草、花、森、海
   tkinter.PhotoImage(file="chip0.png"),
   tkinter.PhotoImage(file="chip1.png"),
   tkinter.PhotoImage(file="chip2.png"),
   tkinter.PhotoImage(file="chip3.png")
]
#7x5
map_data = [
   [0,1,0,2,2,2,2],
   [3,0,0,0,2,2,2],
   [3,0,0,1,0,0,0],
   [3,3,0,0,0,0,1],
   [3,3,3,3,0,0,0]
]

for y in range(5):
   for x in range(7):
      n = map_data[y][x]
      canvas.create_image(x*48+24,y*48+24,image=img[n])
# y は5回分、xは7回文繰り返す
# 縦横48ドット、中央は縦横24ドット


root.mainloop()





#1013c キャラクターのアニメ―ション

import tkinter
x = 0
ani = 0
def animation():
  global x, ani
  x = (x+4)%480
  #x = x + 4
  #if x == 480:
  #  x=0
  canvas.delete("BG")
  canvas.create_image(x-240,150,image=img_bg,tag="BG")
  canvas.create_image(x+240,150,image=img_bg,tag="BG")
  ani = (ani+1)%4
  #剰余演算では左辺より右辺が大きければ商は0になる
  #ani = ani + 1 , if ani ==4, ani=0という三行の機能をもつ
  canvas.create_image(240,200,image=img_dog[ani],tag="BG")
  root.after(200,animation)

root = tkinter.Tk()
root.title("アニメーション")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
img_dog = [
  tkinter.PhotoImage(file="dog0.png"),
  tkinter.PhotoImage(file="dog1.png"),
  tkinter.PhotoImage(file="dog2.png"),
  tkinter.PhotoImage(file="dog3.png")
]
animation()
root.mainloop()



#1013b 背景をスクロール
import tkinter
x = 0
def scroll_bg():
    global x
    x = x + 1
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240, 150, image=img_bg, tag="BG")
    canvas.create_image(x+240, 150, image=img_bg, tag="BG")
    root.after(50, scroll_bg)

root = tkinter.Tk()
root.title("画面のスクロール")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
scroll_bg()
root.mainloop()




#0103 キャラクターのアニメーション
#キャンバスを描画する
"""
幅480高さ300
240,150を指定するとキャンバスの中央に画像を表示
"""

import tkinter
root = tkinter.Tk()
root.title
canvas = tkinter.Canvas(width=480,height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
canvas.create_image(240,150,image=img_bg)
root.mainloop()


#0102
"""
after()命令でリアルタイム処理を行う
"""
import tkinter
import datetime

def time_now():
  d = datetime.datetime.now()
  t = f"{d.hour}:{d.minute}:{d.second}"
  label["text"] = t
  root.after(1000,time_now)

root = tkinter.Tk()
root.geometry("400x100")
root.title("簡易時計")
label = tkinter.Label(font=("Times New Roman",60))
label.pack()
time_now()
root.mainloop()



#lst0101b
"""
bind()命令で取得できるイベント
keyPress キーを押した
KeyRelease キーを離した
Mottion マウスポインタを動かした
ButtonPress Button マウスボタンをクリック
ButtonRelease マウスボタンを話した
"""
import tkinter

def kew_down(e):
  key_c = e.keycode
  label1["text"] = "keycode" + str(key_c)
  key_s = e.keysym
  label2["text"] = "keysym" + key_s

root = tkinter.Tk()
root.geometry("400x200")
root.title("キー入力")
root.bind("<KeyPress>",kew_down)
fnt = ("Times New Roman",30)
label1 = tkinter.Label(text="keycode",font=fnt)
label1.place(x=0,y=0)
label2 =tkinter.Label(text="keysym",font=fnt)
label2.place(x=0,y=80)
root.mainloop()


#list0101

import tkinter
root = tkinter.Tk()
root.geometry("400x200")
root.title("PythonでGUIを扱う")
label = tkinter.Label(root,text="ゲーム開発の一歩",font=("Times New Roman",20))
label.place(x=80,y=60)
root.mainloop()