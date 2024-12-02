import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

#Create window and give it a title
window = tk.Tk()
window.title("Secure Password Generator")

#Some static variables
windowWidth = 490
windowHeight = 210
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
xCenter = int((screenWidth - windowWidth) / 2)
yCenter = int((screenHeight - windowHeight) / 2)

#Resize and position window
window.geometry(f'{windowWidth}x{windowHeight}+{xCenter}+{yCenter}')

#Make window !resizable
#window.resizable(False, False)

#Intro text
label = ttk.Label(
    window,
    text = "Select your settings",
    font = 24
)
label.grid(
    column = 0,
    columnspan = 4,
    row = 0
)

#Password length slider
scaleValue = tk.IntVar()
def getPassLength():
    return int(passLengthScale.get())
def passLengthChanged(event):
    passLengthLabel.configure(text = "Password length: {:>2}".format(getPassLength()))
passLengthLabel = ttk.Label(
    window,
    text = "Password length: "
)
passLengthLabel.grid(
    column = 0,
    row = 1
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
passLengthScale.set(12)
passLengthScale.grid(
    column = 1,
    columnspan = 2,
    row = 1,
    padx = 4
)

#Character selection
charSelectLabel = tk.Label(
    window,
    text = 'Selecet characters:'
)
charSelectLabel.grid(
    column = 0,
    row = 3,
    rowspan = 2,
    padx = 4,
    sticky = 'w'
)
includeLower = tk.IntVar(value = 1)
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
includeUpper = tk.IntVar(value = 1)
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
includeNumbers = tk.IntVar(value = 1)
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
includeSpecial = tk.IntVar(value = 1)
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

#Password listbox
passListBox = tk.Listbox(
    window,
    height = 1,
    width = 51,
    justify = 'center'
)
passListBox.grid(
    column = 0,
    columnspan = 5,
    row = 7,
    padx = 4
)

#Generate passwords button
lowercaseLettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseLettersList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbersList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialCharactersList = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']
def generatePass():
    if initString.get().count(' ') > 0 or initString.get().count('"') > 0 or initString.get().count('\'') > 0 or initString.get().count('`') > 0:
        messagebox.showerror("Error", "Initial text can't include spaces, \", ' or ` ")
        return
    if len(initString.get()) > getPassLength():
        messagebox.showerror("Error", "Initial text is longer than password length.")
        return
    finalCharactersList = []
    if includeLower.get() == 1:
        finalCharactersList.extend(lowercaseLettersList)
    if includeUpper.get() == 1:
        finalCharactersList.extend(uppercaseLettersList)
    if includeNumbers.get() == 1:
        finalCharactersList.extend(numbersList)
    if includeSpecial.get() == 1:
        finalCharactersList.extend(specialCharactersList)
    if len(finalCharactersList) == 0:
        messagebox.showerror("Error", "You have to select atleast one group of characters.")
        return
    password = initString.get()
    for i in range(getPassLength() - len(initString.get())):
        randomChar = random.choice(finalCharactersList)
        password += randomChar
    window.clipboard_clear()
    window.clipboard_append(password)
    passListBox.insert(0, password)
generatePassButton = ttk.Button(
    window,
    text = 'Generate password',
    command = generatePass
)
generatePassButton.grid(
    column = 0,
    columnspan = 5,
    row = 6,
    ipadx = 100,
    pady = 4
)

window.mainloop()