import decode_code
import coding_code


if __name__ == '__main__':
    item = """12345678901234567890"""
    for i in range(15):
        d = coding_code.coding_code(item)
        print(d)
    print(decode_code.decode_code(d))

