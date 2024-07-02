#import pytest
import sys
sys.path.append('C:\\Embedded_SMT32\\pytest_studying\\exercise_003')

from serial_comm import open_port, close_port, send_data, receive_data, serial_ports


def test_open_port():
    port_name = "COM1"

    assert open_port(port_name) == True

def test_open_port_reopen():
    port_name = "COM2"

    #simulate data in serial port
    serial_ports[port_name] = {"open": True, "data": "Example data"}
    assert open_port(port_name) == False

def test_send_data():
    port_name = "COM3"
    open_port(port_name)

    data_send = "Example data"
    assert send_data(port_name,data_send) == True

def test_send_data_without_port():
    port_name = "COM4"
    #open_port(port_name)

    data_send = "Example data"
    assert send_data(port_name,data_send) == False

def test_receive_data():
    port_name = "COM5"
    open_port(port_name)
    data_send = "Hello World!"
    send_data(port_name,data_send)

    s_received_data = receive_data(port_name)

    assert s_received_data == data_send 

def test_receive_data_no_data_available():
    #we need to use a different port than COM3.    
    test_port = "COM6"

    assert receive_data(test_port) == ""

def test_close_port():
    port_name = "COM5"
    open_port(port_name)

    assert close_port(port_name) == True

def test_close_port_without_port():
    port_name = "COM6"
    #open_port(port_name)

    assert close_port(port_name) == False




