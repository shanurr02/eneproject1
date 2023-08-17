import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graphing_Day import getdatabyhour
from timeGenerator import get_hour_array
from graphingWeek import getdatabyweek
from timeGenerator import get_last_7_days

# Getting subsequent time of each data
h= get_hour_array()
# Getting hourlydata
d= getdatabyhour()


# Getting  data for one week
w =getdatabyweek()
# Getting name of last 7 days
nd = get_last_7_days()



def display_graph1():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[0][0], d[0][1], d[0][2], d[0][3], d[0][4], d[0][5], d[0][6], d[0][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("Temp")
    ax.set_title("TEMPERATURE")
    canvas.draw()

def display_graph2():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[1][0], d[1][1], d[1][2], d[1][3], d[1][4], d[1][5], d[1][6], d[1][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("Humidity")
    ax.set_title("HUMIDITY")
    canvas.draw()

def display_graph3():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[2][0], d[2][1], d[2][2], d[2][3], d[2][4], d[2][5], d[2][6], d[2][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("Flow")
    ax.set_title("FLOW")
    canvas.draw()

def display_graph4():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[3][0], d[3][1], d[3][2], d[3][3], d[3][4], d[3][5], d[3][6], d[3][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("Tsp")
    ax.set_title("TSP")
    canvas.draw()

def display_graph5():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[4][0], d[4][1], d[4][2], d[4][3], d[4][4], d[4][5], d[4][6], d[4][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pm_1.0")
    ax.set_title("PM_1.0")
    canvas.draw()

def display_graph6():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[5][0], d[5][1], d[5][2], d[5][3], d[5][4], d[5][5], d[5][6], d[5][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pm_2.5")
    ax.set_title("PM_2.5")
    canvas.draw()

def display_graph7():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[6][0], d[6][1], d[6][2], d[6][3], d[6][4], d[6][5], d[6][6], d[6][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pm_10")
    ax.set_title("PM_10")
    canvas.draw()

def display_graph8():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[7][0], d[7][1], d[7][2], d[7][3], d[7][4], d[7][5], d[7][6], d[7][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_0.3")
    ax.set_title("PQ_0.3")
    canvas.draw()

def display_graph9():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[8][0], d[8][1], d[8][2], d[8][3], d[8][4], d[8][5], d[8][6], d[8][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_0.5")
    ax.set_title("PQ_0.5")
    canvas.draw()

def display_graph10():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[9][0], d[9][1], d[9][2], d[9][3], d[9][4], d[9][5], d[9][6], d[9][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_1.0")
    ax.set_title("PQ_1.0")
    canvas.draw()


def display_graph11():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[10][0], d[10][1], d[10][2], d[10][3], d[10][4], d[10][5], d[10][6], d[10][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_2.5")
    ax.set_title("PQ_2.5")
    canvas.draw()

def display_graph12():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[11][0], d[11][1], d[11][2], d[11][3], d[11][4], d[11][5], d[11][6], d[11][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_5.0")
    ax.set_title("PQ_5.0")
    canvas.draw()

def display_graph13():
    ax.clear()
    ax.plot([h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], [d[12][0], d[12][1], d[12][2], d[12][3], d[12][4], d[12][5], d[12][6], d[12][7]])
    ax.set_xlabel("Time")
    ax.set_ylabel("pq_10")
    ax.set_title("PQ_10")
    canvas.draw()


# Creating Graph for 7 days Data

def display_graph14():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[0][0], w[0][1], w[0][2], w[0][3], w[0][4], w[0][5], w[0][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("temp")
    ax.set_title("TEMPERATURE")
    canvas.draw()

def display_graph15():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[1][0], w[1][1], w[1][2], w[1][3], w[1][4], w[1][5], w[1][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("humidity")
    ax.set_title("HUMIDITY")
    canvas.draw()

def display_graph16():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[2][0], w[2][1], w[2][2], w[2][3], w[2][4], w[2][5], w[2][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("flow")
    ax.set_title("FLOW")
    canvas.draw()

def display_graph17():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[3][0], w[3][1], w[3][2], w[3][3], w[3][4], w[3][5], w[3][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("Tsp")
    ax.set_title("TSP")
    canvas.draw()

def display_graph18():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[4][0], w[4][1], w[4][2], w[4][3], w[4][4], w[4][5], w[4][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pm_1.0")
    ax.set_title("PM_1.0")
    canvas.draw()

def display_graph19():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[5][0], w[5][1], w[5][2], w[5][3], w[5][4], w[5][5], w[5][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pm_2.5")
    ax.set_title("PM_2.5")
    canvas.draw()

def display_graph20():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[6][0], w[6][1], w[6][2], w[6][3], w[6][4], w[6][5], w[6][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pm_10")
    ax.set_title("PM_10")
    canvas.draw()

def display_graph21():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[7][0], w[7][1], w[7][2], w[7][3], w[7][4], w[7][5], w[7][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_0.3")
    ax.set_title("PQ_0.3")
    canvas.draw()

def display_graph22():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[8][0], w[8][1], w[8][2], w[8][3], w[8][4], w[8][5], w[8][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_0.5")
    ax.set_title("PQ_0.5")
    canvas.draw()

def display_graph23():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[9][0], w[9][1], w[9][2], w[9][3], w[9][4], w[9][5], w[9][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_1.0")
    ax.set_title("PQ_1.0")
    canvas.draw()


def display_graph24():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[10][0], w[10][1], w[10][2], w[10][3], w[10][4], w[10][5], w[10][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_2.5")
    ax.set_title("PQ_2.5")
    canvas.draw()

def display_graph25():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[11][0], w[11][1], w[11][2], w[11][3], w[11][4], w[11][5], w[11][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_5.0")
    ax.set_title("PQ_5.0")
    canvas.draw()

def display_graph26():
    ax.clear()
    ax.plot([nd[6], nd[5],nd[4],nd[3],nd[2],nd[1],nd[0]], [w[12][0], w[12][1], w[12][2], w[12][3], w[12][4], w[12][5], w[12][6]])
    ax.set_xlabel("Days")
    ax.set_ylabel("pq_10")
    ax.set_title("PQ_10")
    canvas.draw()


# Create the main application window
root = tk.Tk()
root.title("Dropdown Menu with Graphs")

# Create a Figure and a subplot
fig = Figure(figsize=(7, 4), dpi=70)
ax = fig.add_subplot(1, 1, 1)
# Sample data for the graphs
data_sets = [
    {'x': [h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], 'y': [d[4][0], d[4][1], d[4][2], d[4][3], d[4][4], d[4][5], d[4][6], d[4][7]], 'label': 'PM_1.0'},
    {'x': [h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], 'y': [d[5][0], d[5][1], d[5][2], d[5][3], d[5][4], d[5][5], d[5][6], d[5][7]], 'label': 'PM_2.5'},
    {'x': [h[7], h[6],h[5],h[4],h[3],h[2],h[1],h[0]], 'y': [d[6][0], d[6][1], d[6][2], d[6][3], d[6][4], d[6][5], d[6][6], d[6][7]], 'label': 'PM_10'}
]
# Plot the data sets
for data_set in data_sets:
    ax.plot(data_set['x'], data_set['y'], label=data_set['label'])
ax.set_xlabel("Days")
ax.set_ylabel("pm value")
ax.set_title("All PM Values")
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=410, y=280)

# Create a DropDownMemu1 widget
options = ["Temp", "Humidity", "Flow","TSP", "PM_1.0", "PM_2.5","PM_10", "PQ_0.3", "PQ_0.5","PQ_1.0", "PQ_2.5", "PQ_5.0" , "PQ_10"]
dropdown_var = tk.StringVar()
dropdown_menu = ttk.Combobox(root, textvariable=dropdown_var, values=options,
    font=("Arial", 6), width=10, state="readonly", background="#EFEFEF", foreground="#333333")
dropdown_menu.bind("<<ComboboxSelected>>", lambda event: option_selected(dropdown_var.get(),dropdown_var2.get()))
dropdown_style = ttk.Style()
dropdown_menu.set("AQI-IN")
dropdown_style.configure('TCombobox', padding=6)
dropdown_menu.place(x=430, y=285)  # Placing above the graph


# Create a DropDownMemu2 widget
options2 = ["24 Hours", "7 days"]
dropdown_var2 = tk.StringVar()
dropdown_menu2 = ttk.Combobox(root, textvariable=dropdown_var2, values=options2,
    font=("Arial", 6), width=10, state="readonly", background="#EFEFEF", foreground="#333333")
dropdown_menu2.bind("<<ComboboxSelected>>", lambda event: option_selected(dropdown_var.get(),dropdown_var2.get()))
dropdown_style2 = ttk.Style()
dropdown_menu2.set("Duration")
dropdown_style2.configure('TCombobox', padding=6)
dropdown_menu2.place(x=510, y=285)  # Placing above the graph



# Function to handle option selection
def option_selected(selected_option1, selected_option2):
    # ax.clear()
    if selected_option1 == "Temp" and selected_option2 == "24 Hours":
        display_graph1()
    elif selected_option1 == "Humidity" and selected_option2 == "24 Hours":
        display_graph2()
    elif selected_option1 == "Flow" and selected_option2 == "24 Hours":
        display_graph3()
    elif selected_option1 == "TSP" and selected_option2 == "24 Hours":
        display_graph4()
    elif selected_option1 == "PM_1.0" and selected_option2 == "24 Hours":
        display_graph5()
    elif selected_option1 == "PM_2.5" and selected_option2 == "24 Hours":
        display_graph6()
    elif selected_option1 == "PM_10" and selected_option2 == "24 Hours":
        display_graph7()
    elif selected_option1 == "PQ_0.3" and selected_option2 == "24 Hours":
        display_graph8()
    elif selected_option1 == "PQ_0.5" and selected_option2 == "24 Hours":
        display_graph9()
    elif selected_option1 == "PQ_1.0" and selected_option2 == "24 Hours":
        display_graph10()
    elif selected_option1 == "PQ_2.5" and selected_option2 == "24 Hours":
        display_graph11()
    elif selected_option1 == "PQ_5.0" and selected_option2 == "24 Hours":
        display_graph12()
    elif selected_option1 == "PQ_10" and selected_option2 == "24 Hours":
        display_graph13()
    elif selected_option1 == "Temp" and selected_option2 == "7 days":
        display_graph14()
    elif selected_option1 == "Humidity" and selected_option2 == "7 days":
        display_graph15()
    elif selected_option1 == "Flow" and selected_option2 == "7 days":
        display_graph16()
    elif selected_option1 == "TSP" and selected_option2 == "7 days":
        display_graph17()
    elif selected_option1 == "PM_1.0" and selected_option2 == "7 days":
        display_graph18()
    elif selected_option1 == "PM_2.5" and selected_option2 == "7 days":
        display_graph19()
    elif selected_option1 == "PM_10" and selected_option2 == "7 days":
        display_graph20()
    elif selected_option1 == "PQ_0.3" and selected_option2 == "7 days":
        display_graph21()
    elif selected_option1 == "PQ_0.5" and selected_option2 == "7 days":
        display_graph22()
    elif selected_option1 == "PQ_1.0" and selected_option2 == "7 days":
        display_graph23()
    elif selected_option1 == "PQ_2.5" and selected_option2 == "7 days":
        display_graph24()
    elif selected_option1 == "PQ_5.0" and selected_option2 == "7 days":
        display_graph25()
    elif selected_option1 == "PQ_10" and selected_option2 == "7 days":
        display_graph26()
    
    
# Start the main event loop
root.mainloop()
