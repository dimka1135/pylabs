a = ''
b = ''

n = int(input())
p = int(input())

with open('data.txt') as f:
    f = f.readline()
    for i in f.split(' '):
        if int(i) % n  == 0:
            a += f'{i} '
        b += f'{int(i) ** p} '
        
with open('out-1.txt', 'w') as f:
    f.writelines(a.strip())
    
with open('out-2.txt', 'w') as f:
    f.writelines(b.strip())