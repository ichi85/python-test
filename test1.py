from tkinter import *
from tkinter import messagebox 
from PIL import ImageTk, Image


    
def __init__(self, root):
    self.root = root
    self.root.title("Login System")
    self.root.geometry("1350x700+0+0")

        #------------------- All Images------------------------

    self.bg_icon=ImageTk.PhotoImage(file="C:/project/python/images/gara.jpg")
    self.user_icon=ImageTk.PhotoImage(file="C:/project/python/images/user.png")
    self.pass_icon=ImageTk.PhotoImage(file="C:/project/python/images/lock.png")
    self.logo_icon=ImageTk.PhotoImage(file="C:/project/python/images/cTanjiro.png")
        
        #------------------- Variables ------------------------
    self.uname=StringVar()
    self.pass_=StringVar()

    bg_lbl=Label(self.root, image=self.bg_icon)
    bg_lbl.pack()

    title=Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="red")
    title.place(x=0, y=0, relwidth=1)

    Login_Frame=Frame(self.root, bg="white")
    Login_Frame.place(x=400, y=150)

    logolbl=Label(Login_Frame, image=self.logo_icon, bd=0)
    logolbl.grid(row=0, column=0, columnspan=2, pady=20)


    lbluser=Label(Login_Frame, text="username", image=self.user_icon, font=("times new roman", 20, "bold"), bg="white")
    lbluser.grid(row=1, column=0, padx=20, pady=10)
    txtuser=Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15))
    txtuser.grid(row=1, column=1, padx=20)

    lblpass=Label(Login_Frame, text="password", image=self.pass_icon, font=("times new roman", 20, "bold"), bg="white")
    lblpass.grid(row=2, column=0, padx=20, pady=10)
    txtpass=Entry(Login_Frame, bd=5, relief=GROOVE, textvariable=self.pass_, font=("", 15))
    txtpass.grid(row=2, column=1, padx=20)

    btn_log=Button(Login_Frame, text="Login", width=15, font=("times new roman", 14, "bold"), bg="yellow", fg="red", command=login)
    btn_log.grid(row=3, column=1, pady=10)


    
def login(self):
    if self.uname.get()=="issei" and self.pass_.get()==str("123456"):
        messagebox.showinfo("Successfull", f"welcome {self.uname.get()}")
    elif self.uname.get()==" " or self.pass_.get()==" ":
        messagebox.showerror("Error", "Don't Login")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

root=Tk()
__init__.mainloop()
root.mainloop()