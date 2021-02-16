def camel_to_snake(name):
    a = ''
    for i in name:
        if i.isupper():
            a += '_' + i.lower()
        else:
            a += i
    return a[1:]


def snake_to_camel(name):
    a = []
    for i in name.split('_'):
        a.append(i.capitalize())
    a = ''.join(a)
    return a