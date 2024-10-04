# 与，并且 and
print(True and False)
print(True and True)
print(True and False and True)
print(1 == 1 and True and 2 < 3)
print('hello' and 'hi')  # 短路运算，整个式子的值，依赖后面的值，整个结果会返回后面表达式的值
print('' and 'hi')  # 前面表达式为False，则整个式子的值会依赖前面表达式的值
print(0 and 1)
# 或者or
print(True or False)
print(False or False or True)
print(1 or 0)
print(2024 or 2025 or 0)
print(0 or '' or 888)
# 非not
print(not True)
print(not 1)
print(not '')
# 优先级 not>and>or
print(True and False and not False)
print(True or False and True or False)




