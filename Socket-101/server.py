import socket
import time
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HEADERSIZE=10
#host = socket.gethostbyname(socket.gethostname())
host="localhost"
port_number=1236
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.bind((host,port_number))
s.listen(5)
iterations=1
while True:
	clientsocket,address=s.accept()
	print(f"Connection from {address} has been established!")
	
	msg="Welcome to the server"
	msg=f"{len(msg):<{HEADERSIZE}}"+ msg

	clientsocket.send(bytes(msg,"utf-8"))
	#clientsocket.close() # not required if we are using buffering

	while iterations < 10 :
		time.sleep(2)
		msg = f"The time is {time.time()}"
		msg = f"{len(msg):<{HEADERSIZE}}"+msg
		iterations +=1
		print (msg)
		clientsocket.send(bytes(msg,"utf-8"))