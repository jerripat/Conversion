import string
from tkinter import *
import os
from tkinter import Menu

tk = Tk ()
tk.title ( "Calorie Counter" )
tk.geometry ( "400x350" )
formBgColor = '#134ead'
formFgColor = '#eded1a'
btnColor = '#1aeb21'
radioGrpBg = '#204e99'
tk.configure ( background = formBgColor )

radioGrp = IntVar ()
radioGrp.set ( 1 )
usrname = os.getlogin ()
username = string.capwords ( usrname )
dataFrame = Frame ( tk )
lblOne = (Label ( dataFrame, text = "Lets collect some Data!!", width = "400", height = "350", font = ("Arial", 16),
                  bg = formBgColor ))

# First frame
frame_one = Frame(tk, width=200, height=200,bd=5, bg=formBgColor)
#frame_one.place(relx=0.5,rely=0.5,anchor=CENTER)
frame_one_label = Label(frame_one, text="Enter your weight", font=("Arial",12),bg='white',fg='black')
#frame_one_label.place(relx=0.5,rely=0.25,anchor=CENTER)


def fakeCommand():

    pass


def hide():
   pass

def show():
    pass

def getUser(userId):
    wht = 0
    hgt = 0.0
    time = 0.0
    if userId == 1:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
        txtUser = Entry ( tk, font = ("Arial", 12), bg = formBgColor, fg = formFgColor )
        txtUser.place ( relx = 0.5, rely = 0.6, anchor = N )  # Placed at the top center


def radioChoice():
    # btnStart.destroy()
    # lblMarquee.destroy()

    if radioGrp.get () == 1:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
    elif radioGrp.get () == 2:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
    else:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center


# This is the greeting Label
lblMarquee = Label ( tk, text = f"Welcome to the Calorie Counter {username}",
                     bg = formBgColor, fg = formFgColor, font = ("Arial", 16) )
lblMarquee.place ( relx = 0.5, rely = 0.1, anchor = N )  # Placed at the top center

radYes = Radiobutton ( tk, text = "Yes", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 1 )
radNo = Radiobutton ( tk, text = "No", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 2 )
radElse = Radiobutton ( tk, text = "Someone else", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 3 )
btnSubmit = Button ( tk, text = "Submit", command = getUser, font = ("Mono", 11), width = 6, height = 1 )
lblAskWeight = (Label ( tk, text = "Please enter your weight", font = ("Arial",) ))
lblAskHeight = (Label ( tk, text = "Please enter your height", font = ("Arial",) ))
lblAskTime = (Label ( tk, text = "Please enter your time", font = ("Arial",) ))
entWeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor )
entHeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor )
entTime = Entry ( tk, font = ("Arial", 12), bg = formBgColor )


def start():
    lblAsk = (Label ( tk, text = "Would you like to start a log session?", font = ("Arial", 12), bg = formBgColor,
                      fg = formFgColor ))
    lblAsk.place ( relx = 0.5, rely = 0.5, anchor = CENTER )  # Placed at the top center
    radYes.place ( relx = 0.3, rely = 0.55, anchor = N )
    radNo.place ( relx = 0.4, rely = 0.55, anchor = N )
    radElse.place ( relx = 0.6, rely = 0.55, anchor = N )
    btnSubmit.place ( relx = 0.5, rely = 0.7, anchor = N )  # Placed at the top center


# Define a menu
my_menu = Menu ( tk )
tk.config ( menu = my_menu )

# Create menu items
file_menu = Menu ( my_menu, tearoff = 0 )

my_menu.add_cascade ( label = "File", menu =file_menu)
file_menu.add_command ( label = "New", command = fakeCommand )
file_menu.add_command ( label = "Exit", command = tk.quit )

# Create Edit menu items
edit_menu = Menu ( my_menu, tearoff = 0 )
my_menu.add_cascade ( label = "Edit", menu =edit_menu)
edit_menu.add_command ( label = "Cut", command = fakeCommand )
edit_menu.add_command ( label = "Exit", command = tk.quit )



btnStart = Button ( tk, text = "Start", command = start, width = 5, height = 1, font = ("Arial", 11) )
btnStart.place ( relx = 0.5, rely = 0.28, anchor = N )  # Placed at the top center

tk.mainloop ()
