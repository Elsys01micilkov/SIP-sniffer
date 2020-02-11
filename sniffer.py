import socket
import struct

def get_addresses(raw_data):
    addresses = struct.unpack("!4s4s", raw_data)
    src_addr = socket.inet_ntoa(addresses[0])
    dst_addr = socket.inet_ntoa(addresses[1])
    return (src_addr, dst_addr)

def get_ports(raw_data):
    ports = struct.unpack("!2H", raw_data)
    return ports

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, 17)

    while True:
        raw_data, addr = conn.recvfrom(65535)

        src_addr, dst_addr = get_addresses(raw_data[12:20])

        data_without_ip_header = raw_data[20:]
        
        src_port, dst_port = get_ports(data_without_ip_header[:4])

        if dst_port == 5060:
            print(str(data_without_ip_header[8:], 'ascii'))
main()