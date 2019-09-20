from tkinter import *
import tkinter.ttk as ttk
from pymysql import *
from tkinter.messagebox import *
from connection import *

class rate:
    def check(self):
        db=connection()
        query="select * from rate where vehciletype='"+self.cbvechicle.get()+"'and parkingtype='"+self.cbparking.get()+"'"
        cr = db.conn.cursor()
        cr.execute(query)
        p = cr.fetchone()
        if p != None:
            showerror("", "allready exist")
        else:
            self.submit()

    def submit(self):
        if self.cbvechicle.get()=="" or self.cbparking.get()=="" or self.tbprice.get()=="":
            showerror("","All Field are mandatory")
        else:
            dr=connection()
            query="insert into rate value (null,'"+self.cbvechicle.get()+"','"+self.cbparking.get()+"',"+self.tbprice.get()+")"
            cr = dr.conn.cursor()
            cr.execute(query)
            dr.conn.commit()
            showinfo("", "add sucess")
            self.tbprice.delete(0, END)

    def __init__(self):

        self.root = Tk()
        self.root.title("Rate")
        self.root.geometry("320x200")
        lb = Label(self.root,text="RATES",font=("Arial",30,"bold"),fg="blue")
        lb.grid(row=0, column=0, columnspan=2)

        lb1 = Label(self.root, text="Vechicle_Type",font=("arial",8,"bold"),fg="brown").grid(row=1,column=0,sticky=(W))
        lb2 = Label(self.root, text="Parking_Type",font=("arial",8,"bold"),fg="brown").grid(row=2, column=0,sticky=(W))
        lb3 = Label(self.root, text="Price",font=("arial",8,"bold"),fg="brown").grid(row=3, column=0,sticky=(W))

        self.cbvechicle=ttk.Combobox(self.root,width=30,state="readonly",value=("Two Wheeler Light Vechicle","Two Wheeler Heavy Vechicle","Four Wheeler Light Vechicle","Four Wheeler Heavy Vechicle",))
        self.cbparking=ttk.Combobox(self.root,width=30,state="readonly",value=("Full day","12 Hour","6 Hour","3 Hour"))
        self.tbprice=Entry(self.root,width=30)
        self.cbvechicle.grid(row=1, column=1,sticky=(E,W,N),pady=5,padx=5)
        self.cbparking.grid(row=2, column=1,sticky=(E,W,N),pady=5,padx=5)
        self.tbprice.grid(row=3,column=1,sticky=(E,W,N),pady=5,padx=5)
        bt=Button(self.root,text="ADD",command=self.check,width=10,borderwidth=3,font=("arial",10,"bold")).grid(row=4, column=1,pady=5,padx=5)

        self.root.mainloop()
#-===============================================================
