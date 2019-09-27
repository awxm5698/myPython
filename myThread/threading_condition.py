import threading
import time


def seeker(cond, name):
    time.sleep(2)
    cond.acquire()   # 2.seeker 获取线程锁
    print('2.seeker 获取线程锁')
    print('{}:我已经把眼睛蒙上了！'.format(name))
    cond.notify()    # 3.seeker 通知hider线程
    print('3.seeker 通知hider线程/挂起')
    cond.wait()    # 3.seeker 挂起/ 6.seeker 激活
    print('6.seeker 激活')
    for i in range(3):
        print('{} is finding'.format(name))
        time.sleep(2)
    cond.notify()    # 7.seeker 通知hider线程
    print('7.seeker 通知hider线程/释放')
    cond.release()   # 7.seeker 释放线程锁
    print('7.seeker 释放线程锁')
    print('{} : 找到你了，我赢了！'.format(name))


def hider(cond, name):
    cond.acquire()    # 1.hider 获取线程锁
    print('1.hider 获取线程锁/挂起')
    cond.wait()    # 1.hider 挂起/ 4.hider 激活
    print('4.hider 激活')
    for i in range(2):
        print('{} is hiding!'.format(name))
        time.sleep(3)
    print('{}: 我已经藏好了，快来找我吧！'.format(name))
    cond.notify()    # 5.hider 通知seeker线程
    print('5.hider 通知seeker线程/激活seeker/挂起hider')
    cond.wait()    # 6. hider 挂起/ 7.hider 激活
    print('7.hider 激活/释放')
    cond.release()    # 8. hider 释放线程锁
    print('8. hider 释放线程锁')
    print('{}:被你找到了，唉~^~'.format(name))


if __name__ == '__main__':
    cod = threading.Condition()
    s = threading.Thread(target=seeker, args=(cod, 'seeker'))
    h = threading.Thread(target=hider, args=(cod, 'hider'))
    s.start()
    h.start()

