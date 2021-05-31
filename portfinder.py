#!/bin/python3/

import sys
import socket
from datetime import datetime

#Defining target

if len(sys.argv) == 2:
	try:
		target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPv4
	
	except socket.gaierror:			#DNS could not resolve it
		print("Hostname could not be resolved.")
		sys.exit()
else:
	print("Invalid number of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Banner

print("-" * 50)
print("Scanning target " +target)
print("Starting time: " +str(datetime.now()))
print("-" * 50)

try:
	for port in range(1, 65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #error indicator, 0 = open and 1 = closed
		if result == 0:
			print("Port {} is open.".format(port))
		s.close()
	print("-"* 50)
	print("Ending time: " +str(datetime.now()))

except KeyboardInterrupt:		#Ctrl-C
	print("\nUser Interrupt detected! Exiting program.")
	sys.exit()


except socket.error:			#Can't connect to DNS
	print("Couldn't connect to server.")
	sys.exit()
