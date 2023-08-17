import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from get_data import get_data
from login_api import loginrequest
from graphing_Day import getdatabyhour
from status import check_last_recorded_time_within_1_minute
from graphing_Day import getdatabyhour
from timeGenerator import get_hour_array
from graphingWeek import getdatabyweek
from timeGenerator import get_last_7_days
from download_data import savedataincsv


loginrequest()





#Function End
print(datetime.now().strftime('%A, %d %B %Y\n'))
print("LOADING, PLEASE WAIT...\n")

# CREATE WINDOW - RESIZE FALSE - SIZE - TITLE CARD
root = tk.Tk()
root.resizable(False, False)
root.geometry('1305x780')
root.title("Dashboard")
root.configure(bg='#c7d5e0')

# ----------------------------TOP BLUE BAR - DRAW TITLE -  DRAW DATE TIME-------------------------------
top_bg = tk.Canvas(root, width=1305, height=60, bg='#1b2838', highlightthickness=0).place(x=0, y=0)
tk.Label(top_bg, text='Dashboard', font='Montserrat 25', bg='#1b2838', fg='white').place(x=15, y=3)
tk.Label(top_bg, text=datetime.now().strftime('%A, %d %B %Y'), font='Montserrat 20', bg='#1b2838', fg='white').place(
    x=930, y=8)






# ---------------------------------Updates--------------------------------------------------------------------
updates = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=620)
news_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=600)
tk.Label(news_box_top, text='Updates', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=25, y=600)



# ---------------------------------Downloads------------------------------------------------------------------
Downloads = tk.Canvas(root, width=285, height=120, bg='#2a475e', highlightthickness=0).place(x=1000, y=240)
Downloads_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=220)
tk.Label(Downloads_top, text='Downloads', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=1005, y=220)


def get_selected_dates():
    try:
        date1 = date_var1.get()
        date2 = date_var2.get()
        return date1, date2
    except ValueError:
        return None, None

def open_calendar(button, variable):
    cal_window = tk.Toplevel(root)
    cal_window.title("Select Date")
    cal_window.geometry("+%d+%d" % (button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()))
    date_cal = Calendar(cal_window, selectmode="day", date_pattern="yyyy-mm-dd")
    date_cal.pack()
    ok_button = tk.Button(cal_window, text="OK", command=lambda: set_selected_date(date_cal, variable, cal_window))
    ok_button.pack()

def set_selected_date(calendar, variable, window):
    selected_date = calendar.get_date()
    variable.set(selected_date)
    window.destroy()

def download_data():
    date1, date2 = get_selected_dates()
    if date1 is None or date2 is None:
        messagebox.showerror("Error", "Invalid date format")
    else:
        # Replace this with your actual data download function
        savedataincsv(str(date1),str(date2))
        data = f"Downloaded data from {date1} to {date2}"
        messagebox.showinfo("Download", data)



date_var1 = tk.StringVar()
date_var2 = tk.StringVar()



date_entry1 = ttk.Entry(root, textvariable=date_var1, state="readonly")
date_entry2 = ttk.Entry(root, textvariable=date_var2, state="readonly")

select_button1 = tk.Button(root, text="Select Start Date", command=lambda: open_calendar(select_button1, date_var1))
select_button2 = tk.Button(root, text="Select End Date", command=lambda: open_calendar(select_button2, date_var2))
# date1, date2 = get_selected_dates()
download_button = tk.Button(root, text="Download Data", command=download_data)

select_button1.place(x=1030, y=245)
select_button2.place(x=1180, y=245)
date_entry1.place(x=1030, y=275)
date_entry2.place(x=1180, y=275)
# select_button1.place(x=350, y=45)
# select_button2.place(x=350, y=95)
download_button.place(x=1110, y=320)





















# ---------------------------------Settings------------------------------------------------------------------
Settings = tk.Canvas(root, width=285, height=120, bg='#2a475e', highlightthickness=0).place(x=1000, y=400)
Settings_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=380)
tk.Label(Settings_top, text='Settings', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=1005, y=380)




