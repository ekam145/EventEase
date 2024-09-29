from tkinter import *
from PIL import Image, ImageTk
import login_page, login_department


class WelcomeScreen:
    def __init__(self):
        self.root = Tk()
        self.root.title('EventEase | Administration Panel |')
        self.root.resizable(False, False)
        self.root.geometry('1000x600')

    def welcome_screen_widgets(self):
        # inserting image
        self.image_path = Image.open('images/Event Ease.png').resize((1000, 600))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.imgTk, width=1000, height=600)
        self.image_label.place(x=0, y=0)

        self.loginBtn = Button(self.root, text='ADMIN LOGIN', width='18', height='2', bg="black", fg="white",
                               font=(("@Yu Gothic", 15, "bold")), command=self.open_admin_login_page)
        self.loginBtn.place(x=250, y=340)

        self.loginBtn = Button(self.root, text='DEPARTMENT LOGIN', width='18', height='2', bg="black", fg="white",
                               font=(("@Yu Gothic", 15, "bold")), command=self.open_user_login_page)
        self.loginBtn.place(x=505, y=340)

        self.root.mainloop()

    def open_admin_login_page(self):
        self.root.destroy()
        l = login_page.LoginPage()
        l.login_widgets()

    def open_user_login_page(self):
        self.root.destroy()
        l = login_department.DepartmentLogin()
        l.department_login_page_widgets()


if __name__ == '__main__':
    w = WelcomeScreen()
    w.welcome_screen_widgets()
