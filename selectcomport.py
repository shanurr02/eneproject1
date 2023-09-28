import tkinter as tk
from tkinter import messagebox
import serial.tools.list_ports
import threading
# Function to handle button click event
def connect_to_arduino():
    selected_port = port_var.get()

    try:
        # Establish the connection
        ser = serial.Serial(selected_port, 9600)

        def read_from_arduino():
            while True:
                # Read data from the Arduino
                data = ser.readline().decode().strip()
                
                # Print the received data
                messagebox.showinfo("Arduino Data", data)

        # Start a thread to read from Arduino and display data
        thread = threading.Thread(target=read_from_arduino)
        thread.start()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Get a list of available COM ports
available_ports = [port.device for port in serial.tools.list_ports.comports()]
print(available_ports)

# Create the main application window
root = tk.Tk()
root.title("Arduino Data Reader")

# Create a label and dropdown menu to select the COM port
port_label = tk.Label(root, text="Select a COM port:")
port_label.pack(pady=10)
port_var = tk.StringVar(value=available_ports[0])
port_dropdown = tk.OptionMenu(root, port_var, *available_ports)
port_dropdown.pack(pady=10)

# Create a button to connect to Arduino
connect_button = tk.Button(root, text="Connect to Arduino", command=connect_to_arduino)
connect_button.pack(pady=10)

# Run the main event loop
root.mainloop()
