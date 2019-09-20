from tkinter import *
from tkinter.messagebox import *
import tkinter.ttk as ttk
from connection import *

class uupdate:
#-==================================================================================================
    def search(self):
        if self.textbox1.get()=="":
            showerror("","Enter Your Email")
        elif not (str(self.textbox1.get()).count("@")==1 and str(self.textbox1.get()).count(".")>=1):
            showerror("","Email is not valid",parent=self.root)
        else:
            db = connection()
            cr = db.conn.cursor()
            query = "select * from admin where email='" + self.textbox1.get() + "'"
            cr.execute(query)
            p = cr.fetchone()
            if p!=None:
                self.textbox2.delete(0,END)
                self.textbox2.insert(0,p[2])
                self.cb1.set(p[3])
            else:
                showerror("","Invalid Email",parent=self.root)
#-===================================================================================================================================================================================
    def udate(self):
        if self.textbox1.get()=="" or self.textbox2.get()=="" or self.cb1.get()=="":
            showerror("","All Fields are mandatory")
        else:
            query="UPDATE admin SET email='"+self.textbox1.get()+"',passwords='"+self.textbox2.get()+"',type='"+self.cb1.get()+"' WHERE email='"+self.textbox1.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("", "Update is Success")
#-==========================================================================================================================================================================================
    def delete(self):
        if self.textbox1.get()=="" or self.textbox2.get()=="" or self.cb1.get()=="":
            showerror("","All Fields are Empty")
        else:
            query="delete from admin where email='"+self.textbox1.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("","delete is sucess")
    def __init__(self):
        self.root=Tk()
        self.root.title("Update")
        self.root.geometry("300x150")
        self.root.resizable(0,0)
        #-===========================================================================================
        lb=Label(self.root,text="ADMIN UPDATE",font=("arial",15,"bold"),fg="brown")
        lb.grid(row=0,column=1,columnspan=3)
        #-===========================================================================================
        lb1=Label(self.root, text="Email",fg="brown").grid(row=1, column=0,sticky=(W))
        lb4=Label(self.root, text="Mobile",fg="brown").grid(row=2, column=0,sticky=(W))
        lb5=Label(self.root, text="Type",fg="brown").grid(row=3, column=0,sticky=(W))
        self.cb1 = ttk.Combobox(self.root, value=("Admin", "Limited Use"), state="readonly")
        #-=============================================================================================
        self.textbox1=Entry(self.root)
        self.textbox2 = Entry(self.root)
        #-=============================================================================================
        bt1=Button(self.root, text="Search", command=self.search,width=12).grid(row=1, column=2)
        bt1=Button(self.root, text="Update", command=self.udate,width=12).grid(row=5, column=1)
        bt1=Button(self.root, text="Delete", command=self.delete,width=12).grid(row=3, column=2)
        #-=============================================================================================
        self.textbox1.grid(row=1, column=1,pady=5,padx=5,sticky=(W,E,N))
        self.textbox2.grid(row=2, column=1,pady=5,padx=5,sticky=(W,E,N))
        self.cb1.grid(row=3, column=1,pady=5,padx=5,sticky=(W,E,N))
        #-=============================================================================================
        self.root.mainloop()
#-===================================================================
