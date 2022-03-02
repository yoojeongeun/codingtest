from datetime import datetime
from sys import stdin

num = int(stdin.readline())

for _ in range(num):
    temp = stdin.readline().strip().split(" ")
    deadline = list(map(int, temp[0].split("/")))
    submit = list(map(int, temp[1].split("/")))

    submit = datetime(deadline[2], submit[0], submit[1])
    deadline = datetime(deadline[2], deadline[0], deadline[1])
    o_submit = temp[1]

    day = (submit - deadline).days


    year = deadline.year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        year = 366
    else:
        year = 365

    if day == 0:
        print('SAME DAY')
    elif day >= -7 and day < 0:
        day = abs(day)
        if day == 1:
            print(o_submit + '/' + f'{deadline.year} IS {day} DAY PRIOR')
        else:
            print(o_submit + '/' + f'{deadline.year} IS {day} DAYS PRIOR')

    elif (year-day) <= 7:
        day = year - day
        if day == 1:
            print(o_submit + '/' + f'{deadline.year - 1} IS {day} DAY PRIOR')
        else:
            print(o_submit + '/' + f'{deadline.year - 1} IS {day} DAYS PRIOR')

    elif day <= 7 and day > 0:
        if day == 1:
            print(o_submit + '/' + f'{deadline.year} IS {day} DAY AFTER')
        else:
            print(o_submit + '/' + f'{deadline.year} IS {day} DAYS AFTER')

    elif (year + day) <= 7 :
        day = abs(year+day)
        if day == 1:
            print(o_submit + '/' + f'{deadline.year + 1} IS {day} DAY AFTER')
        else:
            print(o_submit + '/' + f'{deadline.year + 1} IS {day} DAYS AFTER')

    else:
        print('OUT OF RANGE')