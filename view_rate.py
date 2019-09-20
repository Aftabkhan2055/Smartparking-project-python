from tkinter import *
import tkinter.ttk as ttk
from connection import *

class view:
    def __init__(self):
        self.root=Tk()
        self.root.configure(background="skyblue")
        self.root.resizable(0,0)
        lb=Label(self.root,text="VIEW RATE",font=("arial",20,"bold"),fg="blue",bg="skyblue")
        lb.grid(row=0,column=0)

        tree=ttk.Treeview(self.root, column=("rateid","vechicle","type","price"))
        tree.heading("rateid",text="Rate_id")
        tree.heading("vechicle",text="Vechicle_Type")
        tree.heading("type",text="parking_type")
        tree.heading("price",text="Price")
        dr=connection()
        query = "Select * from rate"
        cr=dr.conn.cursor()
        cr.execute(query)
        p = cr.fetchall()

        for i in range(0, len(p)):
            tree.insert("", value=p[i], index=i)

        tree.grid(row=1,column=0)
        tree.column("#0",width=0)
        tree.column("price",width=100)
        self.root.mainloop()
#-======================================================================================
