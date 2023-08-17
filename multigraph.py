import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphing_Day import getdatabyhour
from timeGenerator import get_hour_array

def create_graph_frame(master, x, y):
    # Getting subsequent time of each data
    h = get_hour_array()
    # Getting hourly data
    d = getdatabyhour()

    # Sample data for the graphs
    data_sets = [
        {'x': [h[7], h[6], h[5], h[4], h[3], h[2], h[1], h[0]],
         'y': [d[0][0], d[0][1], d[0][2], d[0][3], d[0][4], d[0][5], d[0][6], d[0][7]],
         'label': 'Graph 1'},
        {'x': [h[7], h[6], h[5], h[4], h[3], h[2], h[1], h[0]],
         'y': [d[1][0], d[1][1], d[1][2], d[1][3], d[1][4], d[1][5], d[1][6], d[1][7]],
         'label': 'Graph 2'},
        {'x': [h[7], h[6], h[5], h[4], h[3], h[2], h[1], h[0]],
         'y': [d[2][0], d[2][1], d[2][2], d[2][3], d[2][4], d[2][5], d[2][6], d[2][7]],
         'label': 'Graph 3'}
    ]

    # Create a Figure and a subplot
    fig = Figure(figsize=(6, 4), dpi=80)
    ax = fig.add_subplot(1, 1, 1)

    # Plot the data sets
    for data_set in data_sets:
        ax.plot(data_set['x'], data_set['y'], label=data_set['label'])

    # Set labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Multiple Graphs")

    # Add a legend
    ax.legend()

    # Create a canvas widget
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    frame = tk.Frame(master)
    frame.place(x=x, y=y)
    canvas_widget.master = frame  # Attach the canvas to the frame
    

    return frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Multiple Graph Frames")

    graph_frame = create_graph_frame(root, x=100, y=100)
    # graph_frame2 = create_graph_frame(root, x=10, y=220)  # Adjust the y-coordinate

    root.mainloop()
