# client.py
import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
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
# import errno
#
# HEADER_LENGTH = 10
#
# IP = "127.0.0.1"
# PORT = 1234
# my_username = input("Username: ")
#
# # Create a socket
# # socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
# # socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect to a given ip and port
# client_socket.connect((IP, PORT))
#
# # Set connection to non-blocking state, so .recv() call won;t block, just return some exception we'll handle
# client_socket.setblocking(False)
#
# # Prepare username and header and send them
# # We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
# username = my_username.encode('utf-8')
# username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
# client_socket.send(username_header + username)
#
# while True:
#
#     # Wait for user to input a message
#     message = input(f'{my_username} > ')
#
#     # If message is not empty - send it
#     if message:
#
#         # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
#         message = message.encode('utf-8')
#         message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
#         client_socket.send(message_header + message)
#
#     try:
#         # Now we want to loop over received messages (there might be more than one) and print them
#         while True:
#
#             # Receive our "header" containing username length, it's size is defined and constant
#             username_header = client_socket.recv(HEADER_LENGTH)
#
#             # If we received no data, server gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
#             if not len(username_header):
#                 print('Connection closed by the server')
#                 sys.exit()
#
#             # Convert header to int value
#             username_length = int(username_header.decode('utf-8').strip())
#
#             # Receive and decode username
#             username = client_socket.recv(username_length).decode('utf-8')
#
#             # Now do the same for message (as we received username, we received whole message, there's no need to check if it has any length)
#             message_header = client_socket.recv(HEADER_LENGTH)
#             message_length = int(message_header.decode('utf-8').strip())
#             message = client_socket.recv(message_length).decode('utf-8')
#
#             # Print message
#             print(f'{username} > {message}')
#
#     except IOError as e:
#         # This is normal on non blocking connections - when there are no incoming data error is going to be raised
#         # Some operating systems will indicate that using AGAIN, and some using WOULDBLOCK error code
#         # We are going to check for both - if one of them - that's expected, means no incoming data, continue as normal
#         # If we got different error code - something happened
#         if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#             print('Reading error: {}'.format(str(e)))
#             sys.exit()
#
#         # We just did not receive anything
#         continue
#
#     except Exception as e:
#         # Any other exception - something happened, exit
#         print('Reading error: '.format(str(e)))
#         sys.exit()
#
#
#
#
#




















import socket
import threading
import tkinter
import tkinter.scrolledtext
# from tkinter import simpledialog
#
# HOST = '162.158.233.82'
# PORT = 9090
#
#
# class CLIENT:
#
#
#
#     def __init__(self,host,port):
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.sock.connect((host,port))
# # content
#         msg = tkinter.Tk()
#         msg.withdraw()
#
#         self.nickname = simpledialog.askstring('Nickname','Please choose a nickname',parent=msg)
#
#
#         self.gui_done = False
#         self.running = True
#
#
#         gui_thread = threading.Thread(target=self.gui_loop)
#         recieve_thread = threading.Thread(target=self.recieve)
#
#
#
#         gui_thread.start()
#         recieve_thread.start()
#
#
#     def gui_loop(self):
#         self.win = tkinter.Tk()
#         self.win.configure(bg='lightgray')
#
#         self.chat_lable = tkinter.Label(self.win, text='Chat=',bg='lightgray')
#         self.chat_lable.config(font=('Arial',12))
#         self.chat_lable.pack(padx=20,pady=5)
#
#
#         self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
#         self.text_area.pack(padx=20,pady=5)
#         self.text_area.config(state='disable')
#
#         self.msg_lable = tkinter.Label(self.win, text='Message:', bg='lightgray')
#         self.msg_lable.config(font=('Arial', 12))
#         self.msg_lable.pack(padx=20, pady=5)
#
#
#
#         self.input_area = tkinter.Button(self.win,text="Send",command=self.write)
#         self.send_button.config(font=('Arial',12))
#         self.send_button.pack(padx=20,pady=5)
#
#
#
#         self.gui_done = True
#
#         self.win.protocol('WM_DELETE_WINDOW',self.stop)
#
#         self.win.mainloop()
#
#
#
#     def write(self):
#         message = f'{self.nickname}: {self.input_area.get("1.0","end")}'
#         self.sock.send(message.encode('utf-8'))
#         self.input_area.delete('1.0','end')
#
#
# #get the whole text
#     def stop(self):
#         self.running = False
#         self.win.destroy()
#         self.socket.close()
#         exit(0)
#
#
#     def receive(self):
#         while self.running:
#             try:
#                 message = self.sock.recv(1024)
#                 if message == 'NICK':
#                     self.sock.send(self.nickname.encode('utf-8'))
#                 else:
#                     if self.gui_done:
#                         self.text_area.config(state='normal')
#                         self.text_area.insert('end',message)
#                         self.text_area.yview('end')
#                         self.text_area.config(state='disable')
#
#             except ConnectionAbortedError:
#                 break
#             except:
#                 print('Error')
#                 self.sock.close()
#                 break
#
# client = CLIENT(HOST,PORT)
