import string
from tkinter import *
import os

tk = Tk ()
tk.title ( "Calorie Counter" )
tk.geometry ( "400x300" )
formBgColor = '#134ead'
formFgColor = '#eded1a'
btnColor = '#b2b865'
radioGrpBg = '#204e99'
tk.configure ( background = formBgColor )

radioGrp = IntVar ()
radioGrp.set ( 1 )
usrname = os.getlogin ()
username = string.capwords ( usrname )


def getUser(userId):
    wht = 0
    hgt = 0.0
    time = 0.0
    if userId == 1:
       lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
       txtUser = Entry ( tk, font = ("Arial", 12), bg = formBgColor, fg = formFgColor )
       txtUser.place ( relx = 0.5, rely = 0.6, anchor = N )  # Placed at the top center

def radioChoice():
    btnStart.destroy ()
    lblMarquee.destroy ()

    if radioGrp.get () == 1:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
    elif radioGrp.get () == 2:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
    else:
        lblOne.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center

    btnSubmit.place ( relx = 0.5, rely = 0.6, anchor = N )  # Placed at the top center


# This is the greeting Label
lblMarquee = Label ( tk, text = f"Welcome to the Calorie Counter {username}",
                     bg = formBgColor, fg = formFgColor, font = ("Arial", 16) )
lblMarquee.place ( relx = 0.5, rely = 0.1, anchor = N )  # Placed at the top center

radYes = Radiobutton ( tk, text = 'Yes', bg = radioGrpBg, variable = radioGrp, value = 1 )
radNo = Radiobutton ( tk, text = 'No', bg = radioGrpBg, variable = radioGrp, value = 2 )
radElse = Radiobutton ( tk, text = 'Someone else', bg = radioGrpBg, variable = radioGrp, value = 3 )
lblOne = Label ( tk, text = 'Yes', bg = formBgColor, fg = formFgColor, font = ("Mono", 11) )
btnSubmit = Button ( tk, text = 'Submit', command = getUser, font = ("Mono", 11), width = 6, height = 1 )
lblAskWeight = (Label ( tk, text = 'Please enter your weight', font = ("Arial",)))
lblAskHeight = (Label ( tk, text = 'Please enter your height', font = ("Arial",)))
lblAskTime = (Label ( tk, text = 'Please enter your time', font = ("Arial",)))
entWeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor)
entHeight = Entry ( tk, font = ("Arial", 12), bg = formBgColor)
entTime = Entry ( tk, font = ("Arial", 12), bg = formBgColor)


def start():
    lblAsk = Label ( tk, text = 'Would you like to start a log session?', font = ("Arial", 12), bg = formBgColor,
                     fg = formFgColor )
    lblAsk.place ( relx = 0.5, rely = 0.5, anchor = N )  # Placed at the top center
    radYes.place ( relx = 0.3, rely = 0.6, anchor = N )
    radNo.place ( relx = 0.5, rely = 0.6, anchor = N )
    radElse.place ( relx = 0.8, rely = 0.6, anchor = N )
    btnSubmit.place ( relx = 0.5, rely = 0.7, anchor = N )  # Placed at the top center
    lblWeight = (Label ( tk, text = 'Please enter your weight', font = ("Arial", 12),
                         bg = formBgColor, fg = formFgColor ))
    lbHWeight = (Label ( tk, text = 'Please enter your height', font = ("Arial", 12),
                         bg = formBgColor, fg = formFgColor ))
    lblTime = (Label ( tk, text = 'Please enter Time', font = ("Arial", 12),
                       bg = formBgColor, fg = formFgColor ))





btnStart = Button ( tk, text = 'Start', command = start, font = ("Arial", 12), width = 5, height = 1 )
btnStart.place ( relx = 0.5, rely = 0.3, anchor = N )  # Placed at the top center

tk.mainloop ()
