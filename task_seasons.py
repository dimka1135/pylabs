variable = {
    (1, 2, 12) : "winter",
    (3, 4, 5) : 'spring',
    (6, 7, 8) : 'summer',
    (9, 10, 11) : 'autumn'
}
a = input()
if a.isdigit():
        a = int(a)
for key, value in variable.items():
    if a in key:
        print(value)