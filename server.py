import socket
import sys
from common_utilities import socket_send, keyboard_to_socket


srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen(5)

except Exception as e:
	print(e)
	exit(1)

while True:

	try:
		print("Waiting for new client... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr)
		print("Client " + cli_addr_str + " connected. Now chatting...")

		while True:
			bytes_read = socket_send(cli_sock, cli_addr_str)
			if bytes_read == 0:
				print("Client closed connection.")
				break

			bytes_sent = keyboard_to_socket(cli_sock)
			if bytes_sent == 0:
				print("User-requested exit.")
				break

	finally:
		cli_sock.close()

srv_sock.close()

exit(0)
