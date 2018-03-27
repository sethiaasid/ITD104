#----------------------------------------------------------------
#
# COUNTDOWN
#
# In this exercise you must create a Graphical User
# Interface using tkinter.  The program should create
# a window containing a label and a button.  The label
# displays a number and each time the button is pressed
# the number in the label should decrease by 1 until
# it reaches zero, at which some other value can be
# displayed.  This will give you practice at both
# creating widgets and getting them to interact.
#

# Import the necessary tkinter functions
from tkinter import Tk, Button, Label

# Create a window
countdown_window = Tk()

# Give the window a title
countdown_window.title('Countdown')


##### PUT YOUR CODE HERE

# 1. Define a function to be called when the button is
#    pressed which will change the label's value
count = 10

def isPressed():
    global count
    count -= 1
    if count != 0:
        label['text'] =  count
    else:
        label['font'] = font = ('Arial', 26)
        label['text'] =  'GO!'
    

# 2. Define the Button widget and pack it into the
#    main window
push_button = Button(countdown_window, text = 'push', font = ('Arial', 16), command = isPressed)
push_button.pack()

# 3. Define the Label widget and pack it into the main
#    window
label = Label(countdown_window, text = '10', font = ('Arial', 16))
label.pack()


# Start the event loop to react to user inputs
countdown_window.mainloop()
