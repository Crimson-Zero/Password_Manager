from tkinter import *   #import the classes not modules
from tkinter import messagebox
LOGO_IMG = "C:/Users/wajee/.spyder-py3/password-manager-start/logo.png"
import random
import json

#For writing 
#json.dump()

#For Reading
#json.load()

#for updating
#json.update()    
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

# ---------------------------- Search Password ------------------------------- #

def search_password():
    
    website= website_Entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        
        messagebox.showerror(title="Error",message="No file found")
    
    else:
        
        with open("data.json") as data_file:
            data=json.load(data_file)
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                
                messagebox.showinfo(title=website,message=f"Email:{email}\n Password : {password}")
            else:
                messagebox.showerror(title="Details doesnot exist",message="No Data found in the file ")
            
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_data():
    
    website_name = website_Entry.get()
    email = Email_Entry.get()
    password = password_Entry.get()
    new_data = {
                 website_name:{
                "email":email,
                "password":password
                }
                }
    
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok=messagebox.askokcancel(title=website_name , message=f"These are the details entered: \n Website : {website_name} \n  Email: {email} \n Password : {password}"
                              f"\n Is this ok to save? ")
    if is_ok:
        
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        
        else:
            data.update(new_data)
        
        finally:
            website_Entry.delete(0,END)
            password_Entry.delete(0,END)
            website_Entry.focus()
            
       # with open("JSON_data.json",mode="w") as data_file:#change mode to w to write this will delete it a for append
        #    json.dump(new_data,data_file, indent=4) #number of spaces for JSON data readibility
            
            #to read the data
        #with open("JSON_data.json",mode="r") as data_file:
            #json.load(data_file)
        
        #for update JSON
        #with open("JSON_data.json",mode="w") as data_file:
            #data=json.load(data_file)  read old data
            
            #update old data
            #json.update(new_data)
        #with open("JSON_data.json",mode="w") as data_file:
            
            #saving new_data
            #json.dump(data,data_file,indent=4)
    
   
    
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
Email_Entry.grid(row=2,column=1)

#populating a static value

Email_Entry.insert(0,"test@gmail.com")  #insert at the begining first character END to add after the text

password_Entry = Entry(width =52)
password_Entry.grid(row=3,column=1,columnspan = 2)

#generate password
search_button = Button(text="Search",command=search_password)
search_button.grid(row=1 ,column=2)
generate_password_button = Button(text="Generate password" , command=generate_password)
generate_password_button.grid(row=3,column=2)


#Add Button

Add_Button = Button(text = "Add",width=44 , command=get_data)
Add_Button.grid(row=4,column=1,columnspan=2)



window.mainloop()
