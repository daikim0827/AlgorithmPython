#######################################################
# 百五減算
#######################################################
print("1から100までの整数を1つ考えてください")
a = int(input("それを 3 で割った余り? "))
b = int(input("それを 5 で割った余り? "))
c = int(input("それを 7 で割った余り? "))
x = (70 * a + 21 * b + 15 * c) % 105
print("あなたの考えた数は %d でしょう!" % x)