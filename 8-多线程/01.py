'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time


def loop1():
    # ctime
    print('Start loop 1 a at:',time.ctime())
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2():
    # ctime
    print('Start loop 2 a at:',time.ctime())
    time.sleep(4)
    print('End loop 2 at :',time.ctime())


def main():
    print("Staring at:",time.ctime())
    loop1()
    loop2()
    print("All done at :",time.ctime())


if __name__ == '__main__':
    main()