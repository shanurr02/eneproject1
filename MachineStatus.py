import tkinter as tk

p = True
def update_buttons_and_remarks():
    if p==True:
        status_button1.config(bg='green')
        status_button2.config(bg='white')
        status_label.config(text="Status: True - Green")
    else:
        status_button1.config(bg='white')
        status_button2.config(bg='red')
        status_label.config(text="Status: False - Red")

app = tk.Tk()
app.title("Status Buttons")

tkvar = tk.DoubleVar()

status_button1 = tk.Button(app, text="Status 1", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
status_button2 = tk.Button(app, text="Status 2", width=10, height=2, bg='white', relief="solid", command=update_buttons_and_remarks)
status_label = tk.Label(app, text="Status: -", font=("Helvetica", 12, "bold"))

status_button1.place(x=50, y=50)
status_button2.place(x=50, y=120)
status_label.place(x=50, y=190)

update_buttons_and_remarks()  # Initialize button colors and remarks based on the initial status

app.mainloop()
