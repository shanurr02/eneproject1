import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors

def on_hover(event):
    if event.xdata and event.ydata:
        ax.set_xlim(event.xdata - 1, event.xdata + 1)
        ax.set_ylim(event.ydata - 10, event.ydata + 10)
        canvas.draw()

root = tk.Tk()
root.geometry("800x600")

fig = Figure(figsize=(7, 4), dpi=70)
ax = fig.add_subplot(1, 1, 1)

# Sample data and other code...

# Plot the data sets...
# ... (same as before)

ax.set_xlabel("Days")
ax.set_ylabel("pm value")
ax.set_title("All PM Values")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=10, y=10)

mplcursors.cursor(hover=True).connect("add", on_hover)

# Create DropDownMenu1 widget...
# ... (same as before)

# Create DropDownMenu2 widget...
# ... (same as before)

root.mainloop()
