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

# Define a menu
my_menu = Menu ( tk )
tk.config ( menu = my_menu )
file_menu = Menu ( my_menu, tearoff = 0 )
my_menu.add_cascade ( label = "File", menu = file_menu )
file_menu.add_command ( label = "New" )
file_menu.add_command ( label = "Exit", command = tk.quit )
dataframe = Frame( tk, bg = formBgColor)
dataFrame = LabelFrame ( tk, text = "Data", bg = formBgColor)

def getUser():

    if userId == 1:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
        txtUser = Entry ( tk, font = ("Arial", 12), bg = formBgColor, fg = formFgColor )
        txtUser.place ( relx = 0.5, rely = 0.6, anchor = N )  # Placed at the top center


def radioChoice():
    if radioGrp.get () == 1:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )
    elif radioGrp.get () == 2:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )
    else:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )


# This is the greeting Label
lblMarquee = Label ( tk, text = f"Welcome to the Calorie Counter {username}",
                     bg = formBgColor, fg = formFgColor, font = ("Arial", 16) )
lblMarquee.place ( relx = 0.5, rely = 0.1, anchor = N )  # Placed at the top center
lblAsk = (Label ( tk, text = "Would you like to start a log session?", font = ("Arial", 12), bg = formBgColor,
                  fg = formFgColor ))
radYes = Radiobutton ( tk, text = "Yes", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 1 )
radNo = Radiobutton ( tk, text = "No", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 2 )
radElse = Radiobutton ( tk, text = "Someone else", bg = radioGrpBg, fg = btnColor, variable = radioGrp, value = 3 )
lblAskWeight = (Label ( tk, text = "Please enter your weight", font = ("Arial",) ))
lblAskHeight = (Label ( tk, text = "Please enter your height", font = ("Arial",) ))
lblAskTime = (Label ( tk, text = "Please enter your time", font = ("Arial",) ))
entWeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor )
entHeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor )
entTime = Entry ( tk, font = ("Arial", 12), bg = formBgColor )


def openDataFrame():
    lblAsk.place_forget ()
    radYes.place_forget ()
    radNo.place_forget ()
    radElse.place_forget ()
    lblMarquee.place_forget ()
    btnStart.place_forget ()
    dataFrame.place ()  # Placed at the top center
    lblOne = Label ( dataFrame, text = "Lets collect some Data!!", font = ("Arial", 16),
                  bg = formBgColor, fg = formFgColor )
    lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )
    btnDataSubmit = Button ( dataFrame, text = "Submit", command = openDataFrame,
                             font = ("Arial", 11) )
    btnDataSubmit.place ( relx = 0.5, rely = 0.7, anchor = N )

def start():
    lblAsk.place ( relx = 0.5, rely = 0.5, anchor = CENTER )  # Placed at the top center
    radYes.place ( relx = 0.3, rely = 0.55, anchor = N )
    radNo.place ( relx = 0.4, rely = 0.55, anchor = N )
    radElse.place ( relx = 0.6, rely = 0.55, anchor = N )
    btnSubmit = Button ( tk, text = "Submit", command = openDataFrame, font = ("Arial", 11) )
    btnSubmit.place ( relx = 0.4, rely = 0.7 , anchor=N)


  #


btnStart = Button( tk, text = "Start", command = start, font = ("Arial", 11) )
btnStart.place ( relx = 0.5, rely = 0.28, anchor = N )  # Placed at the top center



tk.mainloop ()
