# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程

- 程序：一对代码以文本形式存入文档

- 进程：程序运行的一个状态
   - 包含地址空间，内存，数据栈等
   - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题

- 线程：一个进程的独立运行片段，一个进程可以由多个线程
   - 轻量化的进程
   - 一个进程的多个线程之间共享数据和上下文运行环境
   - 共享的互斥问题

- 全局解释器（GIL）
   - Python 代码的执行是由Python虚拟机进行控制
   - 在主循环中只能有一个控制线程在执行

- Python 包
   - thread: 有问题，不好用，python3改成 _thread
   - threading:通行的包

- 案例 01，顺序执行，耗时较长
- 案例 02，改用多线程，缩短总时间，使用 _thread
- 案例 03，多线程，传参数

- threading的使用

   - 直接利用threading.Thread生成Thread实例
      1. t = threading.Thread(target=xxx,args=(xxx,))
      2. t.start()  启动多线程
      3. t.join()  等待多线程执行完成
      4. 案例04
      5. 案例04 加入join后比较案例05的区别

   - 守护线程-daemon
      - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束之后自动结束
      - 一般认为，守护线程不重要或者不允许离开主线程独立运行
      - 守护线程案例能否有效果跟环境有关
      - 案例06 非守护
      - 案例07 守护

   - 线程的常用属性
      - threading.currentThread:返回当前线程
      - threading.enumerate: 返回一个包含正在运行的线程的list
      - threading.activeCount: 正在运行的线程数量
      - thr.setName() 给线程起名字
      - thr.getName() 得到线程的名字
      - 案例 08

   - 直接继承自 threading.Thread
      - 直接继承Thread
      - 重新run函数
      - 案例09
      - 案例10 - 工业化代码

- 共享变量：多个线程同时访问同一个变量的时候，会产生共享变量的问题
   - 案例 11
   - 解决办法：锁，信号灯，
   - 锁（Lock）
      - 是一个标志，表示一个线程在占用一些资源
      - 使用方法：
         - 上锁
         - 使用共享资源，放心的用
         - 取消锁，释放锁
      - 案例 12
      - 锁谁：哪个资源需要多个资源共享，锁那个
      - 理解锁：锁不一定是锁住谁，而是一个令牌

   - 线程安全问题：
      - 如果一个资源/变量 他对与多线程来讲，不用加锁，也不会引起任何问题，则成线程安全的
      - 线程不安全变量的类型，list,set,dict
      - 线程安全的变量的类型，queue

   - 生产者，消费者问题
      - 一个模型，可以用来搭建消息队列
      - queue 是一个用来存放变变量的数据结构，特点是先进先出，内部元素排对，可以理解成一个特殊的list

   - 死锁问题
      - 案例14

   - 锁的等待时间：lcok.acquare(3)

   - semphore
      - 允许一个资源最多由几个线程同时使用
      - 案例15

   - threading.Timer
      - 在指定的秒数之后调用某一个函数
      - Timer是利用多线程，在指定时间后启动一个功能
      - 案例16

   - 可重入锁
      - 一个锁，可以被一个线程多次申请
      - 主要解决递归调用的时候，需要申请锁的情况
      - 案例 17

# 线程替代方案
- subprocess
   - 完全跳过线程，使用进程
   - 是派生进程的主要替代方案
   - python2.4 以后引入的

- multiprocessing
   - 使用threading的接口派生的，使用子进程
   - 允许为多核或者多CPU派生进程，接口跟threading非常相似

- concurrent.futures
   - 新的异步执行模块
   - 任务级别的操作
   - python 3.2以后引入的

# 多进程
- 进程间的通讯(interprecess Communication,IPC)
- 进程之间无任何共享状态
- 进程的创建
   - 直接生产Process的实例对象 案例18
   - 生产派生的Process对象 案例 19

- 在os 中查看 pid，ppid 以及他们的关系
   - 案例 20

- 生产者消费者模型
   - JoinableQueue
   - 案例21
