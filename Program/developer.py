from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\banner.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\bg4.png")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer pannel",font=("tahoma",30,"bold"),bg="sky blue",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\Photo.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        std_b1.place(x=400,y=104,width=180,height=180)

        std_b1_1 = Button(bg_img,text="kawade Ganesh",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=400,y=284,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\IMG_20230427_191041.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=700,y=104,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Kakad Abhishek",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=700,y=284,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\Rushi.jpeg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=1000,y=104,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Karle Rushikesh",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=1000,y=284,width=180,height=45) 
    
      # Photo   button  4
        pho_img_btn=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\Abhishek.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=550,y=384,width=180,height=180)

        pho_b1_1 = Button(bg_img,text="Kale Abhishek",cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=550,y=564,width=180,height=45)

       # Help  Support  Button 5
       
        hlp_img_btn=Image.open(r"C:\Users\YashrajD\Documents\Python_Test_Projects\Images_GUI\Ashutosh.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=850,y=384,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Mule Ashutosh",cursor="hand2",font=("times new roman",17,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=850,y=564,width=180,height=45)













if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()