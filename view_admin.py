from pymysql import *
from tkinter.ttk import *
from tkinter import *
from connection import *
class view:

    def __init__(self):
        self.root = Tk()
        self.root.title("view admin")
        self.root.config(bg='light gray')
        self.lb_heading=Label(self.root,text="view admin")
        labelfont=('Arial',20,'bold')
        self.lb_heading.configure(foreground='brown',background='light gray',font=labelfont)



        self.lb_heading.pack()
        self.t = Treeview(self.root,columns=("email", "password", "mobile","type"))
        self.t.heading("email", text="Emailid")
        self.t.heading("password", text="Password")
        self.t.heading("mobile", text="Mobile number")
        self.t.heading("type", text="type")



        query = "select * from admin"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query)

        p = cr.fetchall()

        for i in range(0, len(p)):
            self.t.insert("", values=p[i], index=i)
        self.t.pack()

        self.root.mainloop()

#-------------------------------------------------------------------------------
#x=view()
