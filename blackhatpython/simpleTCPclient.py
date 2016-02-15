import socket #imports socket lib

target_host = "0.0.0.0"
target_port = 9999

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is an address family, represented by IP, Port. SOCK_STREAM is the socket type. (socket.socket takes [family[,type, [protocol]]] as arguement)

#connect the client
try:
	client.connect((target_host,target_port)) 
except: 
	print "Could not connect to host port combo"

#Send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Recieve response
response = client.recv(4096)

print response