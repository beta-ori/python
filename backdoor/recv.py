import socket 
import subprocess
from pynput.keyboard import Key, Controller
import time

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
			for i in data.decode():
				keyboard.press(i)
				time.sleep(0.1)
			if(data.decode() == 'bye'):
				break
			time.sleep(0.8)
except:
	print("Closing...")
	

