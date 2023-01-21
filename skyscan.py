from colorit import *
init_colorit()
import subprocess
import nmap
import os
import threading
from six.moves import input 
import sys
import requests

#Colors code
ORANGE=255, 165, 0
GREEN=0, 255, 0
RED=255,0,0
YELLOW=255, 255, 0
PURPLE=148,0,211

DEEPPINK=255,20,147
CYAN=0,238,238
WHITE=255, 255, 255
print(color("""
		███████╗  ██╗  ██╗  ██╗   ██╗  ███████╗   ██████╗   █████╗   ███╗   ██╗
		██╔════╝  ██║ ██╔╝  ╚██╗ ██╔╝  ██╔════╝  ██╔════╝  ██╔══██╗  ████╗  ██║
		███████╗  █████╔╝    ╚████╔╝   ███████╗  ██║       ███████║  ██╔██╗ ██║
		╚════██║  ██╔═██╗     ╚██╔╝    ╚════██║  ██║       ██╔══██║  ██║╚██╗██║
		███████║  ██║  ██╗     ██║     ███████║  ╚██████╗  ██║  ██║  ██║ ╚████║
		╚══════╝  ╚═╝  ╚═╝     ╚═╝     ╚══════╝   ╚═════╝  ╚═╝  ╚═╝  ╚═╝  ╚═══╝
		                                                                 "By: V3-Sky" """,(WHITE)))
print(color("[~]",(WHITE)) + color(" The Best Tools For ennumeration!!!",(CYAN)))
print(color("[~]",(WHITE)) + color(" Usage: python3 skyscan.py!!!",(CYAN)))
print(color("--------------",(CYAN))+color("Social Media",(WHITE))+color("---------------",(CYAN)))
print(color("|                                       |",(CYAN)))
print(color("|",(CYAN))+color("  https://discord.gg/bZNS8az8          ",(ORANGE))+color("|",(CYAN)))
print(color("|",(CYAN))+color("  https://github.com/V3-Sky/TryHackMe  ",(ORANGE))+color("|",(CYAN)))
print(color("|_______________________________________|",(CYAN)))

host = input(color("[#]",(GREEN))+color(" Enter Your IP: ",(GREEN)))
print("                                                                                ")
print(color("-------------",(CYAN))+color("(Choix)",(WHITE))+color("--------------",(CYAN)))
print(color("|                                |",(CYAN)))
print(color("|",(CYAN))+color("  1):",(WHITE))+color(" All                       ",(ORANGE))+color("|",(CYAN)))
print(color("|",(CYAN))+color("  2):",(WHITE))+color(" Scan-Port                 ",(ORANGE))+color("|",(CYAN)))
print(color("|",(CYAN))+color("  3):",(WHITE))+color(" Brute-Forcing-Directory   ",(ORANGE))+color("|",(CYAN)))
print(color("|________________________________|",(CYAN)))


#tools scan port
def scan(host):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host, '1-65535')
    for host in nm_scan.all_hosts():
        for proto in nm_scan[host].all_protocols():
            lport = nm_scan[host][proto].keys()
            for port in lport:
                if nm_scan[host][proto][port]['state'] == 'open':
                    print(color(f"Open ",(WHITE)) +color(f'{host}:{port} ',(PURPLE)) +color(">",(WHITE))+color(f' {nm_scan[host][proto][port]["name"]}',(PURPLE)))

#command nmap details
def scan2():
	result = subprocess.run(['nmap', '-p', '0-65535', '-sCV', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode())
	print(result.stderr.decode())


#brute force directory
def scan3():
	f = open("skyscan.txt")
	x = "http://"+host+"/"
	direc = f.readlines()
	try:
		for d in direc:
			target2= (x + d).rstrip()
			r = requests.get(target2)
			if (r.status_code == 200):
				print(color(" [$] ",(WHITE)) +color(f'{target2}',(PURPLE)) + " > " +color(f'{r.status_code}',(WHITE)))
	except requests.exceptions.ConnectionError:
		print("server is down!!!\rPliiiiz run server apache!!")
#------------------------
xss = int(input(color("-->",(GREEN))+color(" Enter Number What Do you Need: ",(GREEN))))
#All
if xss == 1:
	print(color("[>]",(GREEN))+color(" Wait For Ennumeration Scannig...\n",(ORANGE)))
	t1 = threading.Thread(target=scan(host))
	print("\r")
	print(color("[>]",(GREEN))+color(" Script to be run Some brute Force Directory...\n",(ORANGE)))
	t3 = threading.Thread(target=scan3())
	print("\r")
	print(color("[>]",(GREEN))+color(" Script to be run Some Show details For All Port...\n",(ORANGE)))
	t2 = threading.Thread(target=scan2)
	t1.start()
	t3.start()
	t2.start()

#Scan-Port
elif xss == 2:
	print(color("[>]",(GREEN))+color(" Wait For Ennumeration Scannig...\n",(ORANGE)))
	t1 = threading.Thread(target=scan(host))
	print("\r")
	print(color("[>]",(GREEN))+color(" Script to be run Some Show details For All Port...\n",(ORANGE)))
	t2 = threading.Thread(target=scan2)
	t1.start()
	t2.start()

#Brute Forcing Directory
elif xss == 3:
	print(color("[>]",(GREEN))+color(" Script to be run Some brute Force Directory...\n",(ORANGE)))
	t3 = threading.Thread(target=scan3())
	t3.start()