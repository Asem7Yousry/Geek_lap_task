##### develop the ui for the scraping tool using tkinter module #####
## needed modules ##
from tkinter import *  # for the ui of system
import webbrowser  # to show pages in browser by url 
from script_scrap import  scrap_method

### functions for interval time entry ###
def validate_integer(value):
    if value.isdigit():
        return True
    elif value == "":
        return True
    else:
        return False

def increment():
    current_value = int(entry_time.get())
    entry_time.delete(0, END)
    entry_time.insert(0, str(current_value + 10))

def decrement():
    current_value = int(entry_time.get())
    if current_value > 0:  # Ensure the value doesn't go below zero
        entry_time.delete(0, END)
        entry_time.insert(0, str(current_value - 10))


### intialize ui window dimintions and attributes ##
root = Tk()
root.title("Asem Market")
root.minsize(width=800,height=450) # dimintions
root.resizable(False,False) # dening scaling
root.config(bg="gray") # background color

# heading
title = Label(root,text="welcome to Scraping tool",fg="gold",bg="black",font=("tajawal",20,"bold"))
title.pack(fill=X)

# partition in the right side with background color darkblue 
partition1 = Frame(root,width=230,height=430,bg="darkblue")
partition1.place(x=570,y=35) 

### adding some labels in red partition ###
# label 1
label1 = Label(partition1,text="Asem Yousry Developer",font=("tajawal",14,"bold"),fg="gold",bg="darkblue")
label1.place(x= 2,y=10)
# label 2
label2 = Label(partition1,text="Contact Me:-",font=("tajawal",14,"bold"),fg="white",bg="darkblue")
label2.place(x= 62,y=50)

##### methods to show some information about me in browser #####
## method to represent my github account ##
def git_hub():
    webbrowser.open("https://github.com/Asem7Yousry")
    
## method to represent my LinkedIn account ##
def Linked_In():
    webbrowser.open("https://www.linkedin.com/in/asem-yousry-0621a3266/")

## method to represent my Wuzzuf account ##
def Wuzzuf():
    webbrowser.open("https://wuzzuf.net/profile")


### adding buttons in red partition to represent information about me ###
# button 1
button1 = Button(partition1,text="Git Hub",width=20,fg="white",bg="black",font=("tajawal",11,"bold"),command=git_hub)
button1.place(x=25,y=100)
# button 2 
button2 = Button(partition1,text="Linked In",width=20,fg="white",bg="black",font=("tajawal",11,"bold"),command=Linked_In)
button2.place(x=25,y=140)
# button 3
button3 = Button(partition1,text="Wuzzuf",width=20,fg="white",bg="black",font=("tajawal",11,"bold"),command=Wuzzuf)
button3.place(x=25,y=180)
# button 4
button4 = Button(partition1,text="Quit!",width=20,fg="white",bg="black",font=("tajawal",11,"bold"),command=quit)
button4.place(x=25,y=220)

### adding label and entry to user to scrap ##

## for time ## 
# label
Interval_time = Label(root,text="Interval time in sec",fg="red",bg="gray",font=("tajawal",14,"bold"))
Interval_time.place(x=380,y=350)
# entry
validate_cmd = root.register(validate_integer)
entry_time = Entry(root,width=20,font=("tajawal",12),justify="center" , validate="key", validatecommand=(validate_cmd, "%P"))
entry_time.place(x=380,y=380)
entry_time.insert(0, "0")

increment_button = Button(root, text="Increment", command=increment)
increment_button.place(x=380,y=405)

decrement_button = Button(root, text="Decrement", command=decrement)
decrement_button.place(x=450,y=405)
## for symbol ##
# label
symbol = Label(root,text="Symbol",fg="red",bg="gray",font=("tajawal",14,"bold"))
symbol.place(x=235,y=350)
# entry
entry_symbol = Entry(root,width=20,font=("tajawal",12),justify="center",)
entry_symbol.place(x=180,y=380)

## function to call scrap_method ##
def main_method():
    ### override on symbol and interval time ###
    symbol = entry_symbol.get()
    # timy = entry_time.get()
    time = int(entry_time.get())
    ## call method for scraping urls ##
    scrap_method(interval_time=time , symbol=symbol)

## button to scrap
button_scrap= Button(root,text="Srap",fg="black",bg="red",font=("tajawal",16,"bold"),height=2 ,command=main_method)
button_scrap.place(x=40,y=345)

# keep showing ui 
root.mainloop()

