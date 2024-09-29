from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import welcome_screen, dashboard_department, Database


class DepartmentLogin:
    def __init__(self):
        self.root = Tk()
        self.root.title('Login | Department Panel')
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def department_login_page_widgets(self):
        self.image_path = Image.open('images/User.png').resize((1000, 600))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.imgLBL = Label(self.root, image=self.imgTk, width=1000, height=600)
        self.imgLBL.place(x=0, y=0)

        # typing box for user name
        self.username_entry = Entry(self.root, bg='White', fg="Black", font=(("@Yu Gothic", 15, "")))
        self.username_entry.place(x=384, y=288, width=170)

        # typing box of password
        self.password_entry = Entry(self.root, bg='White', fg="Black", font=(("@Yu Gothic", 15, "underline")),
                                    show="*")
        self.password_entry.place(x=384, y=398, width=170)

        # creating login button
        self.loginBtn = Button(self.root, text='LOGIN', bg="White", fg="Black", font=(("@Yu Gothic", 15, "bold")),
                               command=self.run_login_user)
        self.loginBtn.place(x=370, y=480)

        self.backBtn = Button(self.root, text='BACK', bg="white", fg="black", font=(("@Yu Gothic", 15, "bold")),
                              command=self.open_welcome_screen)
        self.backBtn.place(x=495, y=480)

        self.root.mainloop()

    def run_login_user(self):

        if self.username_entry.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter username first")
        elif self.password_entry.get() == "":
            messagebox.showwarning("Alert!", "Please enter username first")
        else:
            print(f'Username is {self.username_entry.get()}, Password is {self.password_entry.get()}')
            login_details = (self.username_entry.get(), self.password_entry.get())
            login_result = Database.department_login(login_details)
            if login_result:
                print("Logged in user - ", login_result)
                messagebox.showinfo("Message", "Login Successful")
                self.root.destroy()
                d = dashboard_department.DepartmentDashboard(login_result)
                d.dashboard_department_page_menus()
                d.dashboard_department_page_widgets()
            else:
                messagebox.showwarning("Alert!", "Please check your username or password")

    def open_welcome_screen(self):
        self.root.destroy()
        w = welcome_screen.WelcomeScreen()
        w.welcome_screen_widgets()


if __name__ == "__main__":
    d = DepartmentLogin()
    d.department_login_page_widgets()
