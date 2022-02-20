# https://www.acmicpc.net/problem/1340
# 백준 1340

from sys import stdin

month_dict = {'January' : 1 ,'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5,
              'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10,
              'November' : 11, 'December' : 12}
day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

temp = stdin.readline().split()
month = month_dict[temp[0]] - 1
day = int(temp[1].rstrip(',')) - 1
year = int(temp[2])
time = list(map(int, temp[3].split(':')))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    day_li[1] += 1

tot_time = sum(day_li) * 60 * 24
cur_time = (sum(day_li[:month]) + day) * 60 * 24 + time[0] * 60 + time[1]


print(cur_time/tot_time * 100)