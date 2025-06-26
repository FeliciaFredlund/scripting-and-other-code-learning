from netmiko import ConnectHandler
from datetime import datetime

start_time = datetime.now()

# routern
router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco"
}

# Anslut till router
connection = ConnectHandler(**router)

# Interface kommandon
interface_commands = [
    "interface loopback 1", "ip add 10.0.0.1 255.255.255.0", "no shutdown",
    "interface loopback 2", "ip add 172.16.0.1 255.255.128.0", "no shutdown",
    "interface loopback 3", "ip add 192.168.200.1 255.255.255.0", "no shutdown"
]

# Default route kommando
default_route_command = "ip route 0.0.0.0 0.0.0.0 f0/0"

# Rip kommando
rip_commands = [
    "router rip",
    "network 10.0.0.0",
    "network 172.16.0.0",
    "network 192.168.200.0",
    "network 192.168.1.0",
    "passive-interface f0/0",
    "default-information originate"
]

# Konfigurering
all_commands = interface_commands + [default_route_command] + rip_commands
command_output = connection.send_config_set(all_commands)

# Hämta verifikation allt blev rätt
ip_int_br = connection.send_command("show ip int br")
ip_prot = connection.send_command("show ip prot")
ip_route = connection.send_command("show ip route")
show_run_config = connection.send_command("show run")

# Avsluta anslutning till router
connection.disconnect()

end_time = datetime.now()

# Printar show kommandon och tid till terminalen
print("\n================\nIP Interface Brief\n================")
print(ip_int_br)
print("================\nIP Protocol\n================")
print(ip_prot)
print("================\nIP Route\n================")
print(ip_route)

print("================\nTimning\n================")
print(f"Start tid: {start_time}\n Slut tid: {end_time}\n Tiden det tog: {end_time - start_time}")

print("================\nShow Running Config\n================")
print(show_run_config)