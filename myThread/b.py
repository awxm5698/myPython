import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print('Listening {}, {}'.format(func, ctime()))
        sleep(4)


def move(func):
    for i in range(2):
        print('See {}, {}'.format(func, ctime()))
        sleep(5)


def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print('something error!')


threads = []
m_list = ['love.mp3', 'loves.mp4']
files = range(len(m_list))
for i in files:
    t = threading.Thread(target=player,args=(m_list[i],))
    threads.append(t)

if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print('All over {}'.format(ctime()))
