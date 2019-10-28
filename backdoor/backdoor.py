from socket import *
import socket

UDP_IP = "255.255.255.255"
UDP_PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

try:
	while(True):
		msg = input("#>")
		s.sendto(msg.encode(), (UDP_IP, UDP_PORT))	
except:	
	pass

