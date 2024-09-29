from tkinter import *
from tkinter import ttk
import Database, dashboard_department, login_department, add_event
from tkinter import messagebox


class DepartmentViewEvents:
    def __init__(self, logged_in_user=""):
        self.root = Tk()
        self.loggedInUser = logged_in_user
        self.root.title("Events Detail | Department Panel")
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def department_view_event_page_menus(self):
        self.menubar = Menu(self.root)

        self.dashboard_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Home', menu=self.dashboard_menu)
        self.dashboard_menu.add_command(label='Dashboard', command=self.open_dashboard_page)

        self.add_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Add', menu=self.add_menu)
        self.add_menu.add_command(label='Add Event', command=self.open_department_add_event_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.run_department_logout)

        self.root.config(menu=self.menubar)

    def department_view_events_page_widgets(self):
        self.frame = Frame(self.root, width='1000', height='2000')
        self.frame.place(x=0, y=0)

        self.frame1 = Frame(self.root, bg="#7D246E", bd=10, relief=RIDGE)
        self.frame1.place(x=25, y=80, width=950,
                          height=400)

        self.frame1_title = Label(self.frame1, text="View Event Details",
                                  font=("Georgia", 25, "bold"), bg="#7D246E", fg="#F0B4D6")
        self.frame1_title.place(x=270, y=5)

        frame2 = Frame(self.frame1, bd=5, relief=RIDGE)
        frame2.place(x=27, y=60, width=870,
                     height=300)

        scrollbar_x = Scrollbar(frame2, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(frame2, orient=VERTICAL)

        self.table = ttk.Treeview(frame2, columns=("a", "b", "c", "d", "e", "f", "g", "h", "i"),
                                  yscrollcommand=scrollbar_y.set,
                                  xscrollcommand=scrollbar_x.set, show="headings", cursor="hand2")

        scrollbar_x.config(command=self.table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        self.table.heading('#0', text="Id")
        self.table.heading('#1', text="Department")
        self.table.heading('#2', text="Coordinator")
        self.table.heading('#3', text="Event Name")
        self.table.heading('#4', text="Date")
        self.table.heading('#5', text="Duration")
        self.table.heading('#6', text="Venue")
        self.table.heading('#7', text="Status")
        self.table.heading('#8', text="Delete")
        self.table.heading('#9', text="Update")

        self.table.column('#0', stretch=NO, minwidth=200, width=200)
        self.table.column('#1', stretch=NO, minwidth=200, width=200)
        self.table.column('#2', stretch=NO, minwidth=200, width=200)
        self.table.column('#3', stretch=NO, minwidth=200, width=200)
        self.table.column('#4', stretch=NO, minwidth=200, width=200)
        self.table.column('#5', stretch=NO, minwidth=200, width=200)
        self.table.column('#6', stretch=NO, minwidth=200, width=200)
        self.table.column('#7', stretch=NO, minwidth=200, width=200)
        self.table.column('#8', stretch=NO, minwidth=200, width=200)
        self.table.column('#9', stretch=NO, minwidth=200, width=200)

        result = Database.show_all_events()
        for i in result:
            print(i)
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'Delete', 'Update'))

        self.table.bind('<Double-Button-1>', self.actions)

        self.table.pack(fill=BOTH, expand=1)

        self.root.mainloop()

    def actions(self, e):
        # print("i am e",e)
        # get the values of the selected rows\\
        tt = self.table.focus()
        col = self.table.identify_column(e.x)
        print(f'cols {col}')
        # print(self.table.item(tt))

        gup = (
            self.table.item(tt).get('text'),
        )
        print("i am gup", gup, col)

        if col == '#8':
            res = messagebox.askyesno("Delete", "Do You really want to delete this event?")
            if res:
                delete_result = Database.delete_event_info(gup)
                if delete_result:
                    messagebox.showinfo("Success", "Event deleted successfully")
                    self.root.destroy()
                    d = DepartmentViewEvents(self.loggedInUser)
                    d.department_view_event_page_menus()
                    d.department_view_events_page_widgets()
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')

        if col == '#9':
            print('edit is called')
            a = add_event.AddEvent(event_data=self.table.item(tt))
            self.root.destroy()
            a.add_event_page_menus()
            a.add_event_page_widgets()

    def open_dashboard_page(self):
        self.root.destroy()
        d = dashboard_department.DepartmentDashboard(self.loggedInUser)
        d.dashboard_department_page_menus()
        d.dashboard_department_page_widgets()

    def open_department_add_event_page(self):
        self.root.destroy()
        a = add_event.AddEvent(logged_in_user=self.loggedInUser)
        a.add_event_page_menus()
        a.add_event_page_widgets()

    def run_department_logout(self):
        confirmation = messagebox.askyesno("Alert!", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_department.DepartmentLogin()
            l.department_login_page_widgets()


if __name__ == '__main__':
    d = DepartmentViewEvents()
    d.department_view_event_page_menus()
    d.department_view_events_page_widgets()
