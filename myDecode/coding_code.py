import random


def get_default_code():
    code = []
    for i in range(33, 127):
        code.append(chr(i))
    random.shuffle(code)
    return code


def coding_code(item):
    if len(item) > 30:
        return 'The max length is 30'
    else:
        item = str(item).ljust(30, '#')
    code = get_default_code()
    key = abs(abs(ord(code[-1]) - ord(code[-2])) - 9)
    new_item = []
    coding_codes = []
    for _item in item:
        if _item == ' ':
            _item = '_'
        new_item.append(_item)
    for i in range(len(new_item)):
        for j in range(len(code)):
            if new_item[i] == code[j]:
                n = i*(i+2)+j+int(key)
                if n >= len(code):
                    n = n % len(code)
                coding_codes.append(code[n])
    return ''.join(coding_codes)+''.join(code)


