# break 在 while 循环中的用法
n = 5
while n > 0:
    if n == 3:
        break
    print(n)
    n -= 1

# 判断一个数字是否是质数
m = 5
a = 2
while a < m:
    if m % a == 0:
        print(m, '不是质数')
        break
    a += 1
else:
    print(m, '是质数')

for i in range(2, m):
    if m % i == 0:
        print(m, '不是质数')
        break
else:
    print(m, '是质数')
