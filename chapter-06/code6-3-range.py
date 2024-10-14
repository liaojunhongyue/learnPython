# range(start, end ,step)
print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 3)))

# 水仙花数：三位数，每一位数字的立方和 = 三位数本身
for i in range(100, 1000):
    a = i % 10  # 个位
    b = i % 100 // 10  # 十位
    c = i // 100 # 百位
    if a**3 + b**3 + c**3 == i:
        print(i)