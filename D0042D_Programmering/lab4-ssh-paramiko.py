'''
Script for terminal to use SSH to configure an unknown number of loopback interfaces with IP addresses from a pool
using Paramiko
Author: Felicia Fredlund
Last updated: 2025-02-XX

Still to do: 
- virtual environment
- pip3 install cryptography
- pip3 install paramiko
- pip3 install getpass
- pip3 install time 

How to run:
python(3) FILENAME.py IP-ADDRESS USERNAME LAST_OCTET/PREFIX

Examples:
python3 lab4-ssh-paramiko.py 192.160.10.1 TIO 78/32
python3 lab4-ssh-paramiko.py 192.160.20.1 TJUGO 78/24
python3 lab4-ssh-paramiko.py 192.160.30.1 TRETTIO 50/32
'''

import paramiko # type:ignore
import sys
import ipaddress
import getpass 
import time

def main():    
    print("## Initial error checking started ##")

    ip_address, username, last_octet, prefix = errorHandling(sys.argv[1:])

    ip_template = getIPTemplate(username, prefix)

    print("## Initial error checking complete ##")
    print("## Connection phase started ##")

    password = getpass.getpass("Need password to connect: ")

    #device = ConnectHandler(device_type="cisco_ios", host=ip_address, username=username, password=password)
    
    print("## Connection phase completed ##")
    print("## Creating commands started ##")

    #show_run = device.send_command("show run | section interface")
    show_run = ""
    time.sleep(1)

    loopbacks = list(filter(lambda line: line.startswith("interface Loopback"), show_run.splitlines()))
    cmds = []
    for i in range(len(loopbacks)):
        cmds.append(loopbacks[i])
        cmds.append(ip_template.replace("y", str(last_octet + i)))

    print(cmds)
    print("## Creating commands completed ##")

    print("## Sending commands started ##")

    j = 0
    while j < len(cmds):
        temp_cmds = [cmds[j], cmds[j+1]]
        #device.send_config_set(temp_cmds)
        j += 2
        time.sleep(1)

    print("## Sending commands completed ##")

    #output = device.send_command("show ip int br")
    #device.disconnect()
    
    print("Show ip int br on router:")
    #print(output)
    
    print("## Script finished ##")

def getIPTemplate(network_name, prefix):
    if network_name == "TIO":
        network_id = 11
    elif network_name == "TJUGO":
        network_id = 21
    elif network_name == "TRETTIO":
        network_id = 31

    mask = ipaddress.IPv4Network("128.0.0.0/" + str(prefix)).netmask
    return f"ip address 192.168.{network_id}.y {mask}"

def errorHandling(script_parameters=[]):
    if len(script_parameters) != 3:
        print("Error: Not enough arguments to function. Needs IP address, username, and last_octet/prefix.")
        sys.exit(1)
    
    ip_address = ipaddress.ip_address(script_parameters[0]).exploded

    username = script_parameters[1]
    if (username != "TIO") and (username != "TJUGO") and (username != "TRETTIO"):
        print("Error: Username is not correct.")
        sys.exit(1)

    last_octet, prefix = script_parameters[2].split("/")

    try:
        last_octet = int(last_octet)
        prefix = int(prefix)
    except:
        print("Error: last octet or prefix is not a number (integer).")
        sys.exit(1)

    if last_octet < 0 or last_octet > 255:
        print(f"Error: Not a valid last octet.")
        sys.exit(1)

    if prefix < 1 or prefix > 32:
        print("Error: Prefix needs to be valid for an IPv4 address.")
        sys.exit(1)
    
    return ip_address, username, last_octet, prefix

main()


'''
show_run = """interface FastEthernet0
	no ip address
!
interface FastEthernet1
	no ip address
!
interface Loopback2
	no ip address
!
interface Loopback3
	switchport mode trunk
	no ip address
!
"""
'''