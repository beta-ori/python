from socket import *
import socket

UDP_IP = "255.255.255.255"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

try:
	path = input("\nEnter the path of the file: ")
	try:
		_file = open(path)
		msg = _file.read()
		try:
			print("Broadcasting the file...")
			print("Press CTRL+C to stop.")
			while(True):
				sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
		except:
			pass
					
				
		_file.close();
	except:
		print("Having problem. Make sure the file exists.")
except:
	print("Closing...");

	

