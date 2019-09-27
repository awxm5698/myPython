import random

# a = [1, 2]
# b = [3, 4]
# c = a + b
# s = random.sample(c, 2)
# c.append(5)

# print(c)
# print(s)

a = 60
d = ''
c = 0
for i in range(100):
    b = random.randint(0, 100)
    if b <= a:
        d = 'go'
        c = c+1
print(d)
print(c)
