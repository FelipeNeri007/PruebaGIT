import socket

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to server on", host, "port", port)

        while True:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            client_socket.sendall(f"{num1},{num2}".encode())
            data = client_socket.recv(1024)
            print("Result from server:", data.decode())

if __name__ == "__main__":
    main()