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
    passLengthLabel.configure(text = "Password length: {:>2}".format(getValue()))
passLengthLabel = ttk.Label(
    window,
    text = "Password length: 1",
)
passLengthLabel.grid(
    column = 0,
    row = 1,
)
passLengthScale = ttk.Scale(
    window,
    from_ = 1,
    to = '50',
    length = 250,
    orient = 'horizontal',
    command = passLengthChanged,
    variable = scaleValue
)
passLengthScale.grid(
    column = 1,
    columnspan = 2,
    row = 1,
    padx = 4
)

#Character selection
charSelectLabel = tk.Label(
    window,
    text = 'Selecet characters:',
)
charSelectLabel.grid(
    column = 0,
    row = 3,
    rowspan = 2,
    padx = 4,
    sticky = 'w',
)
includeLower = tk.IntVar()
includeLowerCheck = ttk.Checkbutton(
    window,
    text = 'Lowercase(a-z)',
    variable = includeLower,
    onvalue = 1
)
includeLowerCheck.grid(
    column = 1,
    row = 3,
    sticky = 'w',
    padx = 4
)
includeUpper = tk.IntVar()
includeUpperCheck = ttk.Checkbutton(
    window,
    text = 'Uppercase(A-Z)',
    variable = includeUpper,
    onvalue = 1
)
includeUpperCheck.grid(
    column = 2,
    row = 3,
    sticky = 'w',
    padx = 4
)
includeNumbers = tk.IntVar()
includeNumbersCheck = ttk.Checkbutton(
    window,
    text = 'Numbers(0-9)',
    variable = includeNumbers,
    onvalue = 1
)
includeNumbersCheck.grid(
    column = 1,
    row = 4,
    sticky = 'w',
    padx = 4
)
includeSpecial = tk.IntVar()
includeSpecialCheck = ttk.Checkbutton(
    window,
    text = 'Special(!,@,#,...)',
    variable = includeSpecial,
    onvalue = 1
)
includeSpecialCheck.grid(
    column = 2,
    row = 4,
    sticky = 'w',
    padx = 4
)

#Initial string entry
initString = tk.StringVar()
initStringLabel = ttk.Label(
    window,
    text = 'Initial text:' 
)
initStringLabel.grid(
    column = 0,
    row = 5,
    padx = 4,
    sticky = 'w'
)
initStringEntry = ttk.Entry(
    window,
    width = 30,
    textvariable = initString
)
initStringEntry.grid(
    column = 1,
    columnspan = 2,
    row = 5,
    padx = 4,
    sticky = 'w'
)

window.mainloop()