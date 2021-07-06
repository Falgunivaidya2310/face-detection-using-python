from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from MAIN import Face_Recognition_System

root1=Tk()

class Mainwindow:

    def __init__(self,root1):
        self.root1=root1
        self.root1.title("Login Page")
        self.root1.geometry("710x400+0+0")
        self.root1.resizable(False,False)

        self.image=ImageTk.PhotoImage(file="front.jpg")
        self.label=Label(self.root1,image=self.image).pack()

        # self.lbel=Label(self.root1,text="Automatic Society Security Task",font=('times new roman',16,'bold'),bg=None)
        # self.lbel.place(x=0,y=5,width=1200,height=40)

        # self.frame=Frame(self.root1)
        # self.frame.place(x=100,y=130,width=400,height=450)

        self.userLabel1=Label(self.root1,text="Username",font=("Andalus",14,'bold'))
        self.userLabel1.place(x=40,y=50)
        self.form1=Entry(self.root1,font=("times new roman",12))
        self.form1.place(x=40, y=90, width=220)

        self.passLabel2=Label(self.root1,text="Password",font=("Andalus",14,'bold'))
        self.passLabel2.place(x=40,y=150)
        self.form2=Entry(self.root1,show="*",font=("times new roman",12))
        self.form2.place(x=40,y=190, width=220)

        self.btn1=Button(self.root1,text="Login",activebackground='#191970',activeforeground='white',fg='black',bg='#F0F8FF',font=("Arial",14,'bold'),command=lambda:self.logindata())
        self.btn1.place(x=40,y=300,width=80)

        self.btn2 = Button(self.root1, text="Next", activebackground='#191970', activeforeground='white', fg='black',command=self.next,
                           bg='#F0F8FF', font=("Arial", 14, 'bold'))
        self.btn2.place(x=150, y=300, width=80)

    def next(self):
        if self.form1.get() == '' or self.form2.get() == '':
            messagebox.showerror("WARNING","All fields must be filled")

        else:
            self.new_window = Toplevel(self.root1)
            self.app = Face_Recognition_System(self.new_window)

    def logindata(self):
        con=pymysql.connect(host="localhost",user='root',password='Minsuga#swag',database='login_management')
        cur=con.cursor()
        cur.execute("Select * from login where Username=%s and Password=%s",(self.form1.get(),self.form2.get()))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("WARNING","User Not Found")
        else:
            messagebox.showinfo("SUCCESS", "Login Successfully")



main=Mainwindow(root1)
root1.mainloop()