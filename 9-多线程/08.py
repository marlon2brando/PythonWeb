
import time
import threading

def loop1():
    # ctime
    print('Start loop 1 a at:',time.ctime())
    time.sleep(5)
    print('End loop 1 at :',time.ctime())

def loop2():
    # ctime
    print('Start loop 2 a at:',time.ctime())
    time.sleep(2)
    print('End loop 2 at :',time.ctime())

def loop3():
    # ctime
    print('Start loop 3 a at:',time.ctime())
    time.sleep(5)
    print('End loop 3 at :',time.ctime())

def main():
    print("Staring at:",time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    t1.setName('Thr_01')
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName('Thr_02')
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName('Thr_03')
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是：{0}".format(thr.getName()))
    print("正在运行的子线程数量是 {0}".format(threading.activeCount()))

    print("All done at :",time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
