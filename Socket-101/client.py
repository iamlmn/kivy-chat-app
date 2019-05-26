import socket
# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
HEADERSIZE=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(("localhost",1236))
''' Why buffer ? To fit a large message '''
while True:
	full_msg=''
	new_msg=True
	while True:
		msg=s.recv(16)
		if new_msg:
			print(f"New msg size : {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE])
			new_msg=False

		full_msg+=msg.decode("utf-8")

		if len(full_msg)-HEADERSIZE == msglen :
			print("Full message recieved")
			print(full_msg[HEADERSIZE:])
			new_msg=True
			full_msg=''

print(full_msg)