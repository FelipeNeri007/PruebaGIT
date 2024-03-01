import socket

def operate_numbers(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Error: Division by zero"
    return addition, subtraction, multiplication, division

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server listening on", host, "port", port)

        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                nums = data.decode().split(',')
                num1 = int(nums[0])
                num2 = int(nums[1])
                result = operate_numbers(num1, num2)
                conn.sendall(str(result).encode())

if __name__ == "__main__":
    main()
