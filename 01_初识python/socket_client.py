import socket

socket_client = socket.socket()
socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入发送给服务端的信息:\n")
    if msg == 'exit':
        break
    socket_client.send(msg.encode(encoding="UTF-8"))

    recv_data = socket_client.recv(1024)
    print(f"接受服务器的消息是{recv_data.decode(encoding='UTF-8')}\n")

socket_client.close()
