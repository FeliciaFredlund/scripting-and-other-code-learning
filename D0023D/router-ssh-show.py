from netmiko import ConnectHandler # type: ignore

# routern vi ska använda SSH för att testa anslutning
router = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "cisco"
}

# Netmikos ConnectHandler ansluter till routern med SSH
connection = ConnectHandler(**router)

# Här sparas utskriften av kommandot "show ip int br" till output
output = connection.send_command("show ip int br")

# Anslutningen till routern avslutas
connection.disconnect()

# Printar output till terminalen
print("Show IP Interface Brief på routern")
print(output)


