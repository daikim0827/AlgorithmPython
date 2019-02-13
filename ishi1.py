#######################################################
# 石取りゲーム1
#######################################################
print('最後に石を取った側が負けです．パスはできません．')
n = int(input('石の数? '))
m = int(input('1回にとれる最大の石の数? '))
if n < 1 or m < 1:
    exit()
my_turn = 1
while n > 0:
    if my_turn % 2 == 1:
        x = (n - 1) % (m + 1)
        if x == 0:
            x = 1
        print('私は %d 個の石を取ります．' % x)
    else:
        while True:
            x = int(input('何個取りますか? '))
            if x > 0 and x <= m and x <= n:
                break
    n -= x
    print('残りは %d 個です．' % n)
    my_turn += 1
if my_turn % 2 == 1:
    print('あなたの負けです．')
else:
    print('私の負けです．')
