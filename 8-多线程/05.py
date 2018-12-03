'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import threading

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

    t1 = threading.Thread(target=loop1,args=('王',))
    t1.start()

    t2 = threading.Thread(target=loop2,args=('老王','老李'))
    t2.start()


    # 加入等待动作
    # 将 t1和t2加入主线程
    t1.join()
    t2.join()

    # 所有线程执行完成之后，才执行下面这句话
    print("All done at :",time.ctime())


if __name__ == '__main__':
    main()

    # 加入等待的动作
    while True:
        time.sleep(10)