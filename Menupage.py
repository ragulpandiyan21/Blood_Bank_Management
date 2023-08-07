import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root = Tk()
root.title("Blood Bank Mgmt")
w=1200
h=750
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
root.geometry("%dx%d+%d+%d" % (w,h,x,y))

#font style
look = "Adobe Caslon Pro"

#bg


#############bg_image
lbl = Label(root, width=1200, height=750).place(x=0, y=0)

def donor_page():
    root.destroy()
    import Regdonor
frame = Frame(root, bg="lightblue", width=900, height=570).place(x=170, y=120)
registerbtn = Button(frame, text="DONOR REGISTRATION",width = 20,height= 2,font=("look","12"), bg = "white", fg="black", activebackground="white",
                    command=donor_page)
registerbtn.place(x=250,y=350)
#cancel
def searchbg():
    root.destroy()
    import SearchBG
checkBCbtn = Button(frame, text="CHECK BLOOD COMP", width = 20,height= 2,font=("look","12"), bg = "white", fg="black", activebackground="white",
                   command=searchbg)
checkBCbtn.place(x=500, y=350)

def search_door():
    root.destroy()
    import Searchdonor
searchbtn = Button(frame, text="SEARCH FOR DONOR", width = 20,height= 2,font=("look","12"), bg = "white", fg="black", activebackground="white",
                   command=search_door)
searchbtn.place(x=750, y=350)

def search_BB():
    root.destroy()
    import SearchBB
searchbtn = Button(frame, text="SEARCH FOR BLOOD BANK", width = 25,height= 2,font=("look","12"), bg = "white", fg="black", activebackground="white",
                   command= search_BB)
searchbtn.place(x=280, y=450)

def search_DD():
    root.destroy()
    import search_by_id
searchbtn = Button(frame, text="SEARCH FOR DONOR DETAILS", width = 26,height= 2,font=("look","12"), bg = "white", fg="black", activebackground="white",
                   command= search_DD)
searchbtn.place(x=580, y=450)

root.mainloop()