import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

data_path = "data.json"


# ---------------------------- Search Implementation ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(data_path) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Oops.. something went wrong, Please check the data file.")
    except:
        messagebox.showinfo(title="Error", message="Oops.. something went wrong, Please check the data file.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    password_entry.delete(0, END)

    password_letter = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = [website, email, password]
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    for item in data:
        if len(item) == 0:
            messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            try:

                with open(data_path, "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open(data_path, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open(data_path, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70, bg="#2A0944")

canvas = Canvas(width=200, height=200, bg="#2A0944", highlightthickness=0)
password_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", fg="#F78812", font=("Arial Black", 12, "bold"), bg="#2A0944")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Surname:", fg="#F78812", font=("Arial Black", 12, "bold"), bg="#2A0944")
email_label.grid(row=2, column=0, padx=5)

password_label = Label(text="Password:  ", fg="#F78812", font=("Arial Black", 12, "bold"), bg="#2A0944")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=28)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=3, padx=12)
email_entry.insert(0, "saba.konjaria@outlook.com")

password_entry = Entry(width=28)
password_entry.grid(row=3, column=1)

# Button
search_button = Button(width=14, text="Search", bg="#3FA796", fg="black",
                       command=find_password)
search_button.grid(row=1, column=2, columnspan=2)

generate_pasword_button = Button(width=14, text="Generate Password", bg="#3FA796", fg="black", command=generate)
generate_pasword_button.grid(row=3, column=2, columnspan=2)

add_button = Button(width=38, text="Add", command=save, bg="#3FA796", fg="black")
add_button.grid(row=4, column=1, columnspan=2, ipadx=0, ipady=0)

window.mainloop()
