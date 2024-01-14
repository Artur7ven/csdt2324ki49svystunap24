import serial
import tkinter as tk

ser = serial.Serial('COM5', 9600, timeout=1)  # Update 'COM5' with your actual port

def send_message():
    user_input = entry.get()
    conversation.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)  # Clear the entry field
    ser.write(user_input.encode('utf-8'))

def receive_message():
    while ser.in_waiting:
        received_message = ser.readline().decode('utf-8')
        conversation.insert(tk.END, f"Server: {received_message}\n")

root = tk.Tk()
root.title("UART Communication Client")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

conversation = tk.Text(frame, width=40, height=10, wrap="word", font=("Arial", 14))
conversation.pack(side=tk.TOP, pady=10)

entry = tk.Entry(frame, width=30, font=("Arial", 12))
entry.pack(side=tk.LEFT, pady=10)

send_button = tk.Button(frame, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.RIGHT)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12))
exit_button.pack(pady=10)

# Poll for received messages
def poll_messages():
    receive_message()
    root.after(100, poll_messages)

# Start polling for messages
poll_messages()

root.mainloop()
