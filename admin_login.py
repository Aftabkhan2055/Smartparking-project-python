from tkinter import *
from tkinter.messagebox import *
from connection import *

class password:
    def passw(self):

        db =connection()
        query="select * from admin where Email='"+self.textbox1.get()+"' and passwords='"+self.textbox2.get()+"'"
        cr=db.conn.cursor()
        cr.execute(query)
        p = cr.fetchone()
        x=0
        y=0
        if  p!=None:
            showinfo("","Login Successfull")
        else:
            showerror("","Invalid Login")

    def __init__(self):
        self.root=Tk()
        self.root.title("Login")
        self.root.resizable(0,0)
        self.root.geometry("400x200")

#-============================================================
        top=Frame(self.root)
        top.pack()
        down=Frame(self.root)
        down.pack()
#-=============================================================
        lb=Label(top,text="ADMIN LOGIN",font=("arial",30,"bold","italic"),fg="blue").pack()
#-=============================================================
        lb1 = Label(down,text="Email",font=("arial",10,"bold"),fg="black").grid(row=0, column=0,sticky=(W))
        lb2 = Label(down, text="password",font=("arial",10,"bold"),fg="black").grid(row=1, column=0,sticky=(W))
        self.textbox1 = Entry(down,font=("arial",10),borderwidth=3)
        self.textbox2 = Entry(down,font=("arial",10),borderwidth=3,show="*")
        self.textbox1.grid(row=0, column=1,pady=5,padx=5)
        self.textbox2.grid(row=1, column=1,pady=5,padx=5)
        bt=Button(down, text="Login",command=self.passw,borderwidth=3,width=12,font="bold").grid(row=3, column=1,pady=5,padx=5)
        self.root.mainloop()
#-===================================================================
