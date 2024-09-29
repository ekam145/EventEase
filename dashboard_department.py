from tkinter import *
from PIL import Image, ImageTk
import login_department, add_event, department_view_event, Database
from tkinter import messagebox
from tkinter import ttk


class DepartmentDashboard:
    def __init__(self, logged_in_user=""):
        self.root = Tk()
        self.loggedInUser = logged_in_user
        self.root.title("Dashboard | Department Panel")
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def dashboard_department_page_menus(self):
        self.menubar = Menu(self.root)

        self.add_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Add', menu=self.add_menu)
        self.add_menu.add_command(label='Add Event', command=self.open_department_add_event_page)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='View', menu=self.view_menu)
        self.view_menu.add_command(label='View Events', command=self.open_department_view_events_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.run_department_logout)

        self.root.config(menu=self.menubar)

    def dashboard_department_page_widgets(self):
        self.image_path = Image.open('im.jpg')
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.imgLBL = Label(self.root, image=self.imgTk, width=1000, height=600)
        self.imgLBL.place(x=0, y=0)

        self.frame = Frame(self.root, width='800', height='400', bg='black')
        self.frame.place(x=100, y=105)

        frame2 = Frame(self.frame, bd=15, relief=RIDGE, bg='#ECC3C9')
        frame2.place(x=2, y=2, width=796,
                     height=396)

        frame1 = Frame(frame2, bd=15, relief=RIDGE)
        frame1.place(x=35, y=35, width=700,
                     height=300)

        scrollbar_x = Scrollbar(frame1, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(frame1, orient=VERTICAL)

        self.table = ttk.Treeview(frame1, columns=("a", "b", "c", "d", "e", "f", "g"),
                                  yscrollcommand=scrollbar_y.set,
                                  xscrollcommand=scrollbar_x.set, show="headings", cursor="hand2")

        scrollbar_x.config(command=self.table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        self.table.heading('a', text="Department")
        self.table.heading('b', text="Event Name")
        self.table.heading('c', text="Venue")
        self.table.heading('d', text="Date")
        self.table.heading('e', text="Time")
        self.table.heading('f', text="Venue")
        self.table.heading('g', text="Status")

        self.table.column('#1', stretch=NO, minwidth=100, width=100)
        self.table.column('#2', stretch=NO, minwidth=100, width=100)
        self.table.column('#3', stretch=NO, minwidth=100, width=100)
        self.table.column('#4', stretch=NO, minwidth=100, width=100)
        self.table.column('#5', stretch=NO, minwidth=100, width=100)
        self.table.column('#6', stretch=NO, minwidth=100, width=100)
        self.table.column('#7', stretch=NO, minwidth=100, width=100)

        for i in Database.show_all_accepted_events():
            self.table.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        self.table.pack(fill=BOTH, expand=1)

        self.root.mainloop()

    def open_department_view_events_page(self):
        self.root.destroy()
        v = department_view_event.DepartmentViewEvents(self.loggedInUser)
        v.department_view_event_page_menus()
        v.department_view_events_page_widgets()

    def open_department_add_event_page(self):
        self.root.destroy()
        a = add_event.AddEvent()
        a.add_event_page_menus()
        a.add_event_page_widgets()

    def run_department_logout(self):
        confirmation = messagebox.askyesno("Alert!", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_department.DepartmentLogin()
            l.department_login_page_widgets()


if __name__ == '__main__':
    d = DepartmentDashboard()
    d.dashboard_department_page_menus()
    d.dashboard_department_page_widgets()