# ---------------------------------Company------------------------------------------------------------------
Company = tk.Canvas(root, width=285, height=120, bg='#2a475e', highlightthickness=0).place(x=1000, y=560)
Company_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=540)
tk.Label(Company_top, text='Company', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=1005, y=540)






# ----------------------------------Graphs--------------------------------------------------------------
Graphs = tk.Canvas(root, width=590, height=520, bg='#2a475e', highlightthickness=0).place(x=390, y=240)
Graphs_top1 = tk.Canvas(root, width=590, height=20, bg='#1b2838', highlightthickness=0).place(x=390, y=220)
tk.Label(Graphs_top1, text='Graphs', font='Montserrat 7 bold', bg='#1b2838',fg='#FFFFFF').place(x=395, y=220)

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
    














#----------------Download Button2 in Downloads frame----------------------------------------------
def save_graph_as_image():
    file_path = "graph_image.png"
    canvas_agg = FigureCanvasAgg(fig)
    canvas_agg.print_png(file_path)
    print(f"Graph image saved as {file_path}")


button2 = tk.Button(root, text="Download", command=save_graph_as_image,
                   font=("Arial", 5), height=2, width=10, 
                   fg="white", bg="blue")
button2.place(x=870 , y=660)

















# -----------------Download button in Graph Bottom Corner----------------------

def download_button_clicked():
    # Add your download logic here
    print("Download button clicked")


download_button = tk.Button(root, text="Download", command=download_button_clicked, 
                            font=("Arial", 6), width=10, 
                            background="#EFEFEF", foreground="#333333")
download_button.place(x=60, y=140)









# ----------------------------------AQI---------------------------------------------------------------------

aqi = tk.Canvas(root, width=1265, height=100, bg='#2a475e', highlightthickness=0 ).place(x=20, y=100)
aqi_top = tk.Canvas(root, width=1265, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=80)
latest_data = get_data()


def update_label():
    # loginrequest()
    latest_data = get_data()
    p = check_last_recorded_time_within_1_minute()
    # p = False
    tk.Label(root, text=latest_data[4], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=95, y=130)
    tk.Label(root, text=latest_data[5], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=195, y=130)
    tk.Label(root, text=latest_data[6], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=295, y=130)
    tk.Label(root, text=latest_data[3], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=395, y=130)
    tk.Label(root, text=latest_data[7], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=495, y=130)
    tk.Label(root, text=latest_data[8], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=595, y=130)
    tk.Label(root, text=latest_data[9], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=695, y=130)
    tk.Label(root, text=latest_data[10], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=795, y=130)
    tk.Label(root, text=latest_data[11], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=895, y=130)
    tk.Label(root, text=latest_data[12], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=995, y=130)
    tk.Label(root, text=latest_data[2], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=1095, y=130)
    tk.Label(root, text=latest_data[0], font='Montserrat 8 bold', bg='#1b9838', fg='#FFFFFF').place(x=1195, y=130)

    # Status code 
    status_button1 = tk.Button(root, text="ON", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
    status_button2 = tk.Button(root, text="OFF", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
    status_label = tk.Label(root, text="Status: -", font='Montserrat 9 bold', bg='#2a475e', fg='#FFFFFF')
    update_buttons_and_remarks(p)
    # Call this function again after 100 milliseconds
    root.after(100, update_label)

    

tk.Label(root, text=latest_data[4], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=95, y=130)
tk.Label(root, text=latest_data[5], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=195, y=130)
tk.Label(root, text=latest_data[6], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=295, y=130)
tk.Label(root, text=latest_data[3], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=395, y=130)
tk.Label(root, text=latest_data[7], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=495, y=130)
tk.Label(root, text=latest_data[8], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=595, y=130)
tk.Label(root, text=latest_data[9], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=695, y=130)
tk.Label(root, text=latest_data[10], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=795, y=130)
tk.Label(root, text=latest_data[11], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=895, y=130)
tk.Label(root, text=latest_data[12], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=995, y=130)
tk.Label(root, text=latest_data[2], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=1095, y=130)
tk.Label(root, text=latest_data[0], font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=1195, y=130)

aqi1 = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=80, y=120)
tk.Label(root, text="PM_1", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=80, y=165)

aqi2  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=180, y=120)
tk.Label(root, text="PM_2.5", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=180, y=165)

