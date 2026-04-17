import socket

# Banner
print("=" * 40)
print("        SIMPLE PORT SCANNER")
print("=" * 40)

# Input target
target = input("Enter IP address (use 127.0.0.1): ")

print("\nScanning target:", target)

# List to store open ports
open_ports = []

# Scan ports
for port in range(1, 9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.3)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    s.close()

# Summary
print("\nScan Completed")
print("Open Ports:", open_ports)
