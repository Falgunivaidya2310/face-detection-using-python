from tkinter import *
from tkinter import ttk
import pymysql

class showAttendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("820x330")
        self.root.title("Attendance Records")

        # search_frame = LabelFrame(root, bd=2, bg="white", relief=RIDGE, text="Search System",
        #                           font=("arial", 10, "bold"))
        # search_frame.place(x=5, y=10, width=690, height=70)
        #
        # search_label = Label(search_frame, bg="white", text='Search By', font=("arial", 10, "bold"))
        # search_label.place(x=5, y=7)
        # search_combo = ttk.Combobox(search_frame, font=("arial", 8, "bold"), state="readonly", width=15)
        # search_combo["values"] = ("Name", "Date", "Time")
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

        table_frame = Frame(root, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=20, width=800, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        record_table = ttk.Treeview(table_frame, column=(
            "Name", "Date", "Time"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=record_table.xview)
        scroll_y.config(command=record_table.yview)

        record_table.heading("Name", text="Name")
        record_table.heading("Date", text="Date")
        record_table.heading("Time", text="Time")
        record_table['show'] = "headings"
        record_table.pack(fill=BOTH, expand=1)

        record_table.column("Name", width=80)
        record_table.column("Date", width=80)
        record_table.column("Time", width=80)

        conn = pymysql.connect(host='localhost', user='root', password='Minsuga#swag', database='login_management')
        cur = conn.cursor()
        cur.execute("select * from attendance")
        data = cur.fetchall()

        if len(data)!=0:
            record_table.delete(*record_table.get_children())
            for i in data:
                record_table.insert("",END,values=i)
            conn.commit()
            conn.close()

if __name__ == "__main__":
    root=Tk()
    obj = showAttendance(root)
    root.mainloop()