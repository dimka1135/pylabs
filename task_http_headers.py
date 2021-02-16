import json


def return_cv(a, v):
    if type(a) is not list:
        lst = a, v
        a = list(lst)
    else:
        a.append(v)
    return a


def line_to_dict(lines):
    a = {}
    for line in lines:
        if line == '\n':
            continue
        elif line[0:6] == 'HTTP/2':
            a.update({'protocol': 'HTTP/2', 'status_code': line.split()[1]})
        elif line[0:6] == 'HTTP/1':
            a.update({'protocol': line.split()[0], 'status_code': line.split()[1],
                          'status_message': ' '.join(line.split()[2:])})
        elif 'POST' in line[0:4] or 'GET' in line[0:4]:
            a.update({'method': line.split()[0], 'uri': line.split()[1],
                          'protocol': line.split()[2]})
        else:
            if len(line.split(': ')) > 1:
                key, value = line.split(': ')
            else:
                key, value = line.split(': ') + [' ']
            if value.endswith("\n"):
                value = value[:-1]
            if a.get(key):
                a[key] = return_cv(a[key], value)
            else:
                a.update({key: value})
    return a


def http_headers_to_json(path_to_http_headers, path_to_result_json):
    json_result = {}
    with open(path_to_http_headers) as f:
        json_result = line_to_dict(f)

    with open(path_to_result_json, 'w') as f:
        json.dump(json_result, f)