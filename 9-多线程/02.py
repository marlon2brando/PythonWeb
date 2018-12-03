'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time
import _thread as thread

def loop1():
    # ctime
    print('Start loop 1 a at:',time.ctime())
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2():
    # ctime
    print('Start loop 2 a at:',time.ctime())
    time.sleep(2)
    print('End loop 2 at :',time.ctime())


def main():
    # 多线程去执行某个程序
    print("Staring at:",time.ctime())

    # start_new_threar(方法名,(参数列表))
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())

    # 没有等待的动作，直接执行完
    print("All done at :",time.ctime())


if __name__ == '__main__':
    main()

    # 加入等待的动作
    while True:
        time.sleep(1)