#Impoting neccessary libraries and modules
import tkinter
from tkinter import *
import random
import array


############################
""" Tkinter Initializing """
############################


#Creating window and giving it a title and size
window = tkinter.Tk()
window.title("Random Password Generator")
window.geometry("800x400")
window.resizable(False, False)


#################################
""" Random Password Generator """
#################################


#Generating random password
def randPass():
    #Clearing entry box each time to generate random password button is pressed
    passEntry.delete(0, END)
    """ Password Generator """

    #Initializing password variable
    password = ""

    passLength = int(characterEntry.get())

    if passLength < 12:
        passEntry.insert(0, "Length is not long enough")

    elif passLength > 100:
        passEntry.insert(0, "Length is too large")

    else:
        passLength = passLength

        #Creating four arrays for the password generaot to pull characters from
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        alphabetLower = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
            'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
        ]

        alphabetUpper = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
            'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'
        ]

        specialCharacter = [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
            '+', '[', ']', '{', '}', ';', ':', ',', '<', '>', '.', '/', '?'
        ]

        #Combining the three above arrays into one array to pull characters from
        sumCharacters = digits + alphabetLower + alphabetUpper + specialCharacter

        #Using the random module to get the random characters from the array
        tempPass = random.sample(sumCharacters, passLength)

        #Shuffling the tempPass list and joining the characters together with the initialized password from above
        random.shuffle(tempPass)
        password = password.join(tempPass)

        #Printing the random generated password
        print(password)

        #Inserting random password into entry box
        passEntry.insert(0, password)


#Copying the random password to clipboard
def clip():
    #Clearing anything currently in clipboard
    window.clipboard_clear()

    #Copying random generated password to clipboard
    window.clipboard_append(passEntry.get())


#####################################
""" Random Password Generator GUI """
#####################################


#Creating label frame and entry box for dessignated password length
labelFrame = LabelFrame(window, text="What is your password's desired length?")
labelFrame.pack(pady=20)
characterEntry = Entry(labelFrame, font=("Calibri", 24))
characterEntry.pack(pady=20, padx=20)

#Creating an label for the genreated random password
passEntry = Entry(window, font=("Calibri", 24))  #passEntry
passEntry.pack(pady=20)  #passEntry

#Creating a frame and buttons
buttonFrame = Frame(window)
buttonFrame.pack(pady=20)
generatePassButton = Button(buttonFrame,
                            text="Generate Random Password",
                            command=randPass)
generatePassButton.grid(row=0, column=0, padx=10)
clipboardButton = Button(buttonFrame,
                         text="Copy Password to Clipboard",
                         command=clip)
clipboardButton.grid(row=0, column=1, padx=10)

window.mainloop()
