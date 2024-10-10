# while 循环
n = 0

while n < 5:
    print('Hello Python')
    n += 1  # 判断条件更新
    print(n)

# 高斯求和
m = 1
total = 0
while m < 101:
    total += m
    m += 1
print(total)

# 1!+2!+3!+n!
n = 1
sum = 0
while n <= 4:
    m = 1
    result = 1
    while m <= n:
        result *= m
        m += 1
    sum += result
    n += 1

print(sum)