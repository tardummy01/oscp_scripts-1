import socket #Used for network info
import sys
import subprocess #used to call shell commands  (e.g using Popen)
import time


RHOST = socket.gethostbyname(socket.gethostname()) #Checks and returns host IP 

reportfile = open("Target:" + RHOST + "_Date:"+ time.strftime("%d_%m_%Y@%H:%M:%S"), 'w')
sys.stdout = reportfile

output = subprocess.Popen(["ls", "-l"], shell=True)


print "Running Enumeration Scan"
print
print "Getting RHOST IP Address"	
print "IP: "+RHOST
