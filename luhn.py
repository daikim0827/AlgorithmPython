#######################################################
# 誤り検出符号（クレジットカード番号をチェックするLuhnのアルゴリズム
#######################################################

s = 5555555555554444  # カード番号
digit = len(str(s))
w = 1
t = 0
for i in reversed(range(digit)):
    d = w * (s % 10)
    s = s // 10
    if d > 9:
        d -= 9
    t += d
    w = 3 - w
if t % 10 == 0:
    print('有効')
else:
    print('無効')