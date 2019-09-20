from datetime import *
from tkinter import *
from tkinter.messagebox import *
import tkinter.ttk as ttk
from connection import *
import http.client

bt_list = []
bt_dict = {}
class ticket:
# -====================================================================================================================
                                    # PARKING 2 :- START
# -====================================================================================================================
    def parking2(self):
        self.rk = Tk()
        self.rk.title("Parking2")
        global bt_list

        for i in range(101, 111):
            for j in range(101, 111):
                s = str(i) + "-" + str(j)
                bt_list.append(s)
                dr = connection()
                query = "select * from parking_ticket where parking_location='" + s + "' and dateofexit is null"
                cr = dr.conn.cursor()
                cr.execute(query)
                p = cr.fetchall()

                if len(p) > 0:
                    bt_dict[bt_list[-1]] = Button(self.rk, text="O", font="bold", width="5",bg="red", state="disabled")
                else:
                    bt_dict[bt_list[-1]] = Button(self.rk, width=7, text=s,bg="green",fg="yellow")
                    bt_dict[bt_list[-1]]["command"] = lambda x=i, y=j: self.park1(x, y)
                bt_dict[bt_list[-1]].grid(row=i, column=j, padx=5, pady=3)

        self.rk.mainloop()
# -====================================================================================================================

    def park1(self, x, y):
        global operation
        operation = str(x) + "-" + str(y)

        self.m.set(operation)
        # for i in range(0, len(bt_list)):
        #     if bt_list[i] == p:
        #         bt_dict[bt_list[-1]] = ttk.Button(self.win, text=" ", width="5", state="disabled")
        # bt_dict[bt_list[-1]].grid(row=x, column=y)
        if x > 99:
            self.rk.destroy()
        else:
            self.win.destroy()
# -===========================================================================================================
                             # PARKING 1:-START
# -====================================================================================================================
    def parking1(self):
        self.win = Tk()
        self.win.title("Parking1")
        global bt_list

        for i in range(1, 11):
            for j in range(1, 11):
                s = str(i)+"-"+str(j)
                bt_list.append(s)
                dr = connection()
                query = "select * from parking_ticket where parking_location='"+s+"' and dateofexit is null"
                cr = dr.conn.cursor()
                cr.execute(query)
                p = cr.fetchall()

                if len(p) > 0:
                    bt_dict[bt_list[-1]] = Button(self.win, text="O", font="bold", bg="red", width="5", state="disabled")
                else:
                    bt_dict[bt_list[-1]] = Button(self.win, width=5, text=s,bg="green",fg="yellow")
                    bt_dict[bt_list[-1]]["command"] = lambda x=i, y=j: self.park1(x, y)
                bt_dict[bt_list[-1]].grid(row=i, column=j, padx=5, pady=3)
        self.win.mainloop()
# -====================================================================================================================
# -====================================================================================================================
    def insert(self):
        if self.vnumber.get()=="" or self.cbvechicle.get()=="" or self.cbparking.get()=="" or self.price=="" or self.parking_location=="" or self.parking_location.get()=="" or self.mobile.get()=="":
            showerror("", "All Fields are mandatory")
        else:
            self.currentdate = datetime.now().strftime("%Y-%m-%d")
            self.currenttime = str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
            dr = connection()
            query = "insert into parking_ticket value (null, '"+self.vnumber.get()+"','"+self.cbvechicle.get()+"','"+self.cbparking.get()+"',"+self.price.get()+",'"+self.parking_location.get()+"','"+self.currentdate+"','"+self.currenttime+"','"+self.mobile.get()+"',null,null,null)"
            cr = dr.conn.cursor()
            cr.execute(query)
            dr.conn.commit()
            # -=============================================================
            conn = http.client.HTTPConnection("server1.vmm.education")
            textmessage = "Your Vehicle no " + self.vnumber.get() + " is Parked at row " + self.parking_location.get() + " and parking Date and Time respectively  " + self.currentdate + " " + self.currenttime
            textmessage = textmessage.replace(" ", "%20")
            conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?username=dhk_py&password=GNEP0QCE&message=" + textmessage + "&phone_numbers=" + self.mobile.get())
            response = conn.getresponse()
            print(response.read())
            # -==============================================================
            showinfo("", "booking sucess")
            self.price.delete(0, END)
            self.parking_location.delete(0, END)
            self.mobile.delete(0, END)
            self.vnumber.delete(0,END)
            self.cbparking.set('')
            self.cbvechicle.set('')
