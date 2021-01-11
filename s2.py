import socket
import threading
import os

s = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)

ip = input("\n\tEnter your ip: ")
port = 1234

s.bind((ip,port))

sip = input("\n\tEnter server ip: ")
sport = 1234


print()
print()


def send():

  while True:
    os.system('tput setaf 5')
    msg = input('\n').encode()
    s.sendto(msg ,(sip,sport))
    if msg.decode == "exit":
      os.system('exit')


def recv():

  while True:
    os.system('tput setaf 2')
    msg = s.recvfrom(1024)
    print("\n\t\t\t=>"  + msg[0].decode())

  



x1 = threading.Thread(target=send)
x2 = threading.Thread(target=recv)

x1.start()
x2.start()
    