aqi3 = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=280, y=120)
tk.Label(root, text="PM_10", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=280, y=165)


aqi4  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=380, y=120)
tk.Label(root, text="TSP", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=380, y=165)

aqi5  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=480, y=120)
tk.Label(root, text="PQ_0.3", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=480, y=165)


aqi6  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=580, y=120)
tk.Label(root, text="PQ_0.5", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=580, y=165)

aqi7  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=680, y=120)
tk.Label(root, text="PQ_1.0", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=680, y=165)
 
aqi8  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=780, y=120)
tk.Label(root, text="PQ_2.5", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=780, y=165)

aqi9  = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=880, y=120)
tk.Label(root, text="PQ_5.0", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=880, y=165)


aqi10 = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=980, y=120)
tk.Label(root, text="PQ_10", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=980, y=165)

aqi11 = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=1080, y=120)
tk.Label(root, text="Flow", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=1080, y=165)


aqi12 = tk.Canvas(root, width=50, height=40, bg='#1b9838', highlightthickness=0).place(x=1180, y=120)
tk.Label(root, text="Temp", font='Montserrat 8 bold', bg='#2a475e', fg='#FFFFFF').place(x=1180, y=165)


tk.Label(aqi_top, text='AQI Parameters', font='Montserrat 7 bold', bg='#1b2838',fg='#FFFFFF').place(x=25, y=80)
    











# ------------------------------MachineStatus ------------------------------------------------------------------------



MachineStatus = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
MachineStatus_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=220)
MachineStatus_temp = tk.Canvas(MachineStatus, width=350, height=30, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
MachineStatus_middle = tk.Canvas(MachineStatus, width=350, height=20, bg='#171a21', highlightthickness=0).place(x=20, y=300)
tk.Label(MachineStatus_top, text='Machine Status', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=25, y=220)
tk.Label(MachineStatus_middle, text='Remarks', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF').place(x=25, y=300)


p = check_last_recorded_time_within_1_minute()
# p = False
def update_buttons_and_remarks(p):
    if p==True:
        status_button1.config(bg='green')
        status_button2.config(bg='white')
        status_label.config(text="Status: Machine is ON and Data is Coming")
    else:
        status_button1.config(bg='white')
        status_button2.config(bg='red')
        status_label.config(text="Status: Machine is OFF and Data is not Coming Contact \nto Company (Phone no. 1947)")


status_button1 = tk.Button(root, text="ON", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
status_button2 = tk.Button(root, text="OFF", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
status_label = tk.Label(root, text="Status: -", font='Montserrat 9 bold', bg='#2a475e', fg='#FFFFFF')
status_button1.place(x=50, y=250)
status_button2.place(x=210, y=250)
status_label.place(x=30, y=330)

# update_buttons_and_remarks(p)










# -------------------------------AQIlevel---------------------------------------------------------------------------


AQIlevel = tk.Canvas(root, width=350, height=160, bg='#2a475e', highlightthickness=0).place(x=20, y=420)
AQIlevel_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=400)
tk.Label(AQIlevel_top, text='AQI', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF') \
    .place(x=25, y=400)

tk.Label(AQIlevel, text="Current", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=425)
tk.Label(AQIlevel, text="Yesterday", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=455)
tk.Label(AQIlevel, text="2 days Ago", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=485)
tk.Label(AQIlevel, text="1 Week Ago", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=515)
tk.Label(AQIlevel, text="Previous Month", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=545)

tk.Canvas(AQIlevel, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=175, y=430)
tk.Canvas(AQIlevel, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=175, y=460)
tk.Canvas(AQIlevel, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=175, y=490)
tk.Canvas(AQIlevel, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=175, y=520)
tk.Canvas(AQIlevel, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=175, y=550)

#----------------------------------------------------------------------------------------------------------------


print('\nDRAWING DASHBOARD')
# MAINLOOP
update_label()
root.mainloop()

# BGCOLOUR #aeccd0
# BOXCOLOR #20639B
