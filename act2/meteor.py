import tkinter
import random

#フォント
fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 50)
index = 0
timer = 0
score = 0
bg_pos = 0#背景の表示位置
#プレイやのxy座標
px = 240
py = 540


METEO_MAX = 30 #流星の数
mx = [0]*METEO_MAX#流星のx座標
my = [0]*METEO_MAX#流星のy座標

key = ""
koff = False
def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

def main():
    global key, koff, index, timer, score, bg_pos, px
    timer = timer + 1
    bg_pos = (bg_pos+1)%640
    canvas.delete("SCREEN")
    canvas.create_image(240, bg_pos-320, image=img_bg, tag="SCREEN")
    canvas.create_image(240, bg_pos+320, image=img_bg, tag="SCREEN")

    #タイトル画面
    #タイトル文字表示、プレスキー表示、
    #キーが押されたら、スコア０、宇宙船の位置を中央に、流星座標を初期値に、インデックスを１へ
    if index == 0:
        canvas.create_text(240, 240, text="METEOR", fill="gold", font=fnt2, tag="SCREEN")
        canvas.create_text(240, 480, text="Press [SPACE] Key", fill="lime", font=fnt1, tag="SCREEN")
        if key == "space":
            score = 0
            px = 240
            init_enemy()
            index = 1
    #ゲーム中 スコアを増やす、宇宙船を動かす、流星を動かす
    if index == 1:
        score = score + 1
        move_player()
        move_enemy()
    #ゲームオーバー画面、流星を動かす、ゲームオーバー文字を表示
    #タイマーが60になったら、インデックスの値を０に、タイマーを０に、
    #スコアを表示
    if index == 2:
        move_enemy()
        canvas.create_text(240, timer*4, text="GAME OVER", fill="red", font=fnt2, tag="SCREEN")
        if timer == 60:
            index = 0
            timer = 0
    canvas.create_text(240, 30, text="SCORE "+str(score), fill="white", font=fnt1, tag="SCREEN")

    #koffがトゥルーなら、値をクリアし、Falseを代入
    if koff == True:
        key = ""
        koff = False
    #50ミリ秒後にmainを再実行
    root.after(50, main)


#2点間の距離を判定、36ドット未満ならTrue
def hit_check(x1, y1, x2, y2):
    if((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) < 36*36):
        return True
    return False

#流星の座標を初期位置にする xy座標を乱数で決める
def init_enemy():
    for i in range(METEO_MAX):
        mx[i] = random.randint(0, 480)
        my[i] = random.randint(-640, 0)

#流星を動かす、繰り返しで流星のy座標を変化、yが660を超えたら、xとyを乱数で決め直す
#ゲーム中に宇宙船と接触したら、index2へtimer0へ
#流星を描画する
def move_enemy():
    global index, timer
    for i in range(METEO_MAX):
        my[i] = my[i] + 6+i/5
        if my[i] > 660:
            mx[i] = random.randint(0, 480)
            my[i] = random.randint(-640, 0)
        if index == 1 and hit_check(px, py, mx[i], my[i]) == True:
            index = 2
            timer = 0
        canvas.create_image(mx[i], my[i], image=img_enemy, tag="SCREEN")

#宇宙船を動かす 左キーが押され、かつpx>30なら pxの値を10減らす、右キーかつpx<450なら10増やす
def move_player():
    global px
    if key == "Left" and px > 30:
        px = px - 10
    if key == "Right" and px < 450:
        px = px + 10
    canvas.create_image(px, py, image=img_player[timer%2], tag="SCREEN")

root = tkinter.Tk()
root.title("Mini Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=480, height=640)
canvas.pack()
img_player = [
    tkinter.PhotoImage(file="act2/starship0.png"),
    tkinter.PhotoImage(file="act2/starship1.png")
]
img_enemy = tkinter.PhotoImage(file="act2/meteo.png")
img_bg = tkinter.PhotoImage(file="act2/cosmo.png")
main()
root.mainloop()
