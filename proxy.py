import socket
import ssl

# Configuration
DNS_SERVER = "1.1.1.1"  # DNS-over-TLS server to forward queries to
DNS_PORT = 853  # Port for DNS-over-TLS server
LISTEN_PORT = 53  # Port to listen for incoming DNS queries on

def handle_query(client_socket):
    # Receive DNS query from client
    query = client_socket.recv(4096)

    # Connect to DNS-over-TLS server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tls_socket = ssl.wrap_socket(server_socket)
    tls_socket.connect((DNS_SERVER, DNS_PORT))

    # Send query to DNS-over-TLS server and receive response
    tls_socket.send(query)
    response = tls_socket.recv(4096)

    # Send response back to client
    client_socket.send(response)

    # Close sockets
    tls_socket.close()
    client_socket.close()

def main():
    # Create socket to listen for incoming DNS queries
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(("0.0.0.0", LISTEN_PORT))
    listen_socket.listen(5)

    print(f"Listening for DNS queries on port {LISTEN_PORT}...")

    # Loop indefinitely to handle incoming queries
    while True:
        client_socket, _ = listen_socket.accept()
        handle_query(client_socket)

if __name__ == "__main__":
    main()
