from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("600x380+0+0")
        self.root.title("Train images")
        self.root.resizable(False, False)

        self.btn_bg = ImageTk.PhotoImage(file="train_bg.jpg")
        Btn = Button(self.root,command=self.train_classifier, image=self.btn_bg, cursor="hand2")
        Btn.pack()

    def train_classifier(self):
        data_dir = ("TrainingImages")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        name = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            names = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            name.append(names)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        name = np.array(name)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, name)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results", "All datasets are trained")


if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()