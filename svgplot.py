#######################################################
# SVGグラフィックス
#######################################################

def static():
    static.ymax = 0

# プロット開始
def plot_start(x, y):
    print("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" width=\"%d\" height=\"%d\">" % (x, y))
    print("<path d=\"", end="")
    static.ymax = y

# プロット終了
def plot_end(close):
    # 1なら閉じる（出発点に戻る線を引く）。0なら閉じない
    if close == 1:
        print("Z")
    print("\" fill=\"none\" stroke=\"black\" />")
    print("</svg>\n")

# ペンアップで移動
def move(x, y):
    print("M %g %g " % (x, static.ymax - y), end="")

# ペンアップで移動（相対座標）
def move_rel(dx, dy):
    print("m %g %g " % (dx, -dy), end="")

# ペンダウンで移動
def draw(x, y):
    print("L %g %g " % (x, static.ymax - y), end="")

# ペンダウンで移動（相対座標）
def draw_rel(dx, dy):
    print("l %g %g" % (dx, -dy), end="")