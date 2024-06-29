import tkinter as tk
from tkinter import ttk

#Create window and give it a title
window = tk.Tk()
window.title("Secure Password Generator")

#Some static variables
windowWidth = 500
windowHeight = 500
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
xCenter = int((screenWidth - windowWidth) / 2)
yCenter = int((screenHeight - windowHeight) / 2)

#Resize and position window
window.geometry(f'{windowWidth}x{windowHeight}+{xCenter}+{yCenter}')

#Make window !resizable
window.resizable(False, False)

#Intro text
label = ttk.Label(
    window,
    text = "Select your settings"
)
label.grid(
    column = 0,
    columnspan = 3,
    row = 0
)

#Password length slider
scaleValue = tk.IntVar()
def getValue():
    return int(passLengthScale.get())
def passLengthChanged(event):
    passLegthValue.configure(text = getValue())
passLengthLabel = ttk.Label(
    window,
    text = "Password length:",
)
passLengthLabel.grid(
    column = 0,
    row = 1,
    ipadx = 2
)
passLengthScale = ttk.Scale(
    window,
    from_ = 1,
    to = 50,
    orient = 'horizontal',
    command = passLengthChanged,
    variable = scaleValue
)
passLengthScale.grid(
    column = 2,
    row = 1
)
passLegthValue = ttk.Label(
    window,
    text = getValue()
)
passLegthValue.grid(
    column = 1,
    row = 1,
    ipadx = 3
)

window.mainloop()