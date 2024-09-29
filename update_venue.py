from tkinter import *
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import login_page, add_department, view_events, view_departments, view_venues, Database, dashboard_screen


class UpdateVenue:
    def __init__(self,id):
        self.root = Toplevel()
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

        
        self.id = id
        print(f"Id {self.id}")

        self.data=Database.show_single_venues(self.id)
        print("data is ",self.data)

        try:
            self.img = Image.open('abc.jpg').resize((1000, 600))
            self.imgTk = ImageTk.PhotoImage(self.img)
            self.imgLBL = Label(self.root, image=self.imgTk)
            self.imgLBL.place(x=0, y=0)
        except Exception as e:
            print(e)

        self.menubar = Menu(self.root)
        self.event = Menu(self.menubar, tearoff=0)

        self.dashboard_menus = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Home', menu=self.dashboard_menus)
        self.dashboard_menus.add_command(label='Dashboard', command=self.open_dashboard_page)

        self.add_menus = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Add Details', menu=self.add_menus)
        self.add_menus.add_command(label='Add Department', command=self.open_add_department)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='View Details', menu=self.view_menu)
        self.view_menu.add_command(label='View Department', command=self.open_view_department_page)
        self.view_menu.add_command(label='View Venues', command=self.open_view_venues_page)
        self.view_menu.add_command(label='View Events', command=self.open_view_events_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.admin_logout)

        self.root.config(menu=self.menubar)
    
    # def update_venue_page_widgets(self):     
        
        self.frame = Frame(self.root, width=600, height=550, bg="white")
        self.frame.place(x=530, y=50)

        
        self.firstLBL = Label(self.root, text='Update Venue Details', bg="white", fg="black",
                                  font=(("Bradley Hand ITC", 40, "bold")))
        self.firstLBL.place(x=400, y=30)
    
        # self.firstLBL = Label(self.root, text='Add Venue Details', bg="white", fg="black",
        #                           font=(("Bradley Hand ITC", 40, "bold")))
        # self.firstLBL.place(x=400, y=30)

        # creating parameters to login
        self.firstLBL = Label(self.frame, text='Venue Name', bg='white', fg="black", font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=0, y=100)

        self.venue_name_entry = Entry(self.frame, bg='white', fg="black", font=(("@Yu Gothic", 15, "")))
        self.venue_name_entry.place(x=230, y=106)
        self.venue_name_entry.insert(0, self.data[1])

        self.firstLBL = Label(self.frame, text='Location', bg='white', fg="black", font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=0, y=194)

        self.location_entry = Entry(self.frame, bg='white', fg="black", font=(("@Yu Gothic", 15, "")))
        self.location_entry.place(x=230, y=199)
        self.location_entry.insert(0, self.data[2])

        self.firstLBL = Label(self.frame, text='Sitting Capacity', bg='white', fg="black",
                              font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=0, y=298)

        self.sitting_entry = Entry(self.frame, bg='white', fg="black", font=(("@Yu Gothic", 15, "underline")))
        self.sitting_entry.place(x=230, y=305)
        self.sitting_entry.insert(0, self.data[3])

        
        # vData = dict(self.id).get("values")
        # print(f"Venue Data {vData}")
        # self.venue_name_entry.insert(0, [0])
        # self.location_entry.insert(1, vData[1])
        # self.sitting_entry.insert(2, vData[2])

        self.update_button = Button(self.frame, text='UPDATE', width=10, bg="#F7F7F7",
                                        font=(("@Yu Gothic", 15, "bold")),
                                        command=self.run_update_venue)
        self.update_button.place(x=236, y=415)
       

        self.root.mainloop()

    def run_update_venue(self):

        if self.venue_name_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter venue name first")
        elif self.location_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter venue location first")
        elif self.sitting_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter sitting capacity first")
        else:
            venue_details = (
                self.venue_name_entry.get().strip(), self.location_entry.get().strip(),
                self.sitting_entry.get().strip(), self.id[0])
            print("Updated Venue details - ", venue_details)
            update_result = Database.update_venue_info(venue_details)
            if update_result:
                messagebox.showinfo("Message", "Venue updated successfully.")
                self.root.destroy()
                v = view_venues.ViewVenues()
                v.view_venues_page_widgets()
            else:
                messagebox.showerror("Alert!", "Something went wrong")

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

    def admin_logout(self):
        confirmation = messagebox.askyesno("Message", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_page.LoginPage()
            l.login_widgets()
        else:
            messagebox.showinfo("Message", "Ok")


if __name__ == "__main__":
    v=UpdateVenue()
 