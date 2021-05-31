# portfinder

A simple port scanner coded in Python.

## Downloading

Download and extract the portfinder.sh file.

```bash
git clone https://github.com/DPrasoon/portfinder.git
```

## Usage

Enter the target IP address as argument.

Example -
```bash
root@kali:~/Desktop/ python3 portfinder.py 10.10.10.10
```

## Working

This script scans the ports of target and returns the port number if it is open.

## Used Modules & Functions

### Module (i) - sys

* **sys.argv** - used to input arguments from user
* **sys.exit()** - to exit the program

### Module (ii) - socket

* **socket.gethostname()** - used to resolve DNS
* **socket.AF_INET** - to get IPv4
* **socket.SOCK_STREAM** - to set up connection oriented TCP connection
* **socket.getdefaulttimeout()** - to set time-out for terminating a connection
* **connect_ex()** -  to indicate if connection was successful or not
* **close()** - to terminate the connection with the port
* **socket.gaierror** - DNS couldn't be resolved
* **socket.error** - errors related to system or connection or I/O

### Module (iii) - datetime
* **datetime.now()** - to print current time and date

### Default Modules
* **if...else** - to check *if* and *else* conditions
* **print** - to print output
* **try...catch** - blocks to catch exceptions
* **KeyboardInterrupt** - Interruption made by user

## Developed by
Git - [DPrasoon](https://github.com/DPrasoon) (Suggestions and improvements are appreciated)
