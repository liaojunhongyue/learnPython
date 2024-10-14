# 列表的创建
# 创建空列表
list1 = []
print(list1)
print(type(list1))

# 创建一个有元素的列表
list2 = [1, 2, 3, True, False, 'hello']
print(list2)

# 使用 list() 创建列表
list3 = list()
print(list3)
list4 = list('12345678')
print(list4)

list5 = ['1', '2', '3', '4', '5', '6', '7', '8']
# 列表的索引
print(list5[1])

# 列表的切片操作
print(list5[2:6:2])

# 列表的加法和乘法
print(list5 + list2)
print(3 * list5)

# 列表的成员运算
print('1' not in list5)
print('1' in [1, 2, 3, 4])

# 内置函数
print(len(list5))  # 元素的个数
print(max(list5))  # 元素的最大值
print(min(list5))  # 元素的最小值

# 列表的遍历
for i in list2:
    print(i)
for i, j in enumerate(list2):
    print(i, j)
for i in range(len(list2)):
    print(i, list2[i])

print('------分隔符------')
# 列表的常用方法 变量.方法名()
# append() 在list末尾增加元素
list5.append('666')
print(list5)
# extend() 在list末尾添加列别
list5.extend([1, 2, 3])
print(list5)
# insert(index, object) 在相应索引位置插入元素
list5.insert(2, 'Hello')
print(list5)
# pop(index) 根据索引来删除元素
list5.pop(3)
print(list5)
# remove(value) 根据元素进行删除，如果两个元素相同，则删除第一个找到的元素
list5.remove('7')
print(list5)
list5.append('Hello')
print(list5)
list5.remove('Hello')
print(list5)
# clear() 清空列表
list5.clear()
print(list5)

# 计算若干个人的平均年龄
age = [10, 20, 30, 40, 23, 45]
total = 0
for i in age:
    total += i
average = total / len(age)
print(average)
print(sum(age)/len(age))
print(sum(age))



