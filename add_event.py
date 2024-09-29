from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

import Database, login_department, department_view_event, dashboard_department,dashboard_screen


class AddEvent:
    def __init__(self, event_data=""):
        self.root = Tk()
        self.selected_event_data = event_data
        
        if self.selected_event_data:
            self.root.title('Update Event | Department Panel')
        else:
            self.root.title('Add Event | Department Panel')
        
        self.root.resizable(False, False)
        self.root.geometry('1000x750')
        
        # Load the background image
        self.bg_image = Image.open("im.jpg")  
        self.bg_image = self.bg_image.resize((1000, 750))
        self.bg = ImageTk.PhotoImage(self.bg_image)

         # Create a background label
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Fonts
        self.title_font = ("Helvetica", 18, "bold")
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        
        # Background colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#007BFF"
        self.text_color = "#333"
        
        

    def add_event_page_menus(self):
        self.menubar = Menu(self.root)

        self.dashboard_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Home', menu=self.dashboard_menu)
        self.dashboard_menu.add_command(label='Dashboard', command=self.open_dashboard_page)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='View', menu=self.view_menu)
        self.view_menu.add_command(label='View Events', command=self.open_department_view_events_page)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Profile', menu=self.profile_menu)
        self.profile_menu.add_command(label='Logout', command=self.run_department_logout)

        self.root.config(menu=self.menubar)

    def add_event_page_widgets(self):
        # self.img = Image.open('images/addimage.png').resize((1200, 750))
        # self.imgTk = ImageTk.PhotoImage(self.img)
        # self.imgLBL = Label(self.root, image=self.imgTk, width=1000, height=750)
        # self.imgLBL.place(x=0, y=0)
        
        self.frame=Frame(self.root, width=600, height=530, bg="#E6E2CE")
        self.frame.place(x=230, y=70)

        self.firstLBL = Label(self.frame, text='Add Event Details',  fg="black",bg="#E6E2CE",
                                  font=(("Bradley Hand ITC", 40, "bold")))
        self.firstLBL.place(x=100, y=30)

        self.dept_id=Label(self.root, text='Department ID', fg='black', bg="#E6E2CE",
                              font=(("@Yu Gothic", 20, "bold")))
        self.dept_id.place(x=260, y=180)

        self.dept_id_list = []
        for i in Database.show_all_departments():
            self.dept_id_list.append(f"{i[0]}-{i[1]}")
        self.dept_id_entry = Combobox(self.root, values=self.dept_id_list, width='22', background='white', foreground="black",
                                      font=(("@Yu Gothic", 15, "")))
        self.dept_id_entry.place(x=497, y=185)
        
        
    

        self.firstLBL = Label(self.root, text='Coordinator ', fg='black', bg="#E6E2CE",
                              font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=260, y=227)

        self.coordinator_entry = Entry(self.root, width='22', bg='white',border=2, fg="black", font=(("@Yu Gothic", 15, "")))
        self.coordinator_entry.place(x=497, y=232)

        self.firstLBL = Label(self.root, text='Event Name', fg='black', bg="#E6E2CE",
                              font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=254, y=282)

        self.event_name_entry = Entry(self.root, width='22', bg='white', fg="black",border=2, font=(("@Yu Gothic", 15, "")))
        self.event_name_entry.place(x=497, y=287)

        self.firstLBL = Label(self.root, text='Date', fg='black', bg="#E6E2CE", font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=350, y=333)

        self.date_entry = Entry(self.root, width='22', fg='black', bg="white",border=2, font=(("@Yu Gothic", 15, "")))
        self.date_entry.place(x=497, y=336)

        self.firstLBL = Label(self.root, text='Duration', fg='black', bg="#E6E2CE", font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=299, y=380)

        self.time_entry = Entry(self.root, width='22', bg='white', fg="black",border=2, font=(("@Yu Gothic", 15, "")))
        self.time_entry.place(x=497, y=386)

        self.firstLBL = Label(self.root, text='Venue', fg='black', bg="#E6E2CE", font=(("@Yu Gothic", 20, "bold")))
        self.firstLBL.place(x=332, y=430)

        self.venues_list = []
        for j in Database.show_all_venues():
            self.venues_list.append(j[1])
        self.venues_combobox = Combobox(self.root, values=self.venues_list, width='20',
                                        font=(("@Yu Gothic", 14, "")))
        self.venues_combobox.place(x=497, y=437)

        if self.selected_event_data:
            eData = dict(self.selected_event_data).get("values")
            print("Selected event data - ", eData)
            self.coordinator_entry.insert(0, eData[1])
            self.event_name_entry.insert(0, eData[2])
            self.date_entry.insert(0, eData[3])
            self.time_entry.insert(0, eData[4])
            self.enterBtn = Button(self.root, text='UPDATE', width=10, bg="#303136", fg="white",
                                   font=(("@Yu Gothic", 15, "bold")), command=self.run_update_event)
            self.enterBtn.place(x=450, y=515)
        else:
            self.enterBtn = Button(self.root, text='CREATE', width=10, bg="#303136", fg="white",
                                   font=(("@Yu Gothic", 15, "bold")), command=self.run_add_event)
            self.enterBtn.place(x=450, y=515)

        self.root.mainloop()

    def run_add_event(self):

        if self.coordinator_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter coordinator first")
        elif self.event_name_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter event name first")
        elif self.date_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter date first")
        elif self.time_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter time first")
        # elif self.selected_department.get().strip():
        #     messagebox.showwarning("Alert!", "Please select department first")
        # elif self.selected_venue.get().strip():
        #     messagebox.showwarning("Alert!", "Please select venue first")
        else:
            event_details = (
                
                self.dept_id_entry.get().split(",")[0],
                self.coordinator_entry.get().strip(),
                self.event_name_entry.get().strip(),
                self.date_entry.get().strip(),
                self.time_entry.get().strip(), self.venues_combobox.get().strip(), "PENDING")

            result = Database.add_event(event_details)
            if result:
                print("Event has been created successfully")
                messagebox.showinfo("Message", "Event has been created successfully.")
                self.root.destroy()
                d = department_view_event.DepartmentViewEvents()
                d.department_view_event_page_menus()
                d.department_view_events_page_widgets()
            else:
                messagebox.showwarning("Alert!", "Something went wrong")

    def run_update_event(self):

        if self.coordinator_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter coordinator first")
        elif self.event_name_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter event name first")
        elif self.date_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter date first")
        elif self.time_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter time first")
        # elif self.selected_department.get().strip():
        #     messagebox.showwarning("Alert!", "Please select department first")
        # elif self.selected_venue.get().strip():
        #     messagebox.showwarning("Alert!", "Please select venue first")
        else:
            event_details = (
                self.dept_id_entry.get().split(",")[0],
                self.coordinator_entry.get(),
                self.event_name_entry.get(),
                self.date_entry.get(),
                self.time_entry.get(),
                self.venues_combobox.get(),
                "ACCEPTED",
                dict(self.selected_event_data).get("text"))
            print("Updated event details - ", event_details)
            result = Database.update_event_info(event_details)
            if result:
                print("Event has been updated successfully")
                messagebox.showinfo("Message", "Event has been updated successfully.")
                d = department_view_event.DepartmentViewEvents()
                d.department_view_event_page_menus()
                d.department_view_events_page_widgets()
            else:
                messagebox.showwarning("Alert!", "Something went wrong")

    def open_dashboard_page(self):
        self.root.destroy()
        d = dashboard_screen.DashboardScreen()
        d.dashboard_screen_menus()
        d.dashboard_screen_widgets()

    def open_department_view_events_page(self):
        self.root.destroy()
        v = department_view_event.DepartmentViewEvents()
        v.department_view_event_page_menus()
        v.department_view_events_page_widgets()

    def run_department_logout(self):
        confirmation = messagebox.askyesno("Alert!", "Do you really want to logout?")
        if confirmation:
            self.root.destroy()
            l = login_department.DepartmentLogin()
            l.department_login_page_widgets()


if __name__ == "__main__":
    a = AddEvent()
    a.add_event_page_menus()
    a.add_event_page_widgets()
