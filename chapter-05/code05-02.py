# for 循环
for i in range(5):
    print('python')

print(list(range(10)))

# 高斯求和
total = 0
for i in range(101):
    total += i
print(total)

# 1!+2!+3!+n!
sum = 0
for n in range(5):
    if n > 0:
        result = 1
        for i in range(n + 1):
            if i > 0:
                result *= i
        print(result)
        sum += result

print(sum)
