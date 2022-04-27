import time
import socket
import sys
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)


#
#
#
#
#
#
#
#
#
#
#
#




















# import socket
# import select
#
# HEADER_LENGTH = 10
#
# IP = "127.0.0.1"
# PORT = 1234
#
# # Create a socket
# # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # SO_ - socket option
# # SOL_ - socket option level
# # Sets REUSEADDR (as a socket option) to 1 on socket
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
# # Bind, so server informs operating system that it's going to use given IP and port
# # For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
# server_socket.bind((IP, PORT))
#
# # This makes server listen to new connections
# server_socket.listen()
#
# # List of sockets for select.select()
# sockets_list = [server_socket]
#
# # List of connected clients - socket as a key, user header and name as data
# clients = {}
#
# print(f'Listening for connections on {IP}:{PORT}...')
#
# # Handles message receiving
# def receive_message(client_socket):
#
#     try:
#
#         # Receive our "header" containing message length, it's size is defined and constant
#         message_header = client_socket.recv(HEADER_LENGTH)
#
#         # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
#         if not len(message_header):
#             return False
#
#         # Convert header to int value
#         message_length = int(message_header.decode('utf-8').strip())
#
#         # Return an object of message header and message data
#         return {'header': message_header, 'data': client_socket.recv(message_length)}
#
#     except:
#
#         # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
#         # or just lost his connection
#         # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
#         # and that's also a cause when we receive an empty message
#         return False
#
# while True:
#
#     # Calls Unix select() system call or Windows select() WinSock call with three parameters:
#     #   - rlist - sockets to be monitored for incoming data
#     #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
#     #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
#     # Returns lists:
#     #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
#     #   - writing - sockets ready for data to be send thru them
#     #   - errors  - sockets with some exceptions
#     # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
#     read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
#
#
#     # Iterate over notified sockets
#     for notified_socket in read_sockets:
#
#         # If notified socket is a server socket - new connection, accept it
#         if notified_socket == server_socket:
#
#             # Accept new connection
#             # That gives us new socket - client socket, connected to this given client only, it's unique for that client
#             # The other returned object is ip/port set
#             client_socket, client_address = server_socket.accept()
#
#             # Client should send his name right away, receive it
#             user = receive_message(client_socket)
#
#             # If False - client disconnected before he sent his name
#             if user is False:
#                 continue
#
#             # Add accepted socket to select.select() list
#             sockets_list.append(client_socket)
#
#             # Also save username and username header
#             clients[client_socket] = user
#
#             print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
#
#         # Else existing socket is sending a message
#         else:
#
#             # Receive message
#             message = receive_message(notified_socket)
#
#             # If False, client disconnected, cleanup
#             if message is False:
#                 print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
#
#                 # Remove from list for socket.socket()
#                 sockets_list.remove(notified_socket)
#
#                 # Remove from our list of users
#                 del clients[notified_socket]
#
#                 continue
#
#             # Get user by notified socket, so we will know who sent the message
#             user = clients[notified_socket]
#
#             print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
#
#             # Iterate over connected clients and broadcast message
#             for client_socket in clients:
#
#                 # But don't sent it to sender
#                 if client_socket != notified_socket:
#
#                     # Send user and message (both with their headers)
#                     # We are reusing here message header sent by sender, and saved username header send by user when he connected
#                     client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
#
#     # It's not really necessary to have this, but will handle some socket exceptions just in case
#     for notified_socket in exception_sockets:
#
#         # Remove from list for socket.socket()
#         sockets_list.remove(notified_socket)
#
#         # Remove from our list of users
#         del clients[notified_socket]
#



















# import socket
# import threading
# Host = '162.158.233.82'
# Port = 9090
#
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind((Host,Port))
#
# server.listen()
#
# clients = []
# nicknames = []
#
# def broadcast(message):
#     for client in clients:
#         client.sent(message)
#
# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024).decode('utf-8')
#             print(f'{nicknames[clients.index(client)]} says {message}')
#             broadcast(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             nicknames.remove(nickname)
#             break
#
#
# def receive():
#     while True:
#         client , address = server.accept()
#         print(f"Connected with {str(address)}")
#
#
#         client.send('NICK'.encode('utf-8'))
#         nickname = client.recv(1024)
#         nicknames.append(nickname)
#
#         clients.append(client)
#
#         print(f"NICKNAME of the client is {nickname}")
#         broadcast(f"{nickname} connected to the server! \n".encode('utf-8'))
#         client.send(f'Connected to the server'.encode('utf-8'))
#         thread = threading.Thread(target=handle(), args=(client,))
#         thread.start()
#
# print('Server running :) ')
# receive()
#############################omyyyyygodddddddd#############################33








