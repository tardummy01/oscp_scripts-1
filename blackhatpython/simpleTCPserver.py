import socket
import threading

bind_ip = "0.0.0.0" 	#Bind IP to local variable for localhost
bind_port = 9999 		#Bind to port not in common usage. 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port)) #Will bind to a socket. Socket must not be in use (add try/exception error messages later)

server.listen(5) #Sets up  socket listerner to listen for connections. 5 is (backlog), the number of allowed queued connections. 

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#client-handling thread code
def handle_client(client_socket):

	#print out what the client sends
	request = client_socket.recv(1024) #reads input

	print "[*] Received: %s" % request #prints input

	#Send back a packet
	client_socket.send("ACK!")	#tells client message is recieved

	client_socket.close()	#close connection. 

while True:	#starts threading for client requests.

	client,addr = server.accept()	# this accepts the client socket into 'client' and the remote ip/port from address. This is based on socket.accept(conn,address)

	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1]) #prints connection ip and port

	#spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))  #This creates a thread object of client_handler. target is the callable object to be invoked by the run() method. args is the argument tuple for the target invocation. 
	client_handler.start() #starts thread activity. 