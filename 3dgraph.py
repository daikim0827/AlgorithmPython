#######################################################
# 3次元グラフ
#######################################################　　
import svgplot
import math

# 座標の下限
Xmin = -1
Ymin = -1
Zmin = -1

# 座標の上限
Xmax = 1
Ymax = 1
Zmax = 1

# 描画する関数
def func(x, z):
    r2 = x * x + z * z
    return math.exp(-r2) * math.cos(10 * math.sqrt(r2))

svgplot.plot_start(480, 260)
lowerhorizon = []
upperhorizon = []
for i in range(241):
    lowerhorizon.append(2e300)  # 正の最大値
    upperhorizon.append(-2e300) # 負の最大値
i = 240
for iz in range(21):
    z = Zmin + (Zmax - Zmin) / 20 * iz
    ok1 = 0
    for ix in range(201):
        x = Xmin + (Xmax - Xmin) / 200 * ix
        i = ix + 2 * (20 - iz) # 0..240
        y = 30 * (func(x, z) - Ymin) / (Ymax - Ymin) + 5 * iz # 0..130
        ok = 0
        if y < lowerhorizon[i]:
            lowerhorizon[i] = y
            ok = 1
        if y > upperhorizon[i]:
            upperhorizon[i] = y
            ok = 1
        if ok == 1 and ok1 == 1:
            svgplot.draw(2*i, 2*y)
        else:
            svgplot.move(2*i, 2*y)
        ok1 = ok
svgplot.plot_end(0)
