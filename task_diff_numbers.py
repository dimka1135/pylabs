a = input()
b = 0
c = 0
for number in range(len(a)):
    if int(number) % 2 == 0:
        b += int(a[number])
    else:
        c += int(a[number])
print(b-c)