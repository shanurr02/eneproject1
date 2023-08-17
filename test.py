import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar  # Make sure to install the 'tkcalendar' package

def get_selected_dates():
    try:
        date1 = date_var1.get()
        date2 = date_var2.get()
        return date1, date2
    except ValueError:
        return None, None

def open_calendar(button, variable):
    cal_window = tk.Toplevel(app)
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
        data = f"Downloaded data from {date1} to {date2}"
        messagebox.showinfo("Download", data)

app = tk.Tk()
app.title("Date Selection and Data Download")

date_var1 = tk.StringVar()
date_var2 = tk.StringVar()

# date_label1 = tk.Label(app, text="Select Date 1:")
# date_label2 = tk.Label(app, text="Select Date 2:")

date_entry1 = ttk.Entry(app, textvariable=date_var1, state="readonly")
date_entry2 = ttk.Entry(app, textvariable=date_var2, state="readonly")

select_button1 = tk.Button(app, text="Select", command=lambda: open_calendar(select_button1, date_var1))
select_button2 = tk.Button(app, text="Select", command=lambda: open_calendar(select_button2, date_var2))
download_button = tk.Button(app, text="Download Data", command=download_data)

select_button1.place(x=1030, y=245)
select_button2.place(x=1180, y=245)
date_entry1.place(x=1030, y=275)
date_entry2.place(x=1180, y=275)
# select_button1.place(x=350, y=45)
# select_button2.place(x=350, y=95)
download_button.place(x=1110, y=320)

app.mainloop()



# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from tkcalendar import Calendar  # Make sure to install the 'tkcalendar' package

# def get_selected_dates():
#     try:
#         date1 = date_var1.get()
#         date2 = date_var2.get()
#         return date1, date2
#     except ValueError:
#         return None, None

# def open_calendar_1():
#     cal_window = tk.Toplevel(app)
#     cal_window.title("Select Date 1")
#     date_cal1 = Calendar(cal_window, selectmode="day", date_pattern="yyyy-mm-dd")
#     date_cal1.pack()
#     ok_button = tk.Button(cal_window, text="OK", command=lambda: set_selected_date(date_cal1, date_var1, cal_window))
#     ok_button.pack()

# def open_calendar_2():
#     cal_window = tk.Toplevel(app)
#     cal_window.title("Select Date 2")
#     date_cal2 = Calendar(cal_window, selectmode="day", date_pattern="yyyy-mm-dd")
#     date_cal2.pack()
#     cal_window.place(x=1180, y = 280)
#     ok_button = tk.Button(cal_window, text="OK", command=lambda: set_selected_date(date_cal2, date_var2, cal_window))
#     ok_button.pack()

# def set_selected_date(calendar, variable, window):
#     selected_date = calendar.get_date()
#     variable.set(selected_date)
#     window.destroy()

# def download_data():
#     date1, date2 = get_selected_dates()
#     if date1 is None or date2 is None:
#         messagebox.showerror("Error", "Invalid date format")
#     else:
#         # Replace this with your actual data download function
#         data = f"Downloaded data from {date1} to {date2}"
#         messagebox.showinfo("Download", data)

# app = tk.Tk()
# app.title("Date Selection and Data Download")

# date_var1 = tk.StringVar()
# date_var2 = tk.StringVar()

# # date_label1 = tk.Label(app, text="Select Date 1:")
# # date_label2 = tk.Label(app, text="Select Date 2:")

# date_entry1 = ttk.Entry(app, textvariable=date_var1, state="readonly")
# date_entry2 = ttk.Entry(app, textvariable=date_var2, state="readonly")

# select_button1 = tk.Button(app, text="Select Start Date", command=open_calendar_1)
# select_button2 = tk.Button(app, text="Select End Date", command=open_calendar_2)
# download_button = tk.Button(app, text="Download Data", command=download_data)

# select_button1.place(x=1030, y=245)
# select_button2.place(x=1180, y=245)
# date_entry1.place(x=1030, y=275)
# date_entry2.place(x=1180, y=275)
# # select_button1.place(x=350, y=45)
# # select_button2.place(x=350, y=95)
# download_button.place(x=110, y=320)

# app.mainloop()
