import threading
from time import ctime, sleep


def super_player(_file, _time):
    for i in range(2):
        print('Start playing: {}, {}'.format(_file, ctime()))
        sleep(_time)


dicts = {'love.mp3': 1, 'like.mp4': 3, 'hate.mp5': 5}
threads = []

for file, time in dicts.items():
    t = threading.Thread(target=super_player, args=(file, time))
    threads.append(t)

f = range(len(threads))

if __name__ == '__main__':
    for i in f:
        threads[i].start()
    for i in f:
        threads[i].join()

    print('All over {}'.format(ctime()))