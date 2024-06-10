import socket

# Define the IP address and port to listen on
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 5000        # Replace with your desired port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the socket to reuse the address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    # Receive data from the client
    data = client_socket.recv(1024)
    if data:
        print(f'Received data: {data}')

        # Send a response to the client
        response = b'ACK'
        client_socket.sendall(response)

    # Close the client connection
    client_socket.close()
