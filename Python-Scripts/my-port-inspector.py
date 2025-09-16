#!/usr/bin/env python3

"""
File name: my-port-inspector.py
myPort Inspector: This basic port scanner tool can be used to scan common ports on your device. 
"""

# Allows Python to create network connections
import socket

"""
- Define default ports; list of common ports to scan
- All caps used for constant variable
- Common ports array: 
  22 - SSH (secure shell)
  80 - HTTP (web traffic)
  443 - HTTPS (secure web traffic, TLS)
  3389 - Remote Desktop (Windows)
"""
COMMON_PORTS = [22, 80, 443, 3389]
 
"""
Function to scan port
Define function that takes a host (IP address) and port number
Function can then be called for each port the user would like to verify
"""
def scan_port(host, port):
    """
    - Attempt to connect to a host:port. 
    - Try statement allows code to be run that may cause an error without crashing program
    - Returns:
      - "Open"             : port accepted the connection
      - "Closed"           : port refused the connection
      - "Timeout"          : connection attempt timed out
      - "Invalid host"     : hostname/IP not valid
      - "Error: <message>" : other unexpected errors 
    """
    try:
        # Create a TCP socket for IPv4 and ensure it's closed automatically
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.settimeout(1)  # Wait max 1 second per port
            result = s.connect_ex((host,port))  # Try to connect and check if the port is open (returns 0 if successful)

            if result == 0:
                return "Open"  # Port accepted the connection
            else:
                return "Closed"  # Port refused the connection
    
    except socket.gaierror:
        # If the hostname/IP is invalid
        return "Invalid host"
    except socket.timeout:
        # If the connection takes too long
        return "Timeout"
    except Exception as e:
        # Any other unexpected error
        return f"Error: {e}"

#Main program
def main():
    """
    Ask the user which host to scan
    .strip() removes any leading/trailing whitespace for IP input
    """
    host = input("Enter the host/IP address to scan (xxx.x.x.x): ").strip()
    print(f"\nScanning {host}...\n")

    # Loop through the common ports and check each one
    for port in COMMON_PORTS:
        status = scan_port(host, port)
        print(f"Port {port}: {status}")
    
    print("\nScan complete.")

# Only run main() if this file is executed directly (best practice)
if __name__ == "__main__":
    main()

            
