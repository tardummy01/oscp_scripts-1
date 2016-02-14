import socket 	#Imports socket library used for networking functions https://docs.python.org/2/library/socket.html?highlight=socket#module-socket
import os 		#Imports OS library used for interacting with misc operating system interfaces https://docs.python.org/2/library/os.html?highlight=os#module-os
import sys 		#IMports sys library used for interacting with system specific parameters and funcitons https://docs.python.org/2/library/sys.html?highlight=sys#module-sys
def retBanner(ip, port): 				#defines function for returning a banner from a website (to detect vuln)
	try:
		socket.setdefaulttimeout(2) 	#Sets default timeout in seconds
		s = socket.socket()				#creates new socket 's'
		s.connect((ip, port)) 			#connects to socket using IP and Port input
		banner = s.recv(1024) 			#creates banner variable of 1024 bytes based on data recieved from socket. 
		return banner 					#returns banner variable. 
	except:
		print "[-] Error, no Socket Connection on supplied IP and Port possible"
def checkVulns(banner, filename):		#defines function for checking for a vulnerabiity based on the input of a banner text and a file containing a list of vulns
	f = open(filename, 'r')				#creates variable representing file, using open function with read modifier.
	for line in f.readlines():			#reads all lines of file. Confirms line is not end of file. (All lines read by readlines contain '\n' unless it is EOF, even if blank)
		if line.strip('\n') in banner: 	#Strips out new line character ('/n') in Vuln List and compares against banne input. 
		print  '[+] Server is vulnerable: ' +\
			banner.strip('\n')			#prints vulnerability server is vulnerable to. 
def main():
	#Error handling for file access
	if len(sys.argv) == 2:				#Checks CLI input (for two values)
		filename = sys.argv[1] 			#sets filename as first input.
		if not os.path.isfile(filename):#check if file exists
			print '[-] ' + filename +\
				' does not exist.'		#returns that searched for file does not exist
			exit(0)						#exits program
		if not os.access(filename, os.R_OK): #checks that file can be read using R_OK permission attempt. 
			print '[-]' + filename +\
				' access denied.'		#returns that searched for file does not exist
			exit(0)						#exits program
	else:
		#Successfuly file access
		print '[-] Usage: ' +str(sys.argv[0]) +\
		' <vuln filename>'				#Informational when user does not input correct amount of items. 
		exit(0)
		portList = [21,22,25,80,110,443]#defines basic port list
		for x in range (147,150):		#checks IP ranges between 147 and 150
				ip = '192.168.95.' + str(x)
				for port in portList:	#sets list
					banner = retBanner(ip,port) #returns banner value for input. 
					if banner:			#if banner function was successful do following.
						print '[+] ' + ip + ': ' + banner #Prints address and port
						checkVulns(banner,filename)
if __name__ == '__main__' :				#This is used to ensure if the module is imported, main is not run unless it is called directly. 
	main()






