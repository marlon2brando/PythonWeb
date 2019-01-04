import socket

def clientFun():

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "I Lover You"

    # 发送的消息必须是bytes
    data = text.encode()
    # 发送
    sock.sendto(data,("127.0.0.1",6789))

    # 接收
    data,addr = sock.recvfrom(200)

    # 解码
    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFun()