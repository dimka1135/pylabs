a = int(input())
day = 0
month = 0
for i in range(1, 13):
    if (a - i) % 50 == 0:
        month += i
        day += ((a - i) // 50 - 5) / 2
        day = int(day)
print(day, month)