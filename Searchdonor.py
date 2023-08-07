from cProfile import label
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
#from Priorityq import ABp
from bloodcomplist import ABp, ABn, On, Op, Bn, Bp, Ap, An, disp, sync
#from Priorityq import ABp, ABn, On, Op, Bn, Bp, Ap, An, roll, pqdis


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
title = Label(booking_frame, text= "SEARCH DONOR",font= ("look", 20),fg= "red", background = "white")
title.place(x=150, y=90)

###Blood group
BG_lbl = Label(booking_frame, text="Blood Group",font=("look", 18), bg="white")
BG_lbl.place(x=170, y=200)
BG_lbl=["ABp", "ABn", "Ap", "An", "Bp","Bn", "Op", "On"]
clicked = StringVar()
clicked.set("Select Blood group")
BGdropbox = OptionMenu(booking_frame, clicked, *BG_lbl)
BGdropbox.place(x=350, y=200, width=200, height=50)
BGdropbox.config(bg = "lightblue", activebackground="white")

def search_DD():
    root.destroy()
    import search_det

def search_BB():
    BG_re = clicked.get()
    bgd = globals()[BG_re]
    print(BG_re)
    sync()
    donor_id = disp(bgd)
    id_lbl=Label(booking_frame, text="Donor id",font= ("look", 12), bg = "white")
    id_lbl.place(x=170,y=440)
    id_lnlE=Entry(booking_frame, font=("look","12"), bg="light blue", bd=1)
    id_lnlE.insert(0,donor_id )
    id_lnlE.place(x=350, y=440, width=200, height=40)
    searchbtn = Button(booking_frame, text="Search", width = 20,height= 2,font=("look","14"), bg = "white", fg="black", activebackground="white",
                   command=search_DD)
    searchbtn.place(x=200, y=550)



searchbtn = Button(booking_frame, text="Search", width = 20,height= 2,font=("look","14"), bg = "white", fg="black", activebackground="white",
                   command=search_BB)
searchbtn.place(x=200, y=350)


def booking_back():
    root.destroy()
    import Menupage

back_btn = Button(booking_frame, text="Back",width = 20,height= 2, font=("look","14"), bg = "white", activebackground="white",fg="black",
                  command=booking_back)
back_btn.place(x=700, y=350)

def searchpq():
    BG_re = clicked.get()
    bgd = globals()[BG_re]
    #roll()
    print(BG_re)
    #donor_id_tup = pqdis(bgd)
    #donor_id = donor_id_tup[1]
    id_lbl=Label(booking_frame, text="Donor id",font= ("look", 12), bg = "white")
    id_lbl.place(x=170,y=440)
    id_lnlE=Entry(booking_frame,font=("look","12"), bg="light blue", bd=1)
    #id_lnlE.insert(0,donor_id )
    id_lnlE.place(x=350, y=440, width=200, height=40)
    searchbtn = Button(booking_frame, text="Search", width = 20,height= 2,font=("look","14"), bg = "white", fg="black", activebackground="white",
                   command=search_DD)
    searchbtn.place(x=200, y=550)
    


back_btn = Button(booking_frame, text="Min age",width = 20,height= 2, font=("look","14"), bg = "white", activebackground="white",fg="black",
                  command=searchpq)
back_btn.place(x=450, y=350)


root.mainloop()