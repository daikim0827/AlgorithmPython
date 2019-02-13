#######################################################
# 安定な結婚の問題
#######################################################
N = 3   # 各性の人数
boy = [0] * (N + 1)
girl = [[0] * (N + 1)] * (N + 1)
position = [0] * (N + 1)
rank = [[0] * (N + 1)] * (N + 1)
for g in range(1, N + 1):   # 各女性の好み
    for r in range(1, N + 1):
        b = int(input())
        rank[g][b] = r
    boy[g] = 0
    rank[g][0] = N + 1  # 番人
for b in range(1, N + 1):   # 各男性の好み
    for r in range(1, N + 1):
        girl[b][r] = int(input())
    position[b] = 0
for b in range(1, N + 1):
    s = b
    while s != 0:
        position[s] += 1
        g = girl[s][position[s]]
        if rank[g][s] < rank[g][boy[g]]:
            boy[g], s = s, boy[g]
for g in range(1, N + 1):
    print('女 %d - 男 %d' % (g, boy[g]))