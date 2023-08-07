from cProfile import label
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar

root = Tk()
root.title("BLOOD BANK MGMT")
w=1200
h=750
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
root.geometry("%dx%d+%d+%d" % (w,h,x,y))

#font style
look = "Adobe Caslon Pro"

booking_frame = Frame(root, bg="white", width=900, height=600).place(x=150, y=50)
title = Label(booking_frame, text= "CHECK COMPABILITY",font= ("look", 20),fg= "red", background = "white")
title.place(x=150, y=90)

###Blood group
BG_lbl = Label(booking_frame, text="Blood Group",font=("look", 16), bg="white")
BG_lbl.place(x=300, y=200)
BG_lbl=["AB+", "AB-", "A+", "A-", "B+","B-", "O+", "O-"]
clicked = StringVar()
clicked.set("Select Blood group")
BGdropbox = OptionMenu(booking_frame, clicked, *BG_lbl)
BGdropbox.place(x=500, y=200, width=200, height=40)
BGdropbox.config(bg = "lightblue", activebackground="white")


def get():
    A = clicked.get()
    if A == "AB+":
        ABp_lbl =Label(booking_frame, text = "The compatable blood groups priority wise AB+ AB- A+ A- B+ B- O+ O-", font=("look", 16), bg="white")
        ABp_lbl.place(x= 300, y = 450)
    elif A == "AB-":
        ABn_lbl =Label(booking_frame, text = "The compatable blood groups priority wise AB- A- B- O-", font=("look", 16), bg="white")
        ABn_lbl.place(x= 300, y = 450)
    elif A == "A+":
        ABp_lbl =Label(booking_frame, text = "The compatable blood groups priority wise A+ A- O+ O-", font=("look", 16), bg="white")
        ABp_lbl.place(x= 300, y = 450)
    elif A == "A-":
        ABn_lbl =Label(booking_frame, text = "The compatable blood groups priority wise A- O-", font=("look", 16), bg="white")
        ABn_lbl.place(x= 300, y = 450)
    elif A == "B+":
        ABp_lbl =Label(booking_frame, text = "The compatable blood groups priority wise B+ B- O+ O-", font=("look", 16), bg="white")
        ABp_lbl.place(x= 300, y = 450)
    elif A == "B-":
        ABn_lbl =Label(booking_frame, text = "The compatable blood groups priority wise B- O-", font=("look", 16), bg="white")
        ABn_lbl.place(x= 300, y = 450)
    elif A == "O+":
        ABp_lbl =Label(booking_frame, text = "The compatable blood groups priority wise O+ O-", font=("look", 16), bg="white")
        ABp_lbl.place(x= 300, y = 450)
    else:
        ABn_lbl =Label(booking_frame, text = "The compatable blood group is O-", font=("look", 16), bg="white")
        ABn_lbl.place(x= 300, y = 450)
    


def search_BB():
    root.destroy()
    import Searchdonor
searchbtn = Button(booking_frame, text="Search", width = 20,height= 2,font=("look","14"), bg = "white", fg="black", activebackground="white",
                   command=get)
searchbtn.place(x=200, y=350)


def booking_back():
    root.destroy()
    import Menupage
back_btn = Button(booking_frame, text="Back",width = 20,height= 2, font=("look","14"), bg = "white", activebackground="white",fg="black",
                  command=booking_back)
back_btn.place(x=500, y=350)


root.mainloop()