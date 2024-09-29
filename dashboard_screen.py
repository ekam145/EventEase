from tkinter import *
from PIL import Image, ImageTk
import login_page, add_department, add_venue, view_events, view_departments, view_venues, Database, add_event
from tkinter import messagebox
from tkinter import ttk


class DashboardScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("Dashboard | Administration Panel")
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def dashboard_screen_menus(self):
        self.menubar = Menu(self.root)
        self.event = Menu(self.menubar, tearoff=0)

        self.add_menus = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Add Details', menu=self.add_menus)
        self.add_menus.add_command(label='Add Department', command=self.open_add_department)
        self.add_menus.add_command(label='Add Venues', command=self.open_add_venue_page)
        self.add_menus.add_command(label='Add Event', command=self.open_add_event_page)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='View Details', menu=self.view_menu)
        self.view_menu.add_command(label='View Department', command=self.open_view_department_page)
        self.view_menu.add_command(label='View Venues', command=self.open_view_venues_page)
        self.view_menu.add_command(label='View Events', command=self.open_view_events_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.admin_logout)

        self.root.config(menu=self.menubar)

    def dashboard_screen_widgets(self):
        self.image_path = Image.open('im.jpg')
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.imgTk, width=1000, height=600)
        self.image_label.place(x=0, y=0)

        self.frame = Frame(self.root, width='800', height='400', bg='black')
        self.frame.place(x=100, y=105)

        frame2 = Frame(self.frame, bd=15, relief=RIDGE, bg='#ECC3C9')
        frame2.place(x=2, y=2, width=796, height=396)

        self.canvas = Canvas(frame2, bg='#ECC3C9', width=796, height=396)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.inner_frame = Frame(self.canvas, bg='#ECC3C9')
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.show_event_cards()

        self.root.mainloop()

    def show_event_cards(self):
        events = Database.show_all_accepted_events()

        row = 0
        col = 0
        for event in events:
            if col > 2:
                col = 0
                row += 1

            event_frame = Frame(self.inner_frame, bd=2, relief=SOLID, bg='white')
            event_frame.grid(row=row, column=col, padx=10, pady=10)

            Label(event_frame, text=f"Department: {event[1]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Coordinator: {event[2]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Event Name: {event[3]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Date: {event[4]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Time: {event[5]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Venue: {event[6]}", font=('Arial', 12), bg='white').pack(pady=5)
            Label(event_frame, text=f"Status: {event[7]}", font=('Arial', 12), bg='white').pack(pady=5)

            col += 1

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
        
    def open_add_event_page(self):
        self.root.destroy()
        a = add_event.AddEvent()
        a.add_event_page_menus()
        a.add_event_page_widgets()

    def admin_logout(self):
        confirmation = messagebox.askyesno("Message", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_page.LoginPage()
            l.login_widgets()
        else:
            messagebox.showinfo("Message", "Ok")


if __name__ == '__main__':
    w = DashboardScreen()
    w.dashboard_screen_menus()
    w.dashboard_screen_widgets()
