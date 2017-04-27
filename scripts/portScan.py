#!/usr/bin/env python3

port = 21 # an int

portType = True # a bool

banner = "FTP Server" # A string


print(type(port))
print(type(banner))
print(type(portType))
print(banner.upper())
print(banner.lower())

portList = []
portList.append(80)
portList.append(25)
portList.append(443)
portList.append(22)

print('list of Ports:', portList)
portList.sort()
print('Port List after sorting:', portList)
pos = portList.index(80)
print('There are', str(pos), 'ports to scan before :80')
portList.remove(443)
print(portList)
cnt = len(portList)
print('scanning', str(cnt), 'total ports')

