s1 = 'hello world'

# 序列的通用操作
print(s1 + ' mia')
print(s1 * 3)
print(len(s1))
print(max(s1), min(s1))
# del s1
# print(s1)
print('s' in s1)
print('abcd' < 'abce')
print('cd' < 'abcd')

# 字符串的遍历
for i in s1:
    print(i)
for value, index in enumerate(s1):
    print(value, index)
for i in range(len(s1)):
    print(i, s1[i])

# 类型转换
print(str(12), type(str(12)))  # int --> str
print(str([1, 2, 3, 4]), type(str([1, 2, 3, 4])))  # list --> str
print(str((1,)), type(str(1,)))  # tuple --> str

# 常用方法
# 判断字符是否都是小写
print(s1.islower())
# 判断字符是否都是大写
print(s1.isupper())
# 查找元素的出现次数
print(s1.count('o'))
# 清空元素开头末尾的多余空格
print(s1.strip())
# 按照给定的元素分隔字符串
print(s1.split(' '))
# 查找元素相对应的索引
print(s1.find('o'))
# 从给定的索引位置查找元素相对应的索引
print(s1.find('o', 5))
# 查找不存在的元素时会返回-1
print(s1.find('a'))
# 用给定的字符串符号连接序列
print('#'.join(['111', '222', '333']))