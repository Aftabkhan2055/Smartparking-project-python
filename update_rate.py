from tkinter import *
from connection import *
from tkinter.messagebox import *
import tkinter.ttk as ttk

class uupdate:
    def search(self):
        db = connection()
        cr = db.conn.cursor()
        query = "select * from rate where rateid=" + self.cbseries.get()
        cr.execute(query)
        p = cr.fetchone()
        if p!=None:
            self.tbprice.delete(0, END)
            self.cbvechicle.set(p[1])
            self.cbparking.set(p[2])
            self.tbprice.insert(0, p[3])
        else:
            showerror("","Rateid Does not exist")
    def uuupdate(self):
        if self.cbvechicle.get()=="" or self.cbparking.get()=="" or self.tbprice.get()=="":
            showerror("","All Fields are mandatory")
        else:
            query="UPDATE rate SET vehciletype='"+self.cbvechicle.get()+"',parkingtype='"+self.cbparking.get()+"',price="+self.tbprice.get()+" WHERE vehciletype='"+self.cbvechicle.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("", "Update is Success")

    def delete(self):
        if self.cbseries.get() == "":
            showerror("", "Rateid Fields is Empty")
        else:
            query = "delete from rate where rateid=" + self.cbseries.get()
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query)
            db.conn.commit()
            showinfo("", "delete is sucess")
            self.getrates()
    def getrates(self):
        db = connection()
        cr = db.conn.cursor()
        s = "select rateid from rate order by rateid"
        cr.execute(s)
        p = cr.fetchall()
        lst = []
        for i in range(0, len(p)):
            lst.append(p[i][0])
        self.cbseries.config(values=tuple(lst))
    def __init__(self):
        self.root = Tk()
        self.root.title("Rate")
        self.root.geometry("410x250")
        # -============================================================================================================
        lb = Label(self.root,text="RATE",font=("Arial",30,"bold"),fg="red")
        lb.grid(row=0, column=0, columnspan=2)
        # -=============================================================================================================
        lb1 = Label(self.root, text="Rate ID", font=("arial", 8, "bold"), fg="brown").grid(row=1, column=0,sticky=(W))
        lb1 = Label(self.root, text="Vechicle_Type",font=("arial",8,"bold"),fg="brown").grid(row=2,column=0,sticky=(W))
        lb2 = Label(self.root, text="Parking_Type",font=("arial",8,"bold"),fg="brown").grid(row=3, column=0,sticky=(W))
        lb3 = Label(self.root, text="Price",font=("arial",8,"bold"),fg="brown").grid(row=4, column=0,sticky=(W))
        # -===============================================================================================================
        self.cbvechicle=ttk.Combobox(self.root,width=30,state="readonly",value=("Two Wheeler Light Vechicle","Two Wheeler Heavy Vechicle","Two Wheeler Light Vechicle","Four Wheeler Heavy Vechicle",))
        self.cbparking=ttk.Combobox(self.root,width=30,state="readonly",value=("Full day","12 Hour","6 Hour","3 Hour"))
        self.cbseries=ttk.Combobox(self.root,width=30,state="readonly")
        self.tbprice=Entry(self.root,width=30)
        # -=================================================================================================================
        self.cbseries.grid(row=1, column=1)
        self.cbvechicle.grid(row=2, column=1,sticky=(E,W,N),pady=5,padx=5)
        self.cbparking.grid(row=3, column=1,sticky=(E,W,N),pady=5,padx=5)
        self.tbprice.grid(row=4,column=1,sticky=(E,W,N),pady=5,padx=5)
        self.getrates()
        bt=Button(self.root,text="UPDATE",width=10,borderwidth=3,font=("arial",10,"bold"),command=self.uuupdate).grid(row=4, column=2,pady=5,padx=5)
        bt = Button(self.root, text="DELETE", width=10, borderwidth=3, font=("arial", 10, "bold"),command=self.delete).grid(row=6, column=1,pady=5, padx=5)
        bt = Button(self.root, text="Search", width=10, borderwidth=3, font=("arial", 10, "bold"),command=self.search).grid(row=3, column=2, pady=5, padx=5)

        self.root.mainloop()

