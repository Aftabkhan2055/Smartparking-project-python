from tkinter import *
import tkinter.ttk
from connection import *

class table:

    def __init__(self):
        #-===================================================================================
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.title("Data Table")
        self.root.configure(background="skyblue")
        #-=====================================================================================
        lb=Label(self.root,text="VIEW ADMIN",font=("arial",20,"bold"),fg="brown",bg="skyblue")
        lb.pack()
        #-======================================================================================
        self.t=tkinter.ttk.Treeview(self.root, column=("email","Mobile","type"))
        self.t.heading("email", text="Email")
        self.t.heading("Mobile", text="Mobile")
        self.t.heading("type", text="Type")

        query= "Select email, mobile,type from admin"
        db = connection()
        cr = db.conn.cursor()

        cr.execute(query)

        p = cr.fetchall()

        for i in range(0,len(p)):
            self.t.insert("", value=p[i], index=i)

        self.t.pack()
        self.t.column("#0", width=0)
        self.t.column("type",width=130)
        self.t.column("Mobile",width=130)
        self.root.mainloop()
#-=========================================================================================
