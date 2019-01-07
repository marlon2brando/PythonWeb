
# 网络编程
- 网络:
- 网络协议: 一套规则
- 网络模型:
   - 七层模型
      - 物理层
      - 数据链路层
      - 网络层
      - 传输层
      - 会话层
      - 表示层
      - 应用层
   - 四层模型-实际应用
      - 链路层
      - 网络层
      - 传输层
      - 应用层

- 每一层都有相应的协议负责交换信息或者协调工作
- TCP/IP 协议簇
- IP地址：负责在网络上唯一定位一个网络地址（物理网卡和虚拟网卡各有一个ip，一台机器有一个mac地址）
   - IP地址分为五类 ABCDE类
   - IPv4 是由四个数字段组成，每个数字字段的取值是 0-255
   - 192.168.xxx.xxx :局域网的ip
   - 127.0.0.1：本机
   - IPv4,IPv6

- 端口：应用的标识
     - 范围：0-65535
        - 知名的端口：0-1023 ，一般是系统用的服务端口
           - 80：http
           - ...
        - 非知名的端口：1024-65535，用户使用的端口

# TCP/UDP 协议和 socket通信
- UDP:非安全的不面向链接的传输
  - 安全性差
  - 大小限制 64kb
  - 没有顺序
  - 速度快

- TCP:基于链接的通信

- SOCKET：套接字通信
  - socket;一个网络通信的端对端的通信协议
  - 通过ip+端口定位对方并发送消息的通信机制
  - 分为两种 UDP和TCP：
     - udp: 即时通讯一般用udp
  - 客户端 Client:发起访问的一方
  - 服务器端 Server：接收访问的一方

- UDP编程
   - Server端程序，
      1. 建立socket，socket是负责具体通信的一个实例
      2. 绑定，为创建socket指派固定的端口和ip地址
      3. 接收对方的内容
      4. 给对方发送反馈，

   - Client端程序

   - 服务器程序

- TCP编程
   - 面向链接的传输，即每次传输之前，需要先建立一个链接
   - 客户端和服务端两个程序需要编写
   - Server端的编写流程
      1. 建立socket通道
      2. 绑定ip和port
      3. 监听接入的访问 socket
      4.

- FTP 编程
- FTP: FileTransformProtocal 文件传输协议
- 用途：定制一些特殊的上传下载文件的服务
- 用户分类：登录FTP服务器必须有一个账户
   - Real账户：注册账户
   - Guest账户：可能临时对某一类人的行为进行授权
   - Anonymous账户：匿名账户，允许任何人

- FTP工作流程
   - FTP服务器一般是21号端口接收请求
   - FTP使用20端口发送请求

   1. 客户端连接远程主机上的FTP服务器
   2. 客户端输入用户名和密码（或者''anonymous'和电子邮件地址）
   3. 客户端和服务器进行各种文件传输和信息查询操作
   4. 客户端和远程FTP服务器退出，结束传输

- FTP 文件表示
   - 分三段表示FTP服务器的文件
   - HOST：主机地址，类似于 ftp.mozilla.org, 以ftp开头
   - DIR:  目录，表示文件所在的本地路径，例如 pub/android/focus/1.9
   - FILE：文件名,表示文件名称
   - 如果想完整的精确表示ftp上某一个文件，需要上述三个部分组合在一起
   - 案例v06

# Mail 编程
## 电子邮件的历史
- 起源：
   - 1969 Leonard K. 教授发送同事的 'LO'
   - 1971 美国国防部的自主的阿帕网（Apranet）的通讯机制
   - 通讯地址里用 @ 符号
   - 1987年，中国的第一封第一份电子邮件
   "Across the Great Wall we can reach every corner in the world"

- 管理程序：
   - Euroda 使邮件普及
   - Netscape,outlook,foxmail,后来居上
   - HotMail 使用浏览器发送邮件

## 邮件工作流程
- MUA (MailUserAgent),邮件用户代理
- MTA (MailTransferAgent),邮件传输代理
- MDA (MailDeliverAgent),邮件传输代理

- laoshi@qq.com 老是给学生 （xuesheng@sina.com）发送一封邮件

- 编写程序：
   用户-> MUA -> MTA (一个或者若干个)... -> MDA -> 用户

    - 发送：MUA-> MTA with SMTP(simple mail transfer protocol)
    - 接收：MDA-> MUA with POP3 and IMAP(Post office protocol v3 and)

- Python for mail
   - SMTP协议负责发送邮件
      - 使用email模块构建一封邮件
         - 纯文本邮件 send_mail.py
         - HTML格式的邮件 send_html_mail.py
         - 发送带附件的邮件
         - 添加邮件头，抄送的等信息
            - mail["From"] 表示发送者的信息，包括姓名和邮件
            - mail["To"] 表示接收者信息，包括信息和邮件地址
            - mail["Subject"] 表示邮件的摘要

        - 使用smtplib模块发送邮件

   - POP3协议负责接收邮件

