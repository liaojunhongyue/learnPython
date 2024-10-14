# 题目要求：输入 2024-02-25，输出这一天是这一年的第多少天
date = input('请输入日期：').split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days[2] += 1

result = 0
for i in range(month):
    result += days[i]
result += day

print('这一天是这一年的第%d天' % result)
