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