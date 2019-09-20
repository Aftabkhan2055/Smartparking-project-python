import tkinter.ttk as ttk
from tkinter import *
from connection import *
from datetime import *
from tkinter.messagebox import *

class exit:
    def update(self):
        if self.vnumber.get()=="" or self.cbvechicle.get()=="" or self.cbparking.get()=="" or self.price=="" or self.parking_location=="" or self.parking_location.get()=="" or self.mobile.get()=="":
            showerror("","All Fields are mandatory")
        else:
            dr=connection()
            query="UPDATE `parking_ticket` SET `dateofexit`='"+self.dateofexit.get()+"',`timeofexit`='"+self.timeofexit.get()+"' WHERE vehicle_number='"+self.vnumber.get()+"'"

            cr = dr.conn.cursor()
            cr.execute(query)
            dr.conn.commit()
            showinfo("","exit")

            self.dateofentry.delete(0, END)
            self.price.delete(0, END)
            self.parking_location.delete(0, END)
            self.mobile.delete(0, END)
            self.vnumber.delete(0,END)
            self.timeofexit.delete(0,END)
            self.dateofexit.delete(0,END)
            self.cbparking.set('')
            self.cbvechicle.set('')
            self.timeofentry.delete(0,END)

    def search(self):
        if self.vnumber.get()=="":
            showwarning("","Enter vehicle number!!!")
        else:
            dr=connection()
            query="select * from parking_ticket where Vehicle_Number='"+self.vnumber.get()+"'"
            cr=dr.conn.cursor()
            cr.execute(query)
            p=cr.fetchone()
            self.dateofentry.delete(0, END)
            self.price.delete(0, END)
            self.parking_location.delete(0,END)
            self.mobile.delete(0,END)

            self.cbvechicle.set(p[2])
            self.cbparking.set(p[3])
            self.price.insert(0,p[4])
            self.parking_location.insert(0,p[5])
            self.dateofentry.insert(0,p[6])
            self.timeofentry.insert(0,p[7])
            self.mobile.insert(0,p[8])
    def __init__(self):
        self.root = Tk()
        self.root.title("Exit Ticket")
        self.root.geometry("400x400")
        # -=================================================================================
        top = Frame(self.root, width=100)
        top.pack()
        down = Frame(self.root)
        down.pack()
        # -====================================================================================
        lb = Label(top, text="EXIT TICKET", font=("Britannic Bold", 25, "italic", "underline"), fg="blue").pack()
        # -=====================================================================================

        lb = Label(down, text="Vehicle_Number", font=('arial', 10, "bold"), fg="brown").grid(row=1, column=0, sticky=(W))
        lb = Label(down, text="Vehicle_Type", font=('arial', 10, "bold"), fg="brown").grid(row=2, column=0, sticky=(W))
        lb = Label(down, text="Parking_Type", font=('arial', 10, "bold"), fg="brown").grid(row=3, column=0, sticky=(W))
        lb = Label(down, text="Price", font=('arial', 10, "bold"), fg="brown").grid(row=4, column=0, sticky=(W))
        lb = Label(down, text="parking_location", font=('arial', 10, "bold"), fg="brown").grid(row=5, column=0, sticky=(W))
        lb = Label(down, text="Date_Of_Entry", font=('arial', 10, "bold"), fg="brown").grid(row=6, column=0, sticky=(W))
        lb = Label(down, text="Time_of_Entry", font=('arial', 10, "bold"), fg="brown").grid(row=7, column=0, sticky=(W))
        lb = Label(down, text="Date_Of_Exit", font=('arial', 10, "bold"), fg="brown").grid(row=8, column=0, sticky=(W))
        lb = Label(down, text="Time_of_Exit", font=('arial', 10, "bold"), fg="brown").grid(row=9, column=0, sticky=(W))
        lb = Label(down, text="mobile", font=('arial', 10, "bold"), fg="brown").grid(row=10, column=0, sticky=(W))

        lb = Label(down, text="Remarksifany", font=('arial', 10, "bold"), fg="brown").grid(row=11, column=0, sticky=(W))

        self.vnumber = Entry(down)
        self.cbvechicle = ttk.Combobox(down, width=30, state="readonly")
        #("Two Wheeler Light Vechicle", "Two Wheeler Heavy Vechicle", "Two Wheeler Light Vechicle","Four Wheeler Heavy Vechicle",
        self.cbparking = ttk.Combobox(down, width=30, state="readonly",
                                      value=("Full day", "12 Hour", "6 Hour", "3 Hour"))
        self.ptype = Entry(down)
        self.price = Entry(down)
        self.parking_location = Entry(down)
        self.dateofentry = Entry(down)
        self.timeofentry = Entry(down)
        self.dateofexit = Entry(down)
        self.timeofexit = Entry(down)
        self.mobile = Entry(down)
        self.remarksifany = Entry(down)

        self.vnumber.grid(row=1, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.cbvechicle.grid(row=2, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.cbparking.grid(row=3, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.price.grid(row=4, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.parking_location.grid(row=5, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.dateofentry.grid(row=6, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.timeofentry.grid(row=7, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.dateofexit.grid(row=8, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.timeofexit.grid(row=9, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.mobile.grid(row=10, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.remarksifany.grid(row=11, column=1, padx=5, pady=5, sticky=(E, N, W))
        #-====================================================================================================================
        self.currentdate = datetime.now().strftime("%Y-%m-%d")
        self.currenttime = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(
            datetime.now().second)
        self.dateofentry.delete(0, END)
        self.timeofentry.delete(0, END)
        self.dateofexit.insert(0, self.currentdate)
        self.timeofexit.insert(0, self.currenttime)
        # -===================================================================================================================
        bt = Button(down, text="Submit", font=('arial', 10, "bold"), borderwidth=3,command=self.update ).grid(row=10,column=2)
        bt = Button(down, text="Find", font=('arial', 10, "bold"), borderwidth=3,command=self.search ).grid(row=6,column=2)

        self.root.mainloop()
#-================================================================================================================================
