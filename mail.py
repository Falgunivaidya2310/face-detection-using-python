from tkinter import *
import smtplib
from PIL import ImageTk

class Mail:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Sending Mail")
        self.root.resizable(False, False)

        self.btn_bg = ImageTk.PhotoImage(file="mail_icon-2.png")
        Btn = Label(self.root, image=self.btn_bg)
        Btn.pack()

        self.address = StringVar()
        self.message = StringVar()

        self.label1 = Label(self.root, text="Email Sending App", relief="solid", width=20, font=("arial", 19, "bold"))
        self.label1.place(x=90, y=195)

        self.lb2 = Label(self.root, text='Recipents Address: ', width=20, font=('Calibri', 15, 'bold'))
        self.lb2.place(x=20, y=280)
        self.fill3 = Entry(self.root, textvar=self.address, width=20, font=('Calibri', 15, 'bold'))
        self.fill3.place(x=250, y=284)

        self.lb3 = Label(self.root, text='Message: ', width=20, font=('Calibri', 15, 'bold'))
        self.lb3.place(x=40, y=350)
        self.fill4 = Entry(self.root, textvar=self.message, width=20, font=('Calibri', 15, 'bold'))
        self.fill4.place(x=250, y=352)

        self.b1 = Button(self.root, text='Send', width=15, bg="brown", fg="white", command=self.send_message)
        self.b1.place(x=80, y=430)

        self.b2 = Button(self.root, text='Reset', width=15, bg="brown", fg="white", command=self.reset)
        self.b2.place(x=280, y=430)

    def reset(self):
        self.fill3.delete(0, 'end')
        self.fill4.delete(0, 'end')

    def send_message(self):
        self.sender_mail = "falguni.vaidya23@gmail.com"
        self.sender_password = "Falguni@2001"

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_mail,self.sender_password)

        self.adress_info = self.address.get()
        self.message_info = self.message.get()

        self.server.sendmail(self.sender_mail,self.adress_info,self.message_info)

        print("Message Sent")


if __name__ == "__main__":
    root=Tk()
    obj = Mail(root)
    root.mainloop()