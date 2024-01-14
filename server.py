import usocket as socket

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS
MENU_BUTTON_WIDTH = 300
MENU_BUTTON_HEIGHT = 150

LIGHT = (227, 193, 111)
DARK = (184, 139, 74)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def create_config():
    return (
        "CONFIGURATION\n"
        f"WIDTH={WIDTH}\n"
        f"HEIGHT={HEIGHT}\n"
        f"ROWS={ROWS}\n"
        f"COLS={COLS}\n"
        f"SQUARE_SIZE={SQUARE_SIZE}\n"
        f"MENU_BUTTON_WIDTH={MENU_BUTTON_WIDTH}\n"
        f"MENU_BUTTON_HEIGHT={MENU_BUTTON_HEIGHT}\n"
        f"LIGHT={','.join(map(str, LIGHT))}\n"
        f"DARK={','.join(map(str, DARK))}\n"
        f"WHITE={','.join(map(str, WHITE))}\n"
        f"BLACK={','.join(map(str, BLACK))}\n"
        f"GREY={','.join(map(str, GREY))}\n"
        f"RED={','.join(map(str, RED))}\n"
        f"GREEN={','.join(map(str, GREEN))}\n"
        f"BLUE={','.join(map(str, BLUE))}\n"
    )

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 80))
    server.listen(5)

    print("Server listening on port 80...")

    while True:
        client, addr = server.accept()
        print("Client connected from", addr)

        request = client.recv(1024).decode("utf-8")
        print("Received request:", request)

        response = create_config()
        client.sendall("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n" + response)
        client.close()

if __name__ == "__main__":
    start_server()
