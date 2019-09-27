import threading
import time
import random

# event = threading.Event()


def light():
    if not event.isSet():
        event.set()
    count = 0
    while True:
        if count < 10:
            print('--- Green Light On ---')
        elif count < 13:
            print('--- Yellow Light On ---')
        elif count < 20:
            if event.isSet():
                event.clear()
            print('--- Red Light On ---')
        else:
            count = 0
            event.set()
        time.sleep(1)
        count += 1


def car(n):
    while 1:
        time.sleep(random.randrange(3, 10))
        if event.isSet():
            print('Car {} is running...'.format(n))
        else:
            print('Car {} is waiting for the red light...'.format(n))
            event.wait()


if __name__ == '__main__':
    car_list = ['BMW', 'AUDI', 'DIAO', 'SANTANA']
    event = threading.Event()
    lights = threading.Thread(target=light)
    lights.start()
    for i in car_list:
        t = threading.Thread(target=car, args=(i,))
        t.start()

