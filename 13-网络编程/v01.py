
import socket

def serverFunc():
    # 1 建立 socket
    # socket.AF_INET：使用 ipv4的协议
    # socket.SOCK_DGRAM：通信的方式，使用UDP协议的
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2 绑定ip地址和端口号port
    # 127.0.0.1 本地地址
    # 6789 端口
    # ip 地址是一个tuple类型（ip.port）
    addr = ("127.0.0.1",6789)
    sock.bind(addr)

    # 3 接收client消息
    # recvfrom接收返回值是一个tuple，前一项表示数据，厚一些表示地址
    # 多参数的函数式缓冲区的大小
    # r = sock.recvfrom(500)
    data,addr = sock.recvfrom(500)

    print(data)
    print(type(data))

    # 4 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode(默认utf8)
    text = data.decode()
    print(text)

    # 5 给对方反馈的消息
    rsp = "Ich hab keine Hunge"

    # 发送的数据需要编码成bytes格式
    # 编码成bytes格式，默认是 utf8
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print("Start Server ....")

    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)

    print("Ending Server ....")