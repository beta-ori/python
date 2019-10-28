import socket 

UDP_IP = "255.255.255.255"
UDP_PORT = 9999
  
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
  
try:                     
	
	print("Waiting for a file...")
	data, addr = sock.recvfrom(1024)
	print("Data is ready.")
	name = input("Enter file name: ")
	_file = open(name, "w")
	_file.write(data.decode())
	_file.close()
	print("Complete")
except:
	print("Closing...")
	

