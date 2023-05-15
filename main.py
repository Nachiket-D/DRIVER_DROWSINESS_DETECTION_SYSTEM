from tkinter import *
import ctypes,os
from tkinter.tix import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename


home = Tk()
img = Image.open("images/DRIVER DROWSINESS.png")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-610)
b= str(lt[1]//2-383)
home.title("DRIVER DROWSINESS")
home.geometry("1243x738+"+a+"+"+b)
home.resizable(0,0)

photo = Image.open("images/button.png")
img2 = ImageTk.PhotoImage(photo)

def add():
    root= Tk()
    root.title("DRIVER DROWSINESS")
    root.geometry("500x300")
    root.resizable(0,0)
    root.config(bg="#1b2b39")

def web():
    import sleep_detection

def about():
    aboutwin = Toplevel()
    img = Image.open("images/about.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(aboutwin, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-610)
    b= str(lt[1]//2-383)
    aboutwin.title("DRIVER DROWSINESS")
    aboutwin.geometry("1243x738+"+a+"+"+b)
    aboutwin.resizable(0,0)
    aboutwin.mainloop()

def contact():
    contactwin = Toplevel()
    img = Image.open("images/contact.png")
    img = ImageTk.PhotoImage(img)
    panel = Label(contactwin, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-610)
    b= str(lt[1]//2-383)
    contactwin.title("DRIVER DROWSINESS")
    contactwin.geometry("1243x738+"+a+"+"+b)
    contactwin.resizable(0,0)
    contactwin.mainloop()

def Exit():
    result = tkMessageBox.askquestion(
        'DRIVER DROWSINESS', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')
                    
Button(home, highlightthickness = 0, bd = 0,activebackground="#fbfdff", image = img2,command=web).place(x=40,y=530)

Button(home, highlightthickness = 0, bd = 0,activebackground="#fbfdff",background="#fbfdff",font=("",18,"bold"),fg = "#1b2b39", text = "About",command=about).place(x=840,y=25)

Button(home, highlightthickness = 0, bd = 0,activebackground="#fbfdff",background="#fbfdff",font=("",18,"bold"),fg = "#1b2b39", text = "Contact",command=contact).place(x=968,y=25)

Button(home, highlightthickness = 0, bd = 0,activebackground="#fbfdff",background="#fbfdff",font=("",18,"bold"),fg = "#1b2b39", text = "Exit",command=Exit).place(x=1125,y=25)

home.mainloop()
