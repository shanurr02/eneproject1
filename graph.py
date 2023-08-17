import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import datetime

def save_graph_as_image():
    file_path = "graph_image.png"
    canvas_agg = FigureCanvasAgg(fig)
    canvas_agg.print_png(file_path)
    print(f"Graph image saved as {file_path}")

# Create the main application window
root = tk.Tk()
root.title("Graph with Download Button")

# Create a Figure and a subplot
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)

# Sample data for time and values
fullTime = datetime.datetime.now().time()
current_hour = fullTime.hour
time = [current_hour-22.5,current_hour-19.5,current_hour-16.5, current_hour-13.5, current_hour-10.5, current_hour-7.5,current_hour-4.5, current_hour-1.5]
values = [10, 20, 25, 30, 15,12,12,14]

# Plot the data
ax.plot(time, values, marker='o')
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Sample Graph")

# Create a canvas to display the graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=50, y=50)

# Create a button to download the graph
download_button = tk.Button(root, text="Download Graph", command=save_graph_as_image)
download_button.place(x=200, y=250)

# Start the main event loop
root.mainloop()
