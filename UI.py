import tkinter as tk
from tkinter import ttk
from captcha.image import ImageCaptcha
import random
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from database import *
# from machineLearning import *

#--------------------------UTILITY FUNCTIONS------------------------>>>>>>>>
#LOGIN FUNCTION
def loginBtn():
    username = username_entry.get()
    password = password_entry.get()

    if isUserPresent(username, password): #returns true or false 
        welcomeHeading.configure(text=f"Welcome {username}")

        login_frame.pack_forget() 
        home_frame.pack(expand=True, fill=tk.BOTH)      
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

#CAPTCHA GENERATING FUNCTION
def generateCaptcha():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"

    total = nums+lower+upper
    chars = "".join(random.sample(total, 6))

    capObj = ImageCaptcha(height=150, width=250)
    capObj.write(chars=chars, output="asset/captcha/cap.png")

    print(chars)
    return chars


#REGISTER BUTTON
def registerBtn():
    login_frame.pack_forget()
    register_frame.pack(expand=True, fill=tk.BOTH)

def signUpBtn():
    email = register_email_entry.get()
    username = register_username_entry.get()
    password = register_password_entry.get()
    captcha = cap_entry.get()

    if(captcha != chars):
        print("Incorrect Captcha Letters")
        register_error.configure(text = "Incorrect Captcha Letters!")
        return

    if(username == "" or password == "" or email == ""):
        print("Fill All the entries")
        register_error.configure(text = "Fill All the entries!")
        return 

    createAccount(username, password, email)

    welcomeHeading.configure(text=f"Welcome {username}")

    register_frame.pack_forget()
    home_frame.pack(expand=True, fill=tk.BOTH)    

#FORGOT PASSWORD FUNCTION
def forgotPasswordBtn():
    login_frame.pack_forget()
    forgot_frame.pack(expand=True, fill=tk.BOTH)

#VALIDATE CREDENTIALS IF PASSWORD FORGOTTEN
def validateBtn():
    email = forgot_email_entry.get()
    username = forgot_username_entry.get()

    if isCredentialsCorrect(username, email): #match the credentials
        forgot_frame.pack_forget()
        change_frame.pack(expand=True, fill=tk.BOTH)

    else:
        messagebox.showerror("Error", "Incorrect Credentials.")

#CHANGE PASSWORD
def changeBtn():
    username = forgot_username_entry.get()
    newPassword = change_password_entry.get()
    changePassword(username, newPassword)

    welcomeHeading.configure(text=f"Welcome {username}")
    change_frame.pack_forget()
    home_frame.pack(expand=True, fill=tk.BOTH)    

#PREDICT AND UPDATE THE OUTPUT TEXT
# def predictBtn():
#     response = predict()
#     outputHeading.configure(text=f"Tomorrow's temperature for Day{response[0]} is  {response[1]} \u00b0C", font=("Poppins", 40))

