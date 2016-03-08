import sys #system specific parameters and functions https://docs.python.org/2/library/sys.html
import socket #low level netowrking interface https://docs.python.org/2/library/socket.html?highlight=socket#module-socket
import getopt #C style parser for command line options https://docs.python.org/2/library/getopt.html?highlight=getopt#module-getopt (look at argparse as replacement https://docs.python.org/2/library/argparse.html#module-argparse)
import threading #higher level threading interface https://docs.python.org/2/library/threading.html?highlight=threading#module-threading
import subprocess #subprocess management - used to spawn processes, conenct to input/output/error pipes, and get return codes: https://docs.python.org/2/library/argparse.html#module-argparse

# Define Global Variables
listen				= False
command				= False
upload				= False
execute				= ""
target				= ""
upload_destination 	= ""
port				= 0


def usage():	#Shows runtime rules
		print "BHP Net Tool"
		print
		print "Usage: bhpnet.py -t target_host -p port"
		print "-l --listen - listen on [host]:[port] for incoming connections"
 		print "-e --execute=file_to_run - execute the given file upon receiving a connection"
 		print "-c --command - initialize a command shell"
 		print "-u --upload=destination - upon receiving connection upload a file and write to [destination]"
 		print
 		print
 		print "Examples: "
 		print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
 		print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
 		print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
 		print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
 		sys.exit(0)


def main():
	global listen
	global port
	global execute
	global command
	global upload_destination
	global target

	if not len(sys.argv[1:]):	#If input does not have at least one input, show help message usage()
			usage()

	#read commandline options (assigns input leters to array argv)
	try:
		opts, args = getopt.getopt(sys:argv[1:], "hle:t:p:cu:", ["help","listen","execute","target","port","command","upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts: 
			if o in ("-h","--help"):