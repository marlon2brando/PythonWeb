import multiprocessing
from time import sleep,ctime


def comsumer(input_q):
    print('Into cumsumer:',ctime())

    while True:
        item = input_q.get()
        print("pull ",item,' out of q')
        input_q.task_done()
    print('Out of comsumer:',ctime())

def producer(sequence,output_q):
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)
        print("Put ",item,'into q')
    print("Out pf producer:",ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    cons_p = multiprocessing.Process(target=comsumer,args=(q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)
    q.join()