#DATASET-------------------------------------------------------->>>>>>>>>>
def showData():
    # str = "   Line     IP Address     Timestamp     Request Type     Status Code     User Agent\n\n"
    data = getData()
    # for record in data:
    #     str += f"{record[0]} \t {record[1]} \t {record[2]} \t {record[3]} \t {record[4]} \n"

    # outputHeading.configure(text=f"{data}", font=("Poppins", 10))

    # dataWindow = tk.Toplevel(root)
    # dataLabel=CTkLabel(master=dataWindow, width=1000, height=100, text=str, font=("Poppins", 15), text_color="black")
    # dataLabel.place(anchor="center", relx=0.5, rely=0.2)
    # dataLabel.pack()

    # print(data)

    window = tk.Tk()
    window.title('Structured Apache Access log')

    # Create a treeview for the table
    tree = ttk.Treeview(window, columns=['ID', 'IP Address', 'Timestamp', 'Request', 'Status Code', 'User Agent'], show='headings')

    # Define column headings
    for column in tree['columns']:
        tree.heading(column, text=column)

    # Insert data into the treeview
    for row in data:
        tree.insert('', 'end', values=row)

    # Add a vertical scrollbar to the treeview
    scrollbar = ttk.Scrollbar(window, orient='vertical', command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    # Pack the treeview and scrollbar
    tree.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    # Start the Tkinter event loop
    window.mainloop()

def addingData():
    res = addData(file_path.get())

# def updatingData():
#     res = updateData(day_entry.get(), temp_entry.get())
#     outputHeading.configure(text=f"{res}", font=("Poppins", 30))

# def deletingData():
#     res = deleteData(day_entry.get())
#     outputHeading.configure(text=f"{res}", font=("Poppins", 30))

#NAVIGATION------------------------------->>>>>>>>>>>>>
def registerToLogin():
    register_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def forgotToLogin():
    forgot_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def changeToLogin():
    change_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def homeToLogin():
    home_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

# ---------------------------------FRAMES--------------------------------->>>>>>>>>
# MAIN 
root = CTk()
set_default_color_theme("asset/themes/theme1.json")
root.geometry("1280x720")
root.title("Login Page")
root.iconbitmap("asset/favicon.ico")

# LOGIN
login_frame = CTkFrame(master=root)

close_button = CTkButton(master=login_frame, text="\u2715 Close", width=10, height=50, font=("Poppins", 25), corner_radius=25, command=exit)
close_button.place(rely = 0.355, relx=0.1, anchor="center")

heading=CTkLabel(master=login_frame, width=1000, height=100, text="Simple Log Analyzer", font=("Ravie", 72), text_color="Purple")
heading.place(anchor="center", relx=0.5, rely=0.1)

heading=CTkLabel(master=login_frame, width=1000, height=100, text="Please login with your credentials or register to make a new account", font=("Bodoni MT", 28), text_color="orange")
heading.place(anchor="center", relx=0.5, rely=0.25)

username_entry = CTkEntry(master=login_frame, width=400, height=50, font = ("Poppins", 25), placeholder_text="Username")
username_entry.place(rely = 0.5, relx=0.3,anchor="center")

password_entry = CTkEntry(master=login_frame, width=400, height=50, show="•", placeholder_text="Password", font = ("Poppins", 25))
password_entry.place(rely = 0.6, relx=0.3, anchor="center")

login_button = CTkButton(master=login_frame, text="Login", width=100, height=35, font=("Poppins", 22), command=loginBtn)
login_button.place(rely = 0.51, relx=0.7, anchor="center")

register_button = CTkButton(master=login_frame, text="Register", width=100, height=35, font=("Poppins", 22),command=registerBtn)
register_button.place(rely = 0.59, relx=0.7, anchor="center")

forgot_button = CTkButton(master=login_frame, text="Forgot Password?", width=150, height=35, font=("Poppins", 22), command=forgotPasswordBtn)
forgot_button.place(rely = 0.75, relx=0.5, anchor="center")


#REGISTER 
register_frame = CTkFrame(master=root)

back_to_login_button = CTkButton(master=register_frame, text="\u2190", width=10, height=35, corner_radius=100, command=registerToLogin)
back_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

registerHeading=CTkLabel(master=register_frame, width=1000, height=100, text="Register", font=("Ravie", 72), text_color="Purple")
registerHeading.place(anchor="center", relx=0.5, rely=0.1)

register_username_entry = CTkEntry(master=register_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Username")
register_username_entry.place(rely = 0.30, relx=0.3,anchor="center")

register_password_entry = CTkEntry(master=register_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Password")
register_password_entry.place(rely = 0.40, relx=0.3,anchor="center")

# register_mobile_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Mobile Number")
# register_mobile_entry.place(rely = 0.35, relx=0.5,anchor="center")

register_email_entry = CTkEntry(master=register_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Email")
register_email_entry.place(rely = 0.50, relx=0.3,anchor="center")

# captcha inside register---------------------------->>>
chars = generateCaptcha()
path = "asset/captcha/cap.png"
i = CTkImage(light_image=Image.open(path), size=(250,100))

cap=CTkLabel(master=register_frame, width=250, height=100, image=i, text="")
cap.place(anchor="center", relx = 0.7, rely = 0.35)

cap_entry = CTkEntry(master=register_frame, width=175, height=35, font=("Poppins", 18), placeholder_text="Captcha code")
cap_entry.place(rely = 0.475, relx=0.7,anchor="center")

signUp_button = CTkButton(master=register_frame, text="Sign Up", width=100, height=35, font=("Poppins", 22), command=signUpBtn)
signUp_button.place(rely = 0.65, relx=0.5, anchor="center")

register_error=CTkLabel(master=register_frame, width=1000, height=100, text="", font=("Poppins", 50), text_color="red")
register_error.place(anchor="center", rely=0.81, relx=0.5)


#FORGOT PASSWORD
forgot_frame = CTkFrame(master=root)

forgot_to_login_button = CTkButton(master=forgot_frame, text="\u2190", width=10, height=50, corner_radius=100, command=forgotToLogin)
forgot_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

registerHeading=CTkLabel(master=forgot_frame, width=1000, height=100, text="Enter Credentials", font=("Poppins", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

forgot_username_entry = CTkEntry(master=forgot_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Username")
forgot_username_entry.place(rely = 0.45, relx=0.3,anchor="center")

# forgot_mobile_entry = CTkEntry(master=forgot_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Mobile")
# forgot_mobile_entry.place(rely = 0.50, relx=0.3,anchor="center")

forgot_email_entry = CTkEntry(master=forgot_frame, width=300, height=35, font=("Poppins", 22), placeholder_text="Email")
forgot_email_entry.place(rely = 0.60, relx=0.3,anchor="center")

validate_button = CTkButton(master=forgot_frame, text="Validate", width=100, height=35, font=("Poppins", 22), command=validateBtn)
validate_button.place(rely = 0.525, relx=0.65, anchor="center")

#CHANGE PASSWORD
change_frame = CTkFrame(master=root)

change_to_login_button = CTkButton(master=change_frame, text="\u2190", width=10, height=50, corner_radius=100, command=changeToLogin)
change_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

changeHeading=CTkLabel(master=change_frame, width=1000, height=100, text="Set New Password", font=("Poppins", 72), text_color="white")
changeHeading.place(anchor="center", relx=0.5, rely=0.2)

change_password_entry = CTkEntry(master=change_frame, width=500, height=50, font=("Poppins", 22), placeholder_text="New Password")
change_password_entry.place(rely = 0.4, relx=0.5,anchor="center")

change_button = CTkButton(master=change_frame, text="Change", width=100, height=35, font=("Poppins", 22), command=changeBtn)
change_button.place(rely = 0.55, relx=0.5, anchor="center")

# HOME 
home_frame = CTkFrame(master=root)

home_to_login_button = CTkButton(master=home_frame, text="\u2190", width=10, height=50, corner_radius=100, command=homeToLogin)
home_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

welcomeHeading=CTkLabel(master=home_frame, width=800, height=90, text="Welcome", font=("Poppins", 72), text_color="white")
welcomeHeading.place(anchor="center", relx=0.5, rely=0.1)

file_path = CTkEntry(master=home_frame, width=500, height=50, placeholder_text="Enter the path of the Apache log file: ", font=("Poppins", 20))
file_path.place(rely = 0.3, relx=0.4,anchor="center")

add_button = CTkButton(master=home_frame, text="Parse and add", width=100, height=35, font=("Poppins", 22), command=addingData)
add_button.place(rely = 0.3, relx=0.75, anchor="center")

plot_button1 = CTkButton(master=home_frame, text="Requests per IP Address", command=plot_requests_by_ip, width=100, height=35, font=("Poppins", 22))
plot_button1.place(rely = 0.6, relx=0.3, anchor="center")

plot_button2 = CTkButton(master=home_frame, text="Requests over time", command=plot_requests_over_time, width=100, height=35, font=("Poppins", 22))
plot_button2.place(rely = 0.6, relx=0.7, anchor="center")

show_button = CTkButton(master=home_frame, text="Show LOGS", command=showData, width=100, height=35, font=("Poppins", 22))
show_button.place(rely = 0.45, relx=0.5, anchor="center")

#----------------------------INITIALIZING--------------------->>>>>>>>>>>>>
createTable()
createDataset()
login_frame.pack(expand=True, fill=tk.BOTH)
root.mainloop()
clearDataset()