import time
import random
a = 20
b = 20

while True:
    lost = random.randint(2, 5)
    a = a - lost
    print('A lost {}, remaining {}'.format(lost, a))
    if a <= 0:
        print('A is failed')
        break
    time.sleep(0.1)
    lost = random.randint(2, 5)
    b = b - lost
    print('B lost {}, remaining {}'.format(lost, b))
    if b <= 0:
        print('B is failed')
        break
    time.sleep(0.1)
