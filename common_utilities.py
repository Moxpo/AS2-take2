import sys
import socket

def fileToBinary(file, socket):
    file = open(file, 'rb')
    data = file.read()
    file.close()
    byte_sent = socket.send(data)
    print(byte_sent)
    return byte_sent

def binaryToFile(binary, socket):
    file = open(binary, 'xb')
    data = socket.recv(400003)
    file.write(data)
    file.close()








































def socket_send(socket, sock_addr):
    data = bytearray(1)
    bytes_read = 0

    while len(data) > 0 and "\n" not in data.decode():
        data = socket.recv(4096)

        print(data.decode(), end="")
        bytes_read += len(data)
    return bytes_read

def keyboard_to_socket(socket):

    print("You: ", end="", flush=True)

    user_input = sys.stdin.readline()
    if user_input == "EXIT\n":
        return 0

    bytes_sent = socket.sendall(str.encode(user_input))
    return bytes_sent
