from add_admin import *
from admin_login import *
from admin_view import *
from admin_update import *
from rate import *
from view_rate import *
from update_rate import *
from booking_parking_ticket import *
from exit_ticket import *
from today_sell import *
from from_date import *
from vnumber import *

class combiner:
    def admin1(self):
        x = admin()
    def admin0(self):
        x = password()
    def admin2(self):
        x = table()
    def admin3(self):
        x = uupdate()
    def rate1(self):
        x = rate()
    def rate2(self):
        x = view()
    def rate3(self):
        x = uupdate()
    def ticket1(self):
        x = ticket()
    def ticket2(self):
        x = exit()
    def tsell1(self):
        x=sell1()
    def tsell2(self):
        x=sell2()
    def tsell3(self):
        x=sell3()
    #-=============================================================================
    def __init__(self):
        self.x = Tk()
        self.x.geometry("1024x768")
        mymenu = Menu(self.x)
        self.x.config(menu=mymenu)

        option1 = Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Admin", menu=option1)

        option1.add_command(label="Admin Login",command=self.admin0)
        option1.add_command(label="Add Admin",command=self.admin1)
        option1.add_command(label="View Admin",command=self.admin2)
        option1.add_command(label= "Admin Update",command=self.admin3)

        option2 = Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Rate", menu=option2)

        option2.add_command(label="Add Rate",command=self.rate1)
        option2.add_command(label="View Rate",command=self.rate2)
        option2.add_command(label="Update Rate",command=self.rate3)

        option3 = Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Ticket", menu=option3)

        option3.add_command(label="Booking",command=self.ticket1)
        option3.add_command(label="exit",command=self.ticket2)

        option4 = Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="sell", menu=option4)

        option4.add_command(label="Today sell", command=self.tsell1)
        option4.add_command(label="DATE", command=self.tsell2)
        option4.add_command(label="vehicle_number", command=self.tsell3)


        self.x.mainloop()
# -===================================================================================================
t=combiner()
