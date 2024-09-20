import socket

def scan_ports(ip, port_range):
    open_ports = []
    for port in range(*port_range):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target_ip = "192.168.1.1"  # Change this to the target IP
port_range = (1, 1025)  # Standard ports
open_ports = scan_ports(target_ip, port_range)

print(f"Open ports on {target_ip}: {open_ports}")
