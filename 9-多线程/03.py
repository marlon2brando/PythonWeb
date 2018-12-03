'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time
import _thread as thread

def loop1(in1):
    # ctime
    print('Start loop 1 a at:',time.ctime())
    print("我是参数：",in1)
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2(in2,in3):
    # ctime
    print('Start loop 2 a at:',time.ctime())
    print("我是参数：",in2,'和参数：',in3)
    time.sleep(2)
    print('End loop 2 at :',time.ctime())


def main():
    # 多线程去执行某个程序
    print("Staring at:",time.ctime())

    # start_new_threar(方法名,(参数列表))
    # 如果参数只有一个，第一个参数后面需要加 ',',必须是元祖格式
    thread.start_new_thread(loop1,('1',))
    thread.start_new_thread(loop2,('2','3'))

    # 没有等待的动作，直接执行完
    print("All done at :",time.ctime())


if __name__ == '__main__':
    main()

    # 加入等待的动作
    while True:
        time.sleep(1)