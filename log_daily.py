from netmiko import ConnectHandler

#ip host
routers = [
    {"host": "192.168.10.2", "name": "R1"},
    {"host": "192.168.10.3", "name": "R2"},
    {"host": "192.168.10.4", "name": "R3"},
    {"host": "192.168.10.5", "name": "R4"}
]

device_type = "cisco_ios"
username = "admin"
password = "admin1234"
secret = "cisco"

# Loop
for router in routers:
    print(f"\nConnecting to {router['name']} ({router['host']})...")
    device = {
        "device_type": device_type,
        "host": router["host"],
        "username": username,
        "password": password,
        "secret": secret,
    }

    try:
        # Connect and collect logs
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_command("show logging")

        # Save logs to a files
        filename = f"{router['name']}_log.txt"
        with open(filename, "w") as file:
            file.write(output)

        print(f"✅ Logs collected from {router['name']} and saved to {filename}")

        connection.disconnect()

    except Exception as e:
        print(f"❌ Failed to connect to {router['name']}: {e}")
