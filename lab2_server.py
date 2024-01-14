import machine
import utime

# Configure UART
uart = machine.UART(0, baudrate=9600, tx=0, rx=1)

def process_message(message):
    # Add 'Svystun' to the received message
    modified_message = message.decode('utf-8') + ' Svystun'
    return modified_message

while True:
    if uart.any():
        received_message = uart.readline()
        if received_message:
            modified_message = process_message(received_message)
            print(f"Received: {received_message.strip()}, Modified: {modified_message}")
            uart.write(modified_message.encode('utf-8'))
    utime.sleep(0.1)

