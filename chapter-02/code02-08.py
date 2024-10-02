# 数据类型的转换
# 转换为整数int
# 字符串str-->int
s = '2024'
n = int(s)
print(type(s), type(n))
s1 = 2.23
print(int(s1))
# 布尔值-->int
s2, s3 = True, False
print(int(s2), int(s3))
# 转换为浮点数
# str-->float
print(float(s))
# bool-->float
print(int(s2), int(s3))
# 进制的转换
s4 = '10'
print(int(s4, 2))
