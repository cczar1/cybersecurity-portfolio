#!/usr/bin/env python3

"""
mini_port_scanner.py
Mini Port Scanner Tool:
This basic port scanner tool can be used to scan common ports on your device.
"""

# Allow Python to communicate over networks
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
      Attempt to connect to a host:port. Return True if port is open. Return false if port is closed.
    - Try statement allows code to be run that may cause an error without crashing program
    - Returns:
      - "Open" if the port is open
      - "Closed" if the port is closed
      - "Timeout" if connection is timed out
      - "Invalid host" if the host is not valid
      - "Error: <message>" for other exceptions
    """
    try:
        # Create a TCP socket for IPv4
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.settimeout(1)  # Wait max 1 second per port
            result = s.connect_ex((host,port))  # Try to connect and check if the port is open

            if result == 0:
                return "Open"  # Port accepted the connection
            else:
                return "Closed"  # Port refused the connection
    
    except socket.gaierror:
        # If the hostname/IP is invalid
        return "Invalid host"
    except socket.gaierror:
        # If the connection takes too long
        return "Timeout"
    except Exception as e:
        # Any other unexpected error
        return f"Error: {e}"
            
