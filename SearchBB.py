from cProfile import label
from tkinter import *
import webbrowser
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import Calendar
import combined as xa

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
title = Label(booking_frame, text= "SEARCH NEAREST BLOOD BANK",font= ("look", 20),fg= "red", background = "white")
title.place(x=150, y=90)

###Blood group
BG_lbl = Label(booking_frame, text="Locations",font=("look", 12), bg="white")
BG_lbl.place(x=170, y=200)
BG_lbl=["Velachery", "Kamatchi Hospital-", "Chrompet", "Tambaram", "Thoraipakkam","Shollinganallur", "Guindy", "Kathipara", 
"Vadapalani", "CMBT", "Thirumangalam", "Anna Nagar", "Aminjikarai", "Egmore"]
clicked = StringVar()
clicked.set("Select your location")
BGdropbox = OptionMenu(booking_frame, clicked, *BG_lbl)
BGdropbox.place(x=350, y=200, width=200, height=40)
BGdropbox.config(bg = "lightblue", activebackground="white")
#locdic = { 'Velachery': 0, 'Kamatchi Hospital': 1, 'Chrompet': 2, 'Tambaram': 3, 'Thoraipakkam' : 4, 'Shollinganallur': 5,
#'Guindy': 6, 'kathipara': 7, 'Vadapalani': 8, 'CMBT':9, 'Thirumangalam': 10, 'Anna Nagar':11, 'Aminjikarai':12, 'Egmore':13}
locdic=["Velachery", "Kamatchi Hospital-", "Chrompet", "Tambaram", "Thoraipakkam","Shollinganallur", "Guindy", "Kathipara", 
"Vadapalani", "CMBT", "Thirumangalam", "Anna Nagar", "Aminjikarai", "Egmore"]
def get():
    choice = clicked.get()
    print(choice)
    for i in range (0, len(locdic)):
        if choice == locdic [i]:
            start = i
            print(start)
            xa.mapping(start)
            webbrowser.open("E:\\ADS PROJECT PYTHON\\Program files\\mappy.html")
    

def search_BB():
    root.destroy()
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