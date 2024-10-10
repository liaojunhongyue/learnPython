# m行n列*号矩阵
m = 4  # 控制的行
n = 5  # 控制的列
for i in range(m):
    print('*' * n)

print('----------分割线----------')

# 打印n行的等腰三角形
n = 10  # 行数
for i in range(n):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1))

print('----------分割线----------')

# 穷举
peach = 1

while True:
    d1 = peach // 2 - 1
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1
    if d3 == 1:
        print(peach)
        break
    peach += 1
