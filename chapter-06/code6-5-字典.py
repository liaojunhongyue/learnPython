# 字典
# 字典的创建
d = {
    'name': 'mia',  # 键值对
    'gender': False
}
print(d)
print(type(d))
# # 空字典的创建
# d = {}
# print(d)
# print(type(d))
# # 使用 dict() 进行创建
# d = dict()
# print(d, type(d))

# 字典获取键值对
print(d['name'])
# 字典新增键值对
d['height'] = 170
print(d['height'])
# 字典修改键值对
d['gender'] = True
print(d['gender'])

# 删除字典
# del d
# print(d)

# 成员运算符 in
print('name' in d)
print('age' in d)

# 字典的遍历
# 遍历字典的key和value
for k, v in d.items():
    print(k, v)
# 遍历字典的key
for k in d.keys():
    print(k)
# 遍历字典的value
for v in d.values():
    print(v)

print('------分割线------')
print(d)
# 字典的常用方法
# 删除字典的某个key
d.pop('name')
print(d)
# 复制字典
a = d.copy()
print('a的键值对', a)
# 获取字典某个键对应的值
print(d.get('gender'))
# 从末尾删除字典的键值对，每次删除一个
d.popitem()
print(d)
d.popitem()
print(d)
# 字典的更新
d.update({'age': 18})
print(d)
# 清空字典
d.clear()
print(d)
