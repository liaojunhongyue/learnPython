# 纸的厚度
n = 0.1
w = n
for i in range(50):
    w *= 2
    print(w)

# 国王麦粒
# 1:1 2:2 3:4 4:8
g = 1  # 当前格子应该放的麦子粒
total = 0  # 总麦粒数
a = 1  # 棋盘的格子数量
while a <= 100:
    total += g
    print('在放满了%d个格子以后，总的麦粒数是%d' % (a, total))
    a += 1
    g *= 2

# 人生的复利（1+0.01）= 1.01
day = 0
total = 1
while day < 365:
    total = total * 1.01
    print(total)
    day += 1
