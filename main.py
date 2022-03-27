from tkinter import *   #import the classes not modules
from tkinter import messagebox
LOGO_IMG = "Absolute or relative path of the image file" 
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = random.randint(0, 51)
    nr_numbers = random.randint(0, 9)
    nr_symbols = random.randint(0, 8)
    
    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)
    
    get_letters=letters[0:nr_letters]
    get_numbers=numbers[0:nr_numbers]
    get_symbols=symbols[0:nr_symbols]
    


    password= get_letters + get_numbers + get_symbols 
    random.shuffle(password)
    final_password="".join(password)
    
    password_Entry.insert(0,final_password)

    
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_data():
    
    website_name = website_Entry.get()
    email = Email_Entry.get()
    password = password_Entry.get()
    
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title=website_name , message=f"These are the details entered: \n Website : {website_name} \n  Email: {email} \n Password : {password}"
                              f"\n Is this ok to save? ")
    if is_ok:  
        with open("passfile.txt",mode="a") as file:#change mode to w to write this will delete it a for append
            file.write(f"Website Name: {website_name} | Email: {email} | password: {password} \n")
    
    website_Entry.delete(0,END)
    password_Entry.delete(0,END)
    website_Entry.focus()
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx = 20 , pady=20) #to add padding between item and the screen

canvas = Canvas(height=200 , width=200)
logo_img = PhotoImage(file=LOGO_IMG)
canvas.create_image(100,100,image=logo_img) #canvas create image need position and image
canvas.grid(row=0,column=1)

#Labels text based representation of what is being shown

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label= Label(text="Email/username:")  #The label tag for the labels
email_label = email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries the entry is the form input in  Tkinter

website_Entry = Entry(width = 52)
website_Entry.grid(row=1,column=1,columnspan = 2)

#to focus cursoe on entry

website_Entry.focus()

Email_Entry = Entry(width = 52)
Email_Entry.grid(row=2,column=1,columnspan = 2)

#populating a static value

Email_Entry.insert(0,"test@hotmail.com")  #insert at the begining first character END to add after the text

password_Entry = Entry(width =52)
password_Entry.grid(row=3,column=1,columnspan = 2)

#generate password

generate_password_button = Button(text="Generate password" , command=generate_password)
generate_password_button.grid(row=3,column=2)


#Add Button

Add_Button = Button(text = "Add",width=44 , command=get_data)
Add_Button.grid(row=4,column=1,columnspan=2)



window.mainloop()
