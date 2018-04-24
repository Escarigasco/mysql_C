import tkinter as tk
from query_handler import query_handler


class GUI(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        self.L1 = tk.Label(self, text="Insert Start Date YYYY-MM-DD")
        self.L1.grid(row=0, column=0)
        self.E1 = tk.Entry(self)
        self.E1.grid(row=0, column=1)

        self.L2 = tk.Label(self, text="Insert End Date YYYY-MM-DD")
        self.L2.grid(row=1, column=0)
        self.E2 = tk.Entry(self)
        self.E2.grid(row=1, column=1)

        self.L3 = tk.Label(self, text="Insert Additional Info")
        self.L3.grid(row=2, column=0)
        self.E3 = tk.Entry(self)
        self.E3.grid(row=2, column=1)

        self.L4 = tk.Label(self, text="Insert Email Address")
        self.L4.grid(row=3, column=0)
        self.E4 = tk.Entry(self)
        self.E4.grid(row=3, column=1)

        self.button = tk.Button(self, text="Select", command=self.on_button)
        self.button.grid()

    def on_button(self):  # you have to make this method private
        qh = query_handler()
        start_date = str(self.E1.get())
        end_date = str(self.E2.get())
        info = str(self.E3.get())
        address = str(self.E4.get())
        print(start_date)
        print(end_date)
        qh.run(start_date, end_date, address, info)
        del qh


app = GUI()
app.mainloop()  # this can't be in the main because it stays looping, it doesn't exit this method as it s the one keeps alive the GUI
print(app.get_parameters)
