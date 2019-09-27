import hashlib


def my_md5(string):
    h = hashlib.md5()
    h.update(string.encode(encoding='utf-8'))
    return h.hexdigest()


