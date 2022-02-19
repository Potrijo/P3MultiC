# We want to wetie the source ode for the client-side so that the client can connect to the server we created.
# So in this Client-Server, we need the same sockt libraru to establish a connetion with the Server-side.
# Assigning the same host and port number to the client as we defined in the Server otherwise it will not make the connection between them.

import socket 
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

# Setting up a connection using connect() of the socket library which stablishes a connection with the server using the host and port we provided.

print('Wating for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

# to ensure the client keeps running as the Server is Running. So for that, we need to use a while loop that.
# And we also going to provide aninput 

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()