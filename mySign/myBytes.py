import binascii

str = 'nnnnn'

print(str.encode())

print(binascii.b2a_hex(str.encode()))

print(binascii.a2b_hex(b'6e6e6e6e6e'))

print(binascii.a2b_hex(b'6e6e6e6e6e').decode())
