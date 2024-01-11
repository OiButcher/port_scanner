import socket
import threading

def scan_port(target_ip, port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout for the connection attempt
    s.settimeout(1)

    try:
        # Attempt to connect to the target IP and port
        s.connect((target_ip, port))
        print(f"Port {port} is open")
    except socket.error:
        # Connection attempt failed, port is likely closed
        pass
    finally:
        # Close the socket
        s.close()

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip}...\n")
    
    # Create a list to hold thread objects
    threads = []
    
    # Create threads to scan each port in the specified range
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Set the target IP address and port range to scan
    target_ip = "127.0.0.1"  # Replace with the target IP address
    start_port = 1
    end_port = 1024  # You can adjust the port range as needed

    # Run the port scanner
    port_scanner(target_ip, start_port, end_port)

