# Create a Server script first so that the client comunicates with it. So we need to import the socket library to establish a connection & thread library for multithreading
import socket 
import os # portable way of using operating system dependent functionality, fx reading or opening files with open(), manipulate paths, etc.
from _thread import *

# Create a socket connection using socket() of the socket library. Along with this, let's declare the host and port on which we need to communicate with clients.
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0

# Bind a host and port to the socket server we created above in the program.
# So if it binds successfully then it starts wating for the client otherwise it just returns the error that occurred while establishing a connection

try:
    ServerSocket.bind((host,port))

except socket.error as e:
    print(str(e))

print('Wating for a connection')
ServerSocket.listen(5) # 5 thread as limit

# We want support handle multiple clients or threads at the same time simultaneosly 
# Create a function that handles requests from the individual client by a thread
# Function named threaded_client which connects to each client on the different address given by the server
# In this function, we're using recv() function to get data from each client independently and then we simply return the reply to the particular client with the same message with string concatenate "Server Says" in the begining.

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Marky Server'))
    while True:
        data = connection.recv(2048)
        reply = 'Marky says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

# We want run our Server all the time, which means we don't want to make that our Server get stopped.
# So for that, we need to use a while loop to make it run the Server endlessly until we manually stop the Server.
# Now we are going to accept connections from the client using accept the () function of the socket server.
# It returns the type of client which has connected and along with the unique thread number or address provided to it.
# Then we use the start_new_thread() function of the thread class which creates or asigns a new thread to each client to handle them individually

while True: 
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))  
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()