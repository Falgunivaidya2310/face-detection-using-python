from tkinter import *
from tkinter import Label
import numpy as np
import cv2
from PIL import Image,ImageTk
import os
from train import Train
import face_recognition
from datetime import datetime
import pymysql as pymysql
from add import Upload
from mail import Mail
from showAtt import showAttendance

path='trainimg'
images=[]
imgLabel=[]
mylst=os.listdir(path)

def open_img():
    os.startfile("trainimg")

def exit_btn():
    exit()


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        self.image=ImageTk.PhotoImage(file="front1.png")
        self.label=Label(self.root,image=self.image).pack()

        text_lbl=Label(self.root,text="Automatic Society Security Task",font=("times new roman",35,"bold"),bg='white',fg='black')
        text_lbl.place(x=0,y=2,width=1200,height=55)

        self.btn_img1=ImageTk.PhotoImage(file="resize_add.png")
        Btn1=Button(self.root,command=self.add_new,image=self.btn_img1,cursor="hand2")
        Btn1.place(x=300,y=100,width=100,height=100)

        self.btn_img2=ImageTk.PhotoImage(file="camera2.jpg")
        Btn2=Button(self.root,command=self.face,image=self.btn_img2,cursor="hand2")
        Btn2.place(x=100,y=300,width=100,height=100)

        self.btn_img3 = ImageTk.PhotoImage(file="gmail1.png")
        Btn3 = Button(self.root, image=self.btn_img3,cursor="hand2",command=self.mail_btn)
        Btn3.place(x=300, y=500, width=100, height=100)

        self.btn_img4 = ImageTk.PhotoImage(file="file1.jpg")
        Btn4 = Button(self.root, image=self.btn_img4,cursor="hand2",command=self.att_btn)
        Btn4.place(x=880, y=180, width=100, height=100)

        self.btn_img6 = ImageTk.PhotoImage(file="exit1.png")
        Btn6 = Button(self.root, image=self.btn_img6,cursor="hand2",command=exit_btn)
        Btn6.place(x=600, y=570, width=100, height=100)

        self.btn_img7 = ImageTk.PhotoImage(file="crowd1.jpg")
        Btn7 = Button(self.root, image=self.btn_img7, cursor="hand2",command=open_img)
        Btn7.place(x=950, y=420, width=100, height=100)

    def train(self):
        self.new_window2=Toplevel(self.root)
        self.app=Train(self.new_window2)

    # def face_data(self):
    #     self.new_window1=Toplevel(self.root)
    #     self.app=Face_Recognition(self.new_window1)

    def add_new(self):
        self.new_window=Toplevel(self.root)
        self.app=Upload(self.new_window)

    def mail_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Mail(self.new_window)

    def att_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=showAttendance(self.new_window)

    def face(self):
        for cl in mylst:
            curimg = cv2.imread(f'{path}\\{cl}')
            images.append(curimg)
            imgLabel.append(os.path.splitext(cl)[0])

        def findEncodings(images):
            encodLst = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodLst.append(encode)
            return encodLst

        encodlstKnowFaces = findEncodings(images)

        def markAttendance2(name, inTime, InDate):
            conn = pymysql.connect(host='localhost', user='root', password='Minsuga#swag',
                                   database='login_management')

            cursor = conn.cursor()

            sql = '''insert into attendance (Name,InDate,InTime) values(%s, %s, %s)'''

            val = (name, InDate, inTime)
            cursor.execute(sql, val)
            conn.commit()

        webcam = cv2.VideoCapture(0)
        nm = "a"

        while True:
            success, img = webcam.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurFrm = face_recognition.face_locations(imgS)
            encodeCurFrm = face_recognition.face_encodings(imgS, faceCurFrm)

            for encodFace, faseLocation in zip(encodeCurFrm, faceCurFrm):
                maches = face_recognition.compare_faces(encodlstKnowFaces, encodFace)
                faceDis = face_recognition.face_distance(encodlstKnowFaces, encodFace)

                machesIndex = np.argmin(faceDis)

                if maches[machesIndex]:
                    name = imgLabel[machesIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faseLocation
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                    crTime = datetime.now().time()
                    crDate = datetime.now().date()
                    if name != nm:
                        markAttendance2(name, str(crTime), str(crDate))
                        nm = name

            cv2.imshow('Frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        webcam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()