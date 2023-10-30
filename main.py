import string
from tkinter import *
import os
from tkinter import Label, IntVar

tk = Tk ()
tk.title ( "Calorie Counter" )
tk.geometry ( "400x350" )
formBgColor = '#134ead'
formFgColor = '#eded1a'
btnColor = '#1aeb21'
radioGrpBg = '#204e99'
tk.configure ( background = formBgColor )

radioGrp: IntVar = IntVar ()
radioGrp.set ( 1 )
usrname = os.getlogin ()
username = string.capwords ( usrname )


def openDataFrame():
    global radioGrp
    hideForm ()
    dataFrame = Frame ( tk, width = '400', height = '400', bg = '#134ead')
    dataFrame.pack()
    lblOne: Label = (Label ( dataFrame, fg = formFgColor, bg = formBgColor,
                             font=("Arial", 12), text = f'Lets collect some data  {username}' ))
    lblOne.place( relx = 0.5, rely = 0.1, anchor = N )  # Placed at the top center)


my_menu = Menu ( tk )
tk.config ( menu = my_menu )
file_menu = Menu ( my_menu, tearoff = 0 )
my_menu.add_cascade ( label = "File", menu = file_menu )
file_menu.add_command ( label = "Data", command = openDataFrame )
file_menu.add_command ( label = "Exit", command = tk.quit )


def hideForm() -> object:
    lblAsk.place_forget ()
    radYes.place_forget ()
    radNo.place_forget ()
    radElse.place_forget ()
    lblMarquee.place_forget ()
    btnStart.place_forget ()
    return ''


# def getUser():
#     userid = int ( radioGrp.get () )
#     if userId == 1:
#         lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
#         txtUser = Entry ( tk, font = ("Arial", 12), bg = formBgColor, fg = formFgColor )
#         txtUser.place ( relx = 0.5, rely = 0.6, anchor = N )  # Placed at the top center


def radioChoice():
    global radioGrp
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


def start():
    lblAsk.place ( relx = 0.5, rely = 0.5, anchor = CENTER )  # Placed at the top center
    radYes.place ( relx = 0.3, rely = 0.55, anchor = N )
    radNo.place ( relx = 0.4, rely = 0.55, anchor = N )
    radElse.place ( relx = 0.6, rely = 0.55, anchor = N )


#


btnStart = Button ( tk, text = "Start", command = start, font = ("Arial", 11) )
btnStart.place ( relx = 0.5, rely = 0.28, anchor = N )  # Placed at the top center

tk.mainloop ()
