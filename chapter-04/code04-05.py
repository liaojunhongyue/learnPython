age = input('请输入你的年龄：')

if age.isdigit():
    age = int(age)
    if age >= 0 and age <= 120:
        print('输入正确')
    else:
        print('输入错误')
else:
    print('请输入阿拉伯数字！')
    