

def decode_code(item):
    code = []
    code_chr = []
    for _item in item:
        code_chr.append(ord(_item))
    code_len = max(code_chr) - min(code_chr) + 1
    for _item in item[-code_len:]:
        code.append(_item)
    key = abs(abs(ord(code[-1]) - ord(code[-2])) - 9)
    new_item = []
    decode_codes = []
    if len(code) == len(item):
        return ''.join(decode_codes)
    for _item in item:
        new_item.append(_item)
    for i in range(len(new_item)-code_len):
        for j in range(len(code)):
            if new_item[i] == code[j]:
                n = j - i*(i+2) - key
                if n <= 0:
                    n = len(code) + n
                if abs(n) >= len(code):
                    n = n % len(code)
                decode_codes.append(code[n])
    return ''.join(decode_codes).replace('_', ' ')