# -====================================================================================================================
    def inrate(self,event):
        if self.cbvechicle.get()!="" and self.cbparking.get()!="":
            ar = connection()
            query = "select price from rate where vehciletype='" + self.cbvechicle.get() + "' and parkingtype='" + self.cbparking.get() + "'"
            print(query)
            cd = ar.conn.cursor()
            cd.execute(query)
            d = cd.fetchone()
            # print(d)
            self.price.config(state='normal')
            self.price.delete(0,END)
            self.price.insert(0,d[0])
            self.price.config(state='readonly')
# -====================================================================================================================
    def __init__(self):
        self.root = Tk()
        self.root.title("Parking Ticket")
        self.root.geometry("410x400")
    # -=================================================================================
        top = Frame(self.root, width=100)
        top.pack()
        down = Frame(self.root)
        down.pack()
    # -====================================================================================
        lb = Label(top, text="PARKING TICKET", font=("Britannic Bold", 25, "italic", "underline"), fg="blue").pack()
    # -=====================================================================================
        self.m = StringVar()
        lb = Label(down, text="Vehicle_Number", font=('arial', 10, "bold"), fg="brown").grid(row=1, column=0, sticky=(W))
        lb = Label(down, text="Vehicle_Type", font=('arial', 10, "bold"), fg="brown").grid(row=2, column=0, sticky=(W))
        lb = Label(down, text="Parking_Type", font=('arial', 10, "bold"), fg="brown").grid(row=3, column=0, sticky=(W))
        lb = Label(down, text="Price", font=('arial', 10, "bold"), fg="brown").grid(row=4, column=0, sticky=(W))
        lb = Label(down, text="parking_location", font=('arial', 10, "bold"), fg="brown").grid(row=5, column=0, sticky=(W))
        # lb = Label(down, text="Date_Of_Entry", font=('arial', 10, "bold"), fg="brown").grid(row=6, column=0, sticky=(W))
        # lb = Label(down, text="Time_of_Entry", font=('arial', 10, "bold"), fg="brown").grid(row=7, column=0, sticky=(W))
        lb = Label(down, text="mobile", font=('arial', 10, "bold"), fg="brown").grid(row=6, column=0, sticky=(W))

        self.vnumber = Entry(down)
        self.cbvechicle = ttk.Combobox(down, width=30, state="readonly", value=("Two Wheeler Light Vechicle", "Two Wheeler Heavy Vechicle", "Four Wheeler Light Vechicle", "Four Wheeler Heavy Vechicle"))
        self.cbparking = ttk.Combobox(down, width=30, state="readonly", value=("Full day", "12 Hour", "6 Hour", "3 Hour"))
        self.ptype = Entry(down)
        self.price = Entry(down)
        self.parking_location = Entry(down, textvariable=self.m, state="readonly")
        # self.dateofentry = Entry(down)
        # self.timeofentry = Entry(down)
        self.mobile = Entry(down)
        self.cbvechicle.bind("<<ComboboxSelected>>",self.inrate)
        self.cbparking.bind("<<ComboboxSelected>>",self.inrate)

        self.vnumber.grid(row=1, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.cbvechicle.grid(row=2, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.cbparking.grid(row=3, column=1,padx=5, pady=5, sticky=(E, N, W))
        self.price.grid(row=4, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.parking_location.grid(row=5, column=1, padx=5, pady=5, sticky=(E, N, W))
        # self.dateofentry.grid(row=6, column=1, padx=5, pady=5, sticky=(E, N, W))
        # self.timeofentry.grid(row=7, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.mobile.grid(row=6, column=1, padx=5, pady=5, sticky=(E, N, W))
        #if self.cbvechicle!="" or self.cbparking!="":
    # -===================================================================================================================
        dr=connection()
    # -==================================================================================================================

        bt1 = Button(down, text="Submit", font=('arial', 10, "bold"), borderwidth=3, command=self.insert, width=7).grid(row=7, column=1)
        bt2 = Button(down, text="Parking 1", font=('arial', 10, "bold"), borderwidth=3, command=self.parking1).grid(row=5, column=2)
        bt3 = Button(down, text="parking 2", font=('arial', 10, "bold"), borderwidth=3, command=self.parking2).grid(row=6, column=2)

        self.root.mainloop()
# -========================================================================================================================
x=ticket()