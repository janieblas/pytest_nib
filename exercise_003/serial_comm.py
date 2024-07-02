# serial_comm.py

# Simulated serial port states
serial_ports = {}

def open_port(port):
    """
    Simulates opening a serial port.
    
    Parameters:
    - port (str): The name of the port to open.

    Returns:
    - bool: True if the port is successfully opened, False otherwise.
    """
    if port not in serial_ports:
        serial_ports[port] = {"open": True, "data": ""}
        return True
    return False

def close_port(port):
    """
    Simulates closing a serial port.
    
    Parameters:
    - port (str): The name of the port to close.

    Returns:
    - bool: True if the port is successfully closed, False otherwise.
    """
    if port in serial_ports and serial_ports[port]["open"]:
        serial_ports[port]["open"] = False
        return True
    return False

def send_data(port, data):
    """
    Simulates sending data to a serial port.
    
    Parameters:
    - port (str): The name of the port to send data to.
    - data (str): The data to send.

    Returns:
    - bool: True if data is successfully sent, False otherwise.
    """
    if port in serial_ports and serial_ports[port]["open"]:
        serial_ports[port]["data"] += data
        return True
    return False

def receive_data(port):
    """
    Simulates receiving data from a serial port.
    
    Parameters:
    - port (str): The name of the port to receive data from.

    Returns:
    - str: The received data.
    """
    if port in serial_ports and serial_ports[port]["open"]:
        data = serial_ports[port]["data"]
        serial_ports[port]["data"] = ""  # Clear the buffer after reading
        return data
    return ""
