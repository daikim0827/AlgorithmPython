#######################################################
# 石取りゲーム2
#######################################################
f = [0] * 21
f[1] = f[2] = 1
for i in range(3, 21):
    f[i] = f[i - 1] + f[i - 2]
print('最後に石を取った側が勝ちです．パスはできません．')
n = int(input('石の数 (2..10000)? '))
if n < 1 or n > 1000:
    exit()
max = n - 1
my_turn = 1
while n > 0:
    print('%d 個まで取れます' % max)
    if my_turn % 2 == 1:
        x = n
        i = 20
        while x > f[i]:
            if x > f[i]:
                x -= f[i]
        if x > max:
            x = 1
        print('私は %d 個の石を取ります．' % x)
    else:
        while True:
            x = int(input('何個取りますか? '))
            if x >= 1 and x <= max:
                break
    n -= x
    max = 2 * x
    if max > n:
        max = n
    print('残りは %d 個です．' % n)
    my_turn += 1
if my_turn % 2 == 1:
    print('あなたの勝ちです．')
else:
    print('私の勝ちです．')
