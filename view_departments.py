from tkinter import *
from tkinter import ttk
import Database, login_page, add_department, add_venue, view_events, view_venues, dashboard_screen,update_department
from tkinter import messagebox
from PIL import Image,ImageTk

class ViewDepartments:
    def __init__(self):
        self.root = Tk()
        self.root.title("Department Details | Administration Panel")
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

        # self.imgs= Image.open('abc.jpg')
        # self.img=self.imgs.resize((1000, 600))
        # self.imgTk = ImageTk.PhotoImage(self.img)
        # self.imgLBL = Label(self.root, image=self.imgTk, width=1000, height=600)
        # self.imgLBL.place(x=0, y=0)

    def view_departments_page_menus(self):
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
        self.view_menu.add_command(label='View Venues', command=self.open_view_venues_page)
        self.view_menu.add_command(label='View Events', command=self.open_view_events_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.admin_logout)

        self.root.config(menu=self.menubar)

    def view_departments_page_widgets(self):
        
        self.frame = Frame(self.root, width='1000', height='600')
        self.frame.place(x=0, y=0)
        self.frame1 = Frame(self.root, bg="#7D246E", bd=10, relief=RIDGE)
        self.frame1.place(x=25, y=90, width=950,
                          height=400)

        self.frame1_title = Label(self.frame1, text="View Department Details",
                                  font=("Georgia", 25, "bold"), bg="#7D246E", fg="#F0B4D6")
        self.frame1_title.place(x=240, y=5)

        frame2 = Frame(self.frame1, bd=15, relief=RIDGE)
        frame2.place(x=20, y=60, width=870,
                     height=300)

        scrollbar_x = Scrollbar(frame2, orient=HORIZONTAL)
        scrollbar_y = Scrollbar(frame2, orient=VERTICAL)

        self.table = ttk.Treeview(frame2, columns=("a", "b", "c", "d", "e"),
                                  yscrollcommand=scrollbar_y.set,
                                  xscrollcommand=scrollbar_x.set, show="headings", cursor="hand2")

        scrollbar_x.config(command=self.table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        scrollbar_y.config(command=self.table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        self.table.heading('a', text="Department Name")
        self.table.heading('b', text="Username")
        self.table.heading('c', text="Password")
        self.table.heading('d', text="Edit")
        self.table.heading('e', text="Delete")

        self.table.column('#1', stretch=NO, minwidth=200, width=200)
        self.table.column('#2', stretch=NO, minwidth=200, width=200)
        self.table.column('#3', stretch=NO, minwidth=200, width=200)
        self.table.column('#4', stretch=NO, minwidth=200, width=200)
        self.table.column('#5', stretch=NO, minwidth=200, width=200)

        result = Database.show_all_departments()
        for i in result:
            self.table.insert('', 0, text=i[0], values=(i[1], i[2], i[3], 'Edit', 'Delete'))

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

        # gup = (
        #     self.table.item(tt).get('text'),
        # )
        # print("i am gup", gup, col)
        self.rowid=(self.table.item(tt).get("text"),)
        print(self.rowid)

        if col == '#5':
            confirmation_result = messagebox.askyesno("Delete", "Do You really want to delete this item.")
            if confirmation_result:
                delete_result = Database.delete_department_info(self.rowid)
                if delete_result:
                    messagebox.showinfo("Success", "Deleted Successfully")
                    self.root.destroy()
                    v = ViewDepartments()
                    v.view_departments_page_widgets()
                else:
                    messagebox.showerror('Alert', 'Something went wrong.')

        if col == '#4':
            print('Edit is called')
            m=messagebox.showwarning("Edit","Do you want to edit details ?")
            if m:
                self.root.destroy()
                update_department.UpdateDepartment(self.rowid)

    def open_dashboard_page(self):
        self.root.destroy()
        d = dashboard_screen.DashboardScreen()
        d.dashboard_screen_menus()
        d.dashboard_screen_widgets()

    def open_view_venues_page(self):
        self.root.destroy()
        v = view_venues.ViewVenues()
        v.view_venue_page_menus()
        v.view_venues_page_widgets()

    def open_view_events_page(self):
        self.root.destroy()
        v = view_events.ViewEvents()
        v.view_events_page_menus()
        v.view_events_page_widgets()

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
    v = ViewDepartments()
    v.view_departments_page_menus()
    v.view_departments_page_widgets()