# import socket
# from threading import Thread
#
# # server's IP address
# SERVER_HOST = "0.0.0.0"
# SERVER_PORT = 5002 # port we want to use
# separator_token = "<SEP>" # we will use this to separate the client name & message
#
# # initialize list/set of all connected client's sockets
# client_sockets = set()
# # create a TCP socket
# s = socket.socket()
# # make the port as reusable port
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # bind the socket to the address we specified
# s.bind((SERVER_HOST, SERVER_PORT))
# # listen for upcoming connections
# s.listen(5)
# print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
#
# #########################################################################################################
# def listen_for_client(cs):
#     """
#     This function keep listening for a message from `cs` socket
#     Whenever a message is received, broadcast it to all other connected clients
#     """
#     while True:
#         try:
#             # keep listening for a message from `cs` socket
#             msg = cs.recv(1024).decode()
#         except Exception as e:
#             # client no longer connected
#             # remove it from the set
#             print(f"[!] Error: {e}")
#             client_sockets.remove(cs)
#         else:
#             # if we received a message, replace the <SEP>
#             # token with ": " for nice printing
#             msg = msg.replace(separator_token, ": ")
#         # iterate over all connected sockets
#         for client_socket in client_sockets:
#             # and send the message
#             client_socket.send(msg.encode())
#
# while True:
#     # we keep listening for new connections all the time
#     client_socket, client_address = s.accept()
#     print(f"[+] {client_address} connected.")
#     # add the new connected client to connected sockets
#     client_sockets.add(client_socket)
#     # start a new thread that listens for each client's messages
#     t = Thread(target=listen_for_client, args=(client_socket,))
#     # make the thread daemon so it ends whenever the main thread ends
#     t.daemon = True
#     # start the thread
#     t.start()
#     ####################################################################################################
#     # close client sockets
#     for cs in client_sockets:
#         cs.close()
#     # close server socket
#     s.close()
#     ######################################################################################################
#     import socket
#     import random
#     from threading import Thread
#     from datetime import datetime
#     from colorama import Fore, init, Back
#
#     # init colors
#     init()
#
#     # set the available colors
#     colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
#               Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
#               Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
#               Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
#               ]
#
#     # choose a random color for the client
#     client_color = random.choice(colors)
#
#     # server's IP address
#     # if the server is not on this machine,
#     # put the private (network) IP address (e.g 192.168.1.2)
#     SERVER_HOST = "127.0.0.1"
#     SERVER_PORT = 5002  # server's port
#     separator_token = "<SEP>"  # we will use this to separate the client name & message
#
#     # initialize TCP socket
#     s = socket.socket()
#     print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
#     # connect to the server
#     s.connect((SERVER_HOST, SERVER_PORT))
#     print("[+] Connected.")
#
#     ####################################################################################################
#     # prompt the client for a name
#     name = input("Enter your name: ")
#
#
#     ####################################################################################################
#
#     def listen_for_messages():
#         while True:
#             message = s.recv(1024).decode()
#             print("\n" + message)
#
#
#     # make a thread that listens for messages to this client & print them
#     t = Thread(target=listen_for_messages)
#     # make the thread daemon so it ends whenever the main thread ends
#     t.daemon = True
#     # start the thread
#     t.start()
#     ####################################################################################################
#     while True:
#         # input message we want to send to the server
#         to_send = input()
#         # a way to exit the program
#         if to_send.lower() == 'q':
#             break
#         # add the datetime, name & the color of the sender
#         date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
#         # finally, send the message
#         s.send(to_send.encode())
#
#     # close the socket
#     s.close()
#     #################################  another chatroom :)###################
#
#     # import socket
#     # import select
#     #
#     # HEADER_LENGTH = 10
#     #
#     # IP = "127.0.0.1"
#     # PORT = 1234
#     #
#     # # Create a socket
#     # # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
#     # # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
#     # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     #
#     # # SO_ - socket option
#     # # SOL_ - socket option level
#     # # Sets REUSEADDR (as a socket option) to 1 on socket
#     # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     #
#     # # Bind, so server informs operating system that it's going to use given IP and port
#     # # For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
#     # server_socket.bind((IP, PORT))
#     #
#     # # This makes server listen to new connections
#     # server_socket.listen()
#     #
#     # # List of sockets for select.select()
#     # sockets_list = [server_socket]
#     #
#     # # List of connected clients - socket as a key, user header and name as data
#     # clients = {}
#     #
#     # print(f'Listening for connections on {IP}:{PORT}...')
#     #
#     # # Handles message receiving
#     # def receive_message(client_socket):
#     #
#     #     try:
#     #
#     #         # Receive our "header" containing message length, it's size is defined and constant
#     #         message_header = client_socket.recv(HEADER_LENGTH)
#     #
#     #         # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
#     #         if not len(message_header):
#     #             return False
#     #
#     #         # Convert header to int value
#     #         message_length = int(message_header.decode('utf-8').strip())
#     #
#     #         # Return an object of message header and message data
#     #         return {'header': message_header, 'data': client_socket.recv(message_length)}
#     #
#     #     except:
#     #
#     #         # If we are here, client closed connection violently, for example by pressing ctrl+c on his script
#     #         # or just lost his connection
#     #         # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write)
#     #         # and that's also a cause when we receive an empty message
#     #         return False
#     #
#     # while True:
#     #
#     #     # Calls Unix select() system call or Windows select() WinSock call with three parameters:
#     #     #   - rlist - sockets to be monitored for incoming data
#     #     #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
#     #     #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
#     #     # Returns lists:
#     #     #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
#     #     #   - writing - sockets ready for data to be send thru them
#     #     #   - errors  - sockets with some exceptions
#     #     # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
#     #     read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
#     #
#     #
#     #     # Iterate over notified sockets
#     #     for notified_socket in read_sockets:
#     #
#     #         # If notified socket is a server socket - new connection, accept it
#     #         if notified_socket == server_socket:
#     #
#     #             # Accept new connection
#     #             # That gives us new socket - client socket, connected to this given client only, it's unique for that client
#     #             # The other returned object is ip/port set
#     #             client_socket, client_address = server_socket.accept()
#     #
#     #             # Client should send his name right away, receive it
#     #             user = receive_message(client_socket)
#     #
#     #             # If False - client disconnected before he sent his name
#     #             if user is False:
#     #                 continue
#     #
#     #             # Add accepted socket to select.select() list
#     #             sockets_list.append(client_socket)
#     #
#     #             # Also save username and username header
#     #             clients[client_socket] = user
#     #
#     #             print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
#     #
#     #         # Else existing socket is sending a message
#     #         else:
#     #
#     #             # Receive message
#     #             message = receive_message(notified_socket)
#     #
#     #             # If False, client disconnected, cleanup
#     #             if message is False:
#     #                 print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
#     #
#     #                 # Remove from list for socket.socket()
#     #                 sockets_list.remove(notified_socket)
#     #
#     #                 # Remove from our list of users
#     #                 del clients[notified_socket]
#     #
#     #                 continue
#     #
#     #             # Get user by notified socket, so we will know who sent the message
#     #             user = clients[notified_socket]
#     #
#     #             print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
#     #
#     #             # Iterate over connected clients and broadcast message
#     #             for client_socket in clients:
#     #
#     #                 # But don't sent it to sender
#     #                 if client_socket != notified_socket:
#     #
#     #                     # Send user and message (both with their headers)
#     #                     # We are reusing here message header sent by sender, and saved username header send by user when he connected
#     #                     client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
#     #
#     #     # It's not really necessary to have this, but will handle some socket exceptions just in case
#     #     for notified_socket in exception_sockets:
#     #
#     #         # Remove from list for socket.socket()
#     #         sockets_list.remove(notified_socket)
#     #
#     #         # Remove from our list of users
#     #         del clients[notified_socket]