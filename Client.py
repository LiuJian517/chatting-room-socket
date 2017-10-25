import socket
import time
import threading

socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = socket_socket
sock.connect(('localhost', 5550))
sock.send(b'1')
print(sock.recv(1024).decode())

nickName = input('input your nickname: ')
sock.send(nickName.encode())


def sendThreadFunc():
    while True:
        try:
            myword = input()
            sock.send(myword.encode())
            # print(sock.recv(1024).decode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')


def recvThreadFunc():
    while True:
        try:
            otherword = sock.recv(1024)
            if otherword:
                print(otherword.decode())
            else:
                pass
        except ConnectionAbortedError:
            print('Server closed this connection!')

        except ConnectionResetError:
            print('Server is closed!')


th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
th1.start()
th2.start()
th1.join()
th2.join()

'''
threads = [th1, th2]
for t in threads:
    t.setDaemon(True)
    t.start()

print(t)
# <Thread(Thread-2, started daemon 14568)>

# 把下面这行注释掉就会出错！！！
t.join()
'''