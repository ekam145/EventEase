from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import login_page, add_department, add_venue, view_departments, view_venues, Database, dashboard_screen


class ViewEvents:
    def __init__(self):
        self.root = Tk()
        self.root.title("Events Details | Administration Panel")
        self.root.resizable(False, False)
        self.root.geometry('1200x600')

    def view_events_page_menus(self):
        self.menubar = Menu(self.root)
        self.event = Menu(self.menubar, tearoff=0)

        self.dashboard_menus = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Home', menu=self.dashboard_menus)
        self.dashboard_menus.add_command(label='Dashboard', command=self.open_dashboard_page)

        self.add_menus = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Add Details', menu=self.add_menus)
        self.add_menus.add_command(label='Add Department', command=self.open_add_department)
        self.add_menus.add_command(label='Add Venues', command=self.open_add_venue_page)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='View Details', menu=self.view_menu)
        self.view_menu.add_command(label='View Department', command=self.open_view_department_page)
        self.view_menu.add_command(label='View Venues', command=self.open_view_venues_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.admin_logout)

        self.root.config(menu=self.menubar)

    def view_events_page_widgets(self):
        self.frame = Frame(self.root, width='1200', height='600')
        self.frame.place(x=0, y=0)

        # self.img = Image.open('images/tableimage.jpg').resize((1200, 600))
        # self.imgTk = ImageTk.PhotoImage(self.img)
        # self.imgLBL = Label(self.frame, image=self.imgTk, width=1200, height=600)
        # self.imgLBL.place(x=0, y=0)

        self.title_label = Label(self.frame, text="All Events Details", font=(("Bradley Hand ITC", 40, "bold")))
        self.title_label.place(x=400, y=50)

        scrollbar_x = Scrollbar(self.frame, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(self.frame, orient=VERTICAL)

        self.table = ttk.Treeview(self.frame, columns=("a", "b", "c", "d", "e", "f", "g", "h", "i"),
                                  yscrollcommand=scrollbar_y.set,
                                  xscrollcommand=scrollbar_x.set, show="headings", cursor="hand2")

        scrollbar_x.config(command=self.table.xview)
        scrollbar_x.place(x=140, y=550, width=900)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_y.place(x=1042, y=150, height=400)

        self.table.heading('#0', text="Id")
        self.table.heading('#1', text="Department")
        self.table.heading('#2', text="Coordinator")
        self.table.heading('#3', text="Event Name")
        self.table.heading('#4', text="Date")
        self.table.heading('#5', text="Duration")
        self.table.heading('#6', text="Venue")
        self.table.heading('#7', text="Status")
        self.table.heading('#8', text="Reject")
        self.table.heading('#9', text="Accept")

        self.table.column('#0', stretch=NO, minwidth=100, width=100)
        self.table.column('#1', stretch=NO, minwidth=100, width=100)
        self.table.column('#2', stretch=NO, minwidth=100, width=100)
        self.table.column('#3', stretch=NO, minwidth=100, width=100)
        self.table.column('#4', stretch=NO, minwidth=100, width=100)
        self.table.column('#5', stretch=NO, minwidth=100, width=100)
        self.table.column('#6', stretch=NO, minwidth=100, width=100)
        self.table.column('#7', stretch=NO, minwidth=100, width=100)
        self.table.column('#8', stretch=NO, minwidth=100, width=100)
        self.table.column('#9', stretch=NO, minwidth=100, width=100)

        result = Database.show_all_events()
        for i in result:
            print(i)
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'Reject', 'Accept'))

        self.table.bind('<Double-Button-1>', self.actions)

        self.table.place(x=140, y=150, height=400)

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
            reject_result = messagebox.askyesno("Alert!", "Do You really want to update the status?")
            if reject_result:
                result = Database.reject_event(gup)
                if result:
                    messagebox.showinfo("Message", "Status updated")
                    self.root.destroy()
                    v = ViewEvents()
                    v.view_events_page_menus()
                    v.view_events_page_widgets()
            else:
                messagebox.showerror('Alert', 'Something went wrong.')

        if col == '#9':
            accept_result = messagebox.askyesno("Alert!", "Do You really want to update the status?")
            if accept_result:
                result = Database.accept_event(gup)
                if result:
                    messagebox.showinfo("Message", "Status updated")
                    self.root.destroy()
                    v = ViewEvents()
                    v.view_events_page_menus()
                    v.view_events_page_widgets()
            else:
                messagebox.showerror('Alert', 'Something went wrong.')

    def open_dashboard_page(self):
        self.root.destroy()
        d = dashboard_screen.DashboardScreen()
        d.dashboard_screen_menus()
        d.dashboard_screen_widgets()

    def open_view_department_page(self):
        self.root.destroy()
        v = view_departments.ViewDepartments()
        v.view_departments_page_menus()
        v.view_departments_page_widgets()

    def open_view_venues_page(self):
        self.root.destroy()
        v = view_venues.ViewVenues()
        v.view_venue_page_menus()
        v.view_venues_page_widgets()

    def open_add_department(self):
        self.root.destroy()
        a = add_department.AddDepartment()
        a.add_department_page_menus()
        a.add_department_page_widgets()

    def open_add_venue_page(self):
        self.root.destroy()
        a = add_venue.AddVenue()
        a.add_venue_page_menus()
        a.add_venue_page_widgets()

    def admin_logout(self):
        confirmation = messagebox.askyesno("Message", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_page.LoginPage()
            l.login_widgets()
        else:
            messagebox.showinfo("Message", "Ok")


if __name__ == '__main__':
    v = ViewEvents()
    v.view_events_page_menus()
    v.view_events_page_widgets()
