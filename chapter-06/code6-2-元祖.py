# 元祖
# 元祖的创建
# 元祖的简单创建
tuple1 = (1, 2, 3, True, 'Hello')
print(tuple1)
print(type(tuple1))
# 创建单一元素的元祖
tuple2 = (1,)
print(tuple2)
print(type(tuple2))
# 创建空元素的元祖
tuple3 = tuple()
print(tuple3)
print(type(tuple3))
tuple4 = ()
print(tuple4)
print(type(tuple4))

# tuple 的类型转换
# 将字符串转换成 tuple
tuple5 = tuple('hello')
print(tuple5)
# 将列表转换成 tuple
tuple6 = tuple([1, 2, 3, 4])
print(tuple6)
# 将 tuple 转换成列表
list1 = list(tuple6)
print(list1)
# 将 tuple 转换成字符串
str1 = str(tuple6)
print(str1)
print(type(str1))
print(str1[2])

print('------分割线------')
# 元祖的通用方法
# tuple1 = (1, 2, 3, True, 'Hello')
# 索引
print(tuple1[-1])
# 切片
print(tuple1[::-1])
# len
print(len(tuple1))
# max,min
print(max(tuple6), min(tuple6))
# del
del tuple5
# print(tuple5)  # 报错
# 加法 +
print(tuple1 + tuple6)
# 乘法 *
print(tuple1 * 3)
# 成员运算符 in
print(1 in tuple1)

# 修改列表中的元素
print(list1)
list1[2] = 5
print(list1)
# 修改 tuple 中的元素会报错
# tuple1[1] = 4
# print(tuple1)

# 元祖的常用方法
# 元素的计数 count()
a = tuple1.count('Hello')
print(a)
# 根据索引查找元素 index()
b = tuple1.index('Hello')
print(b)

print('------分割线------')
# 遍历元祖的每一项
for i in tuple1:
    print(i)
# 遍历元祖的索引和每一项的值
for index, value in enumerate(tuple1):
    print(index, value)
# 用 range 方法进行遍历
for i in range(len(tuple1)):
    print(i, tuple1[i])