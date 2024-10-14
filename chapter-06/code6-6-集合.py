# 集合
# 集合的创建
s = set()
print(s, type(s))
s = {1, 2, 3, 4}
print(s, type(s))

# 类型转换
s = set([1, 2, 3])  # list --> set
print(s)
s = set((1, 2, 3))  # tuple --> set
print(s)
s = set('123')  # str --> set
print(s)
s = set({1: 'a', 'a': 2})  # dict --> set
print(s)

# 常用方法
# 成员运算符 in
print(1 in s)
# 长度 len
print(len(s))
# max,min
print(max({1, 2, 3, 4}))
print(min({1, 2, 3, 4}))
# del
# del s
# print(s)

print('------分隔符------')
# 集合的遍历
for i in s:
    print(i)

# 集合的常用方法
# 移除集合中的元素
s.remove('a')
print(s)
# 更新集合中的元素
s.update({2, 3, 4, 5, 6, 7, 6, 5})
print(s)
# 新增一个集合中的元素
s.add(9)
print(s)

# 交集 并集
s2 = {5, 6, 7, 8, 9}
# 交集
print(s & s2)
# 并集
print(s | s2)

# 列表去重
score = [80, 70, 60, 80, 70, 60, 40]
s = set(score)
print(s)
# 统计各个分数都有几个学生
d = {}
for i in s:
    t = score.count(i)
    d[i] = t
for k, v in d.items():
    print('得分为%d的学生有%d' % (k, v))