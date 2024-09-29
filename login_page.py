from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import dashboard_screen
import Database
import welcome_screen


class LoginPage:
    def __init__(self):
        self.root = Tk()
        self.root.title('Administrator | Event Management System')
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def login_widgets(self):
        # inserting image
        self.img = Image.open('images/loginimage2.png').resize((1000, 600))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLBL = Label(self.root, image=self.imgTk, width=1000, height=600)
        self.imgLBL.place(x=0, y=0)

        # Username Entry Widget
        self.username_entry = Entry(self.root, bg='White', fg="Black", font=(("@Yu Gothic", 15, "")))
        self.username_entry.place(x=630, y=205)

        # Password Entry Widget
        self.password_entry = Entry(self.root, bg='White', fg="Black", font=(("@Yu Gothic", 15, "underline")), show="*")
        self.password_entry.place(x=630, y=390)

        # Login Button Widget
        self.loginBtn = Button(self.root, text='Login', bg="Black", fg="White", font=(("@Yu Gothic", 15, "bold")),
                               command=self.login_user)
        self.loginBtn.place(x=639, y=490)

        self.loginBtn = Button(self.root, text='Back', bg="Black", fg="White", font=(("@Yu Gothic", 15, "bold")),
                               command=self.open_welcome_screen_page)
        self.loginBtn.place(x=760, y=490)

        self.root.mainloop()

    def login_user(self):
        if self.username_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter username first")
        elif self.password_entry.get() == "":
            messagebox.showwarning("Alert!", "Please enter password first")
        else:
            login_details = (self.username_entry.get().strip(), self.password_entry.get())
            print("Login details - ", login_details)

            result = Database.admin_login(login_details)
            if result:
                messagebox.showinfo('Message', 'Login Successfully')
                self.root.destroy()
                w = dashboard_screen.DashboardScreen()
                w.dashboard_screen_menus()
                w.dashboard_screen_widgets()
            else:
                messagebox.showerror('Alert!', 'Invalid username or password.')

    def open_welcome_screen_page(self):
        self.root.destroy()
        w = welcome_screen.WelcomeScreen()
        w.welcome_screen_widgets()


if __name__ == "__main__":
    l = LoginPage()
    l.login_widgets()
