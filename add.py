from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import cv2

class Upload:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x750")
        self.root.title("Registration form")
        self.root.resizable(False, False)

        self.btn_bg = ImageTk.PhotoImage(file="admin.png")
        Btn = Label(self.root, image=self.btn_bg)
        Btn.pack()

        self.fn = StringVar()
        self.ln = StringVar()
        self.age = StringVar()
        self.dob = StringVar()
        self.fad = StringVar()
        self.prof = StringVar()
        self.bldg = StringVar()
        self.tele = StringVar()
        self.gender = StringVar()

        self.label1 = Label(self.root, text="Registration Form", relief="solid", width=20, font=("arial", 19, "bold"))
        self.label1.place(x=100, y=150)

        self.label2 = Label(self.root, text="FirstName: ", width=20, font=("arial", 10, "bold"))
        self.label2.place(x=40, y=230)
        self.entry2 = Entry(self.root, textvar=self.fn)
        self.entry2.place(x=230, y=232)

        self.label3 = Label(self.root, text="LastName: ", width=20, font=("arial", 10, "bold"))
        self.label3.place(x=40, y=280)
        self.entry3 = Entry(self.root, textvar=self.ln)
        self.entry3.place(x=230, y=282)

        self.label4 = Label(self.root, text="Age: ", width=20, font=("arial", 10, "bold"))
        self.label4.place(x=40, y=330)
        self.entry4 = Entry(self.root, textvar=self.age)
        self.entry4.place(x=230, y=332)

        self.label5 = Label(self.root, text="Date of Birth: ", width=20, font=("arial", 10, "bold"))
        self.label5.place(x=40, y=380)
        self.entry5 = Entry(self.root, textvar=self.dob)
        self.entry5.place(x=230, y=382)

        self.label6 = Label(self.root, text="Full Address: ", width=20, font=("arial", 10, "bold"))
        self.label6.place(x=40, y=430)
        self.entry6 = Entry(self.root, textvar=self.fad)
        self.entry6.place(x=230, y=432)

        self.label7 = Label(self.root, text="Profession: ", width=20, font=("arial", 10, "bold"))
        self.label7.place(x=40, y=480)
        self.list1 = ['Milkman', 'Newspaper-Delivery', 'Maid', 'Watchman1','Watchman2']
        self.droplist = OptionMenu(self.root, self.prof, *self.list1)
        self.prof.set("Choose Profession")
        self.droplist.config(width=15)
        self.droplist.place(x=230, y=480)

        self.label8 = Label(self.root, text="Building No: ", width=20, font=("arial", 10, "bold"))
        self.label8.place(x=40, y=530)
        self.list2 = ['K3/5', 'K3/6', 'K3/7']
        self.droplist = OptionMenu(self.root, self.bldg, *self.list2)
        self.bldg.set("Choose Bldng no")
        self.droplist.config(width=15)
        self.droplist.place(x=230, y=530)

        self.label9 = Label(self.root, text="Telephone No: ", width=20, font=("arial", 10, "bold"))
        self.label9.place(x=40, y=580)
        self.entry9 = Entry(self.root, textvar=self.tele)
        self.entry9.place(x=230, y=582)

        self.label10 = Label(self.root, text="Gender: ", width=20, font=("arial", 10, "bold"))
        self.label10.place(x=40, y=630)
        self.list3 = ['Male', 'Female', 'Others']
        self.droplist = OptionMenu(self.root, self.gender, *self.list3)
        self.gender.set("Choose Gender")
        self.droplist.config(width=15)
        self.droplist.place(x=230, y=630)

        self.b4 = Button(self.root, text="Save", width=12, bg="brown", fg="white", command=lambda:self.add_data())
        self.b4.place(x=200, y=690)

        self.b5 = Button(self.root, text="Show Records", width=12, bg="brown", fg="white", command=self.show)
        self.b5.place(x=350, y=690)

        self.b3 = Button(self.root, command=self.generate_dataset, text="Take Photo", width=12, bg="brown", fg="white")
        self.b3.place(x=50, y=690)

    def show(self):
        frame = Tk()
        frame.geometry("1000x330")
        frame.title("Show Records")

        # search_frame = LabelFrame(frame, bd=2, bg="white", relief=RIDGE, text="Search System",
        #                           font=("arial", 10, "bold"))
        # search_frame.place(x=5, y=10, width=690, height=70)
        #
        # search_label = Label(search_frame, bg="white", text='Search By', font=("arial", 10, "bold"))
        # search_label.place(x=5, y=7)
        # search_combo = ttk.Combobox(search_frame, font=("arial", 8, "bold"), state="readonly", width=15)
        # search_combo["values"] = ("Select", "Name", "Phone_No")
        # search_combo.current(0)
        # search_combo.place(x=85, y=8)
        # search_entry = ttk.Entry(search_frame, width=20, font=("arial", 10, "bold"))
        # search_entry.place(x=250, y=7)
        #
        # search_btn = Button(search_frame, text="Search", width=10, font=("arial", 10, "bold"), bg="brown",
        #                     fg="white")
        # search_btn.place(x=450, y=7)
        #
        # show_btn = Button(search_frame, text="Show All", width=10, font=("arial", 10, "bold"), bg="brown",
        #                   fg="white")
        # show_btn.place(x=550, y=7)

        table_frame = Frame(frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=20, width=990, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        record_table = ttk.Treeview(table_frame, column=(
            "FirstName", "LastName", "Age", "DOB", "Address", "Profession", "Bldg_No", "Phone_No", "Gender"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=record_table.xview)
        scroll_y.config(command=record_table.yview)

        record_table.heading("FirstName", text="FirstName")
        record_table.heading("LastName", text="LastName")
        record_table.heading("Age", text="Age")
        record_table.heading("DOB", text="Date Of Birth")
        record_table.heading("Address", text="Full Address")
        record_table.heading("Profession", text="Profession")
        record_table.heading("Bldg_No", text="Building No")
        record_table.heading("Phone_No", text="Phone No")
        record_table.heading("Gender", text="Gender")
        record_table['show'] = "headings"
        record_table.pack(fill=BOTH, expand=1)

        record_table.column("FirstName", width=100)
        record_table.column("LastName", width=100)
        record_table.column("Age", width=100)
        record_table.column("DOB", width=100)
        record_table.column("Address", width=100)
        record_table.column("Profession", width=100)
        record_table.column("Bldg_No", width=100)
        record_table.column("Phone_No", width=100)
        record_table.column("Gender", width=100)

        conn = pymysql.connect(host='localhost', user='root', password='Minsuga#swag', database='login_management')
        cur = conn.cursor()
        cur.execute("select * from upload")
        data = cur.fetchall()

        if len(data)!=0:
            record_table.delete(*record_table.get_children())
            for i in data:
                record_table.insert("",END,values=i)
            conn.commit()
            conn.close()

        frame.mainloop()

    def add_data(self):
        if self.fn.get() == "" or self.ln.get() == "" or self.age.get() == "" or self.dob.get() == "" or self.fad.get() == "" or self.prof.get() == "Select Profession":
            messagebox.showerror("ERROR", "All fields are required!")
        else:
            try:
                conn = pymysql.connect(host='localhost', user='root', password='Minsuga#swag',
                                       database='login_management')
                cur = conn.cursor()
                cur.execute("insert into upload values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.fn.get(), self.ln.get(), self.age.get(), self.dob.get(), self.fad.get(), self.prof.get(),
                    self.bldg.get(), self.tele.get(),
                    self.gender.get()))

                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS", "Student details has been added successfully")

            except EXCEPTION as es:
                messagebox.showerror("ERROR", f"Due to: {str(es)}")

    def generate_dataset(self):
        if self.fn.get() == "" or self.ln.get() == "" or self.age.get() == "" or self.dob.get() == "" or self.fad.get() == "" or self.prof.get() == "Select Profession":
            messagebox.showerror("ERROR", "All fields are required!")
        else:
            # self.root1 = Tk()
            # self.root1.geometry("600x370")
            # self.root1.title("Upload Image")
            #
            # self.labelFrame = ttk.LabelFrame(self, text="Pick a photo")
            # self.labelFrame.place(x=0, y=20)
            fname = self.entry2.get()
            lname = self.entry3.get()
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)

                k = cv2.waitKey(1)
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = fname + lname + ".png".format(img_counter)
                    cv2.imwrite("trainimg\ " + img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()

            cv2.destroyAllWindows()

    # def upload_btn(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=System(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj = Upload(root)
    root.mainloop()