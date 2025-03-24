'''
Script for terminal to use SSH to configure an unknown number of loopback interfaces with IP addresses from a pool
using Paramiko
Author: Felicia Fredlund
Last updated: 2025-02-28

How to run:
python(3) FILENAME.py IP-ADDRESS USERNAME LAST_OCTET/PREFIX

Examples:
python3 lab4-ssh-paramiko.py 192.168.10.1 TIO 78/32
python3 lab4-ssh-paramiko.py 192.168.20.1 TJUGO 78/24
python3 lab4-ssh-paramiko.py 192.168.30.1 TRETTIO 50/32
'''

import paramiko
import sys
import ipaddress
import getpass 
import time

def main():    
    print("## Initial error checking started ##")

    hostname, username, last_octet, prefix = parameterChecking(sys.argv[1:])

    ip_template = getIPTemplate(username, prefix)

    print("## Initial error checking complete ##")
    print("## Connection phase started ##")

    password = getpass.getpass("User password for connection: ")

    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        connection.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
    except Exception as e:
        print(e)
        print("## Login failed. ##")
        return
    
    channel = connection.invoke_shell()
    time.sleep(1)
    output = channel.recv(65535).decode()

    if "#" not in output:
        print("## Login failed. Specifically Channel.invoke_shell() ##")
        connection.close()
        return
    
    print("## Connection phase completed ##")
    print("## Creating commands started ##")

    channel.send("show run | section interface Loopback\n")
    time.sleep(5)
    output = channel.recv(65535).decode()

    loopbacks = list(filter(lambda line: line.startswith("interface Loopback"), output.splitlines()))
    cmds = []
    for i in range(len(loopbacks)):
        cmds.append(loopbacks[i] + "\n")
        cmds.append(ip_template.replace("y", str(last_octet + i)) + "\n")
    
    print("## Creating commands completed ##")
    print("## Sending commands started ##")

    channel.send("conf t\n")
    time.sleep(1)

    for cmd in cmds:
        channel.send(cmd)
        time.sleep(1)
        output = channel.recv(65535).decode() # To clear the channel

    channel.send("end\n")
    time.sleep(1)
    output = channel.recv(65535).decode()

    print("## Sending commands completed ##")

    channel.send("show run | section interface Loopback\n")
    time.sleep(5)
    output = channel.recv(65535).decode()
    connection.close()
    
    print("Show running config, but only interface loopback:")
    print(output)
    
    print("## Script finished ##")

def getIPTemplate(network_name, prefix):
    if network_name == "TIO":
        network_id = 11
    elif network_name == "TJUGO":
        network_id = 21
    elif network_name == "TRETTIO":
        network_id = 31

    # A carefully selected network id chosen to be able to get any netmask sent
    mask = ipaddress.IPv4Network("128.0.0.0/" + str(prefix)).netmask
    return f"ip address 192.168.{network_id}.y {mask}"

def parameterChecking(script_parameters=[]):
    error_text = ""
    
    # Checking number of arguments
    if len(script_parameters) != 3:
        error_text += "Error: Not enough arguments. Needs IP address, username, and last_octet/prefix.\n"
    
    # Checking IP address
    try:
        ip_address = ipaddress.ip_address(script_parameters[0]).exploded
    except:
        error_text += "Error: Not a valid IP address.\n"

    # Checking username
    username = script_parameters[1]
    if username != "TIO" and username != "TJUGO" and username != "TRETTIO":
        error_text += "Error: Username is not correct.\n"

    # Checking last octet and prefix
    last_octet, prefix = script_parameters[2].split("/")

    try:
        last_octet = int(last_octet)
        if last_octet < 0 or last_octet > 255:
            error_text += "Error: Last octet is not a valid IPv4 octet.\n"
    except:
        error_text += "Error: Last octet is not a number (integer).\n"

    try:
        prefix = int(prefix)
        if prefix < 1 or prefix > 32:
            error_text += "Error: Prefix needs to be valid for an IPv4 address.\n"
    except:
        error_text += "Error: Prefix is not a number (integer).\n"
    
    # If there were errors, this executes
    if len(error_text) != 0:
        print(error_text)
        sys.exit(1)

    return ip_address, username, last_octet, prefix

if __name__ == "__main__":
    main()