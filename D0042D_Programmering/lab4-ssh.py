'''
Script for terminal to use SSH to configure an unknown number of loopback interfaces with IP addresses from a pool
USE PARAMIKO BECAUSE IT IS BETTER FOR IT USES SSHv2, NETMIKO ONLY USES SSHv1
Author: Felicia Fredlund
Last updated: 2025-02-XX

Still to do: 
- virtual environment
- pip3 install cryptography
- pip3 install paramiko
- pip3 install netmiko
- pip3 install getpass
- pip3 install time 

How to run:
python(3) FILENAME.py IP-ADDRESS USERNAME

Examples:
python3 lab4-ssh.py 192.160.10.1 TIO
python3 lab4-ssh.py 192.160.20.1 TJUGO
python3 lab4-ssh.py 192.160.30.1 TRETTIO
'''

from enum import Enum

import sys
import getpass 
import time

class TextToNumber(Enum):
    TIO = 10
    TJUGO = 20
    TRETTIO = 30

def main():    
    print("## Initial error checking started ##")

    if len(sys.argv) != 3:
        raise Exception("Error: Not enough arguments to function. Please add IP address and username when calling script.")
    
    username = sys.argv[2]

    ip_address = sys.argv[1]    
    if not isIPAddress(ip_address):
        raise Exception("Error: IP address argument is not an IP address.")    

    ip_x = 0
    match username:
        case TextToNumber.TIO.name:
            ip_x = TextToNumber.TIO.value
        case TextToNumber.TJUGO.name:
            ip_x = TextToNumber.TJUGO.value
        case TextToNumber.TRETTIO.name:
            ip_x = TextToNumber.TRETTIO.value
        case _:
            raise ValueError("Error: Username is not correct.")
    ip_cmd_template = f"ip address {ip_x}.{ip_x}.{ip_x}.y 255.255.255.255"

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
        cmds.append(ip_cmd_template.replace("y", str(78+i)))

    print("## Creating commands completed ##")
    print(cmds)

    print("## Sending commands started ##")

    j = 0
    while j < len(cmds):
        temp_cmds = [cmds[j], cmds[j+1]]
        #device.send_config_set(temp_cmds)
        j += 2
        time.sleep(1)

    print("## Sending commands completed ##")

    #output = device.send_command("show run | section interface")
    #device.disconnect()
    
    #print("Show run on router:")
    #print(output)
    
    print("## Script finished ##")

def isIPAddress(ipadress):
    # NotImplementedError for IPv6
    if ":" in ipadress:
        raise NotImplementedError("IPv6 version is not implemented yet.")
    
    octets = ipadress.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            octet = int(octet)
        except ValueError:
            return False
        if  octet < 0 or octet > 255:
            return False
    return True

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