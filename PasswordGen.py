from tkinter import *
import customtkinter
from random import randint 

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk() # create CTK Window

width = 380
height = 260
app.geometry("380x260")
app.title("Drey's Password Generator")
app.maxsize(width*1.5, height*1.5)
app.minsize(width-20,height-10)
my_password = chr(randint(33,126))

# Generate Random Password
def new_rand():
    # Clear Our Entry Box
    Password_Entry.delete(0, END) 

    # GetPW Length and convert to integer
    pw_length = int(my_entry.get())

    # Create a variable to hold our password
    my_password = ''

    #Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    # Output Password to the screen
    Password_Entry.insert(0, my_password)

def clipper():
    # Clear the clipboard
    app.clipboard_clear()
    # Copy to clipboard
    app.clipboard_append(Password_Entry.get())

# Label Frame
LabelFrame = customtkinter.CTkLabel(master=app, text= "How long is your password?", font=("Helvetica", 18))
LabelFrame.pack(pady=10)

# Create Entry box to designate number of characters
my_entry = customtkinter.CTkEntry(master=LabelFrame, font=("Helvetica", 24),placeholder_text="Ex: 20",width=width)
my_entry.grid(pady=10)

# Create EntryBox for our returned password
Password_Entry = customtkinter.CTkEntry(master=LabelFrame, font=("Helvetica", 24),fg_color="transparent", border_width=0,width=width)
Password_Entry.grid(row=2,pady=10)

ButtonFrame = customtkinter.CTkFrame(master=app)
ButtonFrame.pack(pady=10)

# Create our buttons 
my_button = customtkinter.CTkButton(master=ButtonFrame,text="Generate Password",command=new_rand)
my_button.grid(row=3,column=0,padx=5,)

clip_button = customtkinter.CTkButton(master=ButtonFrame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=3,column=1,padx=5,)

# FeedBack Text
FeedBack = customtkinter.CTkLabel(master=app, text= "Create Secure Passwords!! [V.1 2023]", font=("Helvetica", 14))
FeedBack.pack(pady=10)

app.mainloop()