import socket #imports socket lib

target_host = "0.0.0.0"
target_port = 9999

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET is an address family, represented by IP, Port. SOCK_DGRAM is the socket type (UDP)

#Send data (this is connectionless, so no conenction is required)
client.sendto("AAABBBCCC",(target_host,target_port))

#Recieve data
data, addr = client.recvfrom(4096)

print data