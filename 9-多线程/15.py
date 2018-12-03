import threading
import time

semphore = threading.Semaphore(3)

def func():
    if semphore.acquire():
        for i in range(5):
            print(threading.current_thread().getName() + ' get semphore')
        time.sleep(15)
        semphore.release()
        print(threading.current_thread().getName() + 'release semphore')


for i in range(8):
    t1 = threading.Thread(target=func,args=())
    t1.start()


# if __name__ == '__main__':
#     pass