# We want to wetie the source ode for the client-side so that the client can connect to the server we created.
# So in this Client-Server, we need the same sockt libraru to establish a connetion with the Server-side.
# Assigning the same host and port number to the client as we defined in the Server otherwise it will not make the connection between them.

import socket 
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233
status = True

# Setting up a connection using connect() of the socket library which stablishes a connection with the server using the host and port we provided.

print('Wating for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

# to ensure the client keeps running as the Server is Running. So for that, we need to use a while loop that.
# And we also going to provide aninput 

Response = ClientSocket.recv(2024)

Input = input('Entra el nom del artxiu que vols descarregar: ')
ClientSocket.send(str.encode(Input))
print('enviat nom del artxiu')

#Response = ClientSocket.recv(2048)
#print(Response.decode('utf-8'))
f = open(f'./Rebuts/{Input}', 'wb')
while True:
# read 1024 bytes from the socket (receive)
    bytes_read = ClientSocket.recv(2048)
    f.write(bytes_read)
    if not bytes_read:    
        # nothing is received
        # file transmitting is done
        f.close()
        break
    # write to the file the bytes we just received
    
    # update the progress bar

ClientSocket.close()