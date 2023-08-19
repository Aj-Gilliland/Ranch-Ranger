import tkinter
from tkinter import messagebox
from typing import List
import json
from dataclasses import dataclass
from PIL import Image, ImageTk, ImageDraw, ImageOps

window = tkinter.Tk()
window.title("Ranch Ranger v4")
window.configure(bg="#333333")
window.state("zoomed")

root_frame = tkinter.Frame(bg="#333333")
root_frame.pack()

# @dataclass
# class User:
#    username: str
#    password: str

# user = User('','')

global_username = ""
global_password = ""

#       To Do
# Make each user only be able to see their own data
# Add photos
# finshing touches :)))))))
# (*wip*)


################################################
#!!!
def save_animal_data(data):
    with open(f"{global_username}_data.json", "w") as file:
        json.dump(data, file)


################################################
#!!!
def load_animal_data():
    try:
        with open(f"{global_username}_data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"{global_username}'s file is not found")
        return {}


# return an empty dictionary if the file doesn't exist

################################################


def remove_animal(animal_type):
    animal_data = load_animal_data()
    if animal_type in animal_data:
        del animal_data[animal_type]
    save_animal_data(animal_data)


################################################


def add_animal(name, quantity, food_per_day, food_rate):
    animal_data = load_animal_data()
    animal_data[name] = {
        "quantity": quantity,
        "food_per_day": food_per_day,
        "rate": food_rate,
    }
    save_animal_data(animal_data)


################################################


# creates the main menu for the animal managment side of the software
def animal_menu():
    for widget in root_frame.winfo_children():
        widget.destroy()

    # title label
    animal_label = tkinter.Label(
        root_frame, text="Animals", bg="#333333", fg="#F5DEB3", font=("Arial", 30)
    )
    animal_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    # add animal button
    add_animal_button = tkinter.Button(
        root_frame,
        text="Add Animal",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 10),
        command=lambda: add_animal(
            animal_type_entry.get(),
            quantity_entry.get(),
            food_per_day_entry.get(),
            food_rate_entry.get(),
        ),
    )
    add_animal_button.grid(row=1, column=0, pady=20, sticky="e")

    # remove animal button
    remove_animal_button = tkinter.Button(
        root_frame,
        text="Remove Animal",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 10),
        command=lambda: remove_animal(animal_type_entry.get()),
    )
    remove_animal_button.grid(row=1, column=1, pady=20, sticky="w")

    # add animal entry fields
    animal_type_label = tkinter.Label(
        root_frame, text="Animal Name?", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    animal_type_label.grid(row=2, column=0, pady=10, sticky="e")
    animal_type_entry = tkinter.Entry(root_frame, font=("Arial", 16))
    animal_type_entry.grid(row=2, column=1, pady=10, sticky="w")

    quantity_label = tkinter.Label(
        root_frame,
        text="How many animals you got?",
        bg="#333333",
        fg="#FFFFFF",
        font=("Arial", 16),
    )
    quantity_label.grid(row=3, column=0, pady=10, sticky="e")
    quantity_entry = tkinter.Entry(root_frame, font=("Arial", 16))
    quantity_entry.grid(row=3, column=1, pady=10, sticky="w")

    food_per_day_label = tkinter.Label(
        root_frame,
        text="Food per day?(lbs)",
        bg="#333333",
        fg="#FFFFFF",
        font=("Arial", 16),
    )
    food_per_day_label.grid(row=4, column=0, pady=10, sticky="e")
    food_per_day_entry = tkinter.Entry(root_frame, font=("Arial", 16))
    food_per_day_entry.grid(row=4, column=1, pady=10, sticky="w")

    food_rate_label = tkinter.Label(
        root_frame, text="Price per lbs", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    food_rate_label.grid(row=5, column=0, pady=10, sticky="e")
    food_rate_entry = tkinter.Entry(root_frame, font=("Arial", 16))
    food_rate_entry.grid(row=5, column=1, pady=10, sticky="w")

    # empty row to create space
    tkinter.Label(
        root_frame, text="", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    ).grid(row=6, column=0, pady=10)

    # listbox to display animals and their stats
    animal_list_label = tkinter.Label(
        root_frame, text="Animal Stats", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    animal_list_label.grid(row=7, column=0, columnspan=2, pady=10, sticky="s")
    animal_listbox = tkinter.Listbox(
        root_frame, font=("Arial", 12), width=40, height=10, selectbackground="grey"
    )
    animal_listbox.grid(row=8, column=0, columnspan=2, pady=20)
    animal_listbox.insert(1, "Animal   Number of Animals    lbs per Month")
    x = 2
    animals = load_animal_data()
    for animal in animals:
        animal_listbox.insert(
            x,
            f'{animal.title()}                        {animals[animal]["quantity"]}                    {animals[animal]["food_per_day"]}/lbs per day',
        )
        x += 1

    # back button
    back_button = tkinter.Button(
        root_frame,
        text="Back",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 10),
        command=lambda: main_menu(),
    )
    back_button.grid(row=9, column=0, columnspan=2, pady=20, sticky="s")


################################################


# creates the main menu for the budgeting side of the software
def budget_menu():
    for widget in root_frame.winfo_children():
        widget.destroy()
    expenses_label = tkinter.Label(
        root_frame, text="Expenses", bg="#333333", fg="#F5DEB3", font=("Arial", 30)
    )
    expenses_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

    # label showing total monthly cost
    animals = load_animal_data()
    monthly_total = 0
    for animal in animals:
        total_per_animal = (
            float(animals[animal]["quantity"])
            * float(animals[animal]["food_per_day"])
            * float(animals[animal]["rate"])
        )
        monthly_total += total_per_animal
    monthly_total_label = tkinter.Label(
        root_frame,
        text=f"Your typicall monthly cost will be ${monthly_total}",
        bg="#333333",
        fg="#F5DEB3",
        font=("Arial", 15),
    )
    monthly_total_label.grid(row=1, column=0, columnspan=1, sticky="news", pady=20)
    # label showing yearly cost with a 20% discount (average discount on yearly bought feed for farmers)
    yearly_total = monthly_total * 12 * 0.8
    yearly_total_label = tkinter.Label(
        root_frame,
        text=f"If you buy a years supply you will average ${yearly_total} every year.",
        bg="#333333",
        fg="#F5DEB3",
        font=("Arial", 15),
    )
    yearly_total_label.grid(row=2, column=0, columnspan=1, sticky="news", pady=20)

    # listbox showing indivigual cost (wip)
    animal_list_label = tkinter.Label(
        root_frame, text="Animal Rates", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    animal_list_label.grid(row=7, column=0, columnspan=2, pady=10, sticky="s")
    animal_listbox = tkinter.Listbox(
        root_frame, font=("Arial", 12), width=40, height=10, selectbackground="grey"
    )
    animal_listbox.grid(row=8, column=0, columnspan=2, pady=20)
    animal_listbox.insert(1, "Animal                             Rate")
    x = 2
    animals = load_animal_data()
    for animal in animals:
        animal_listbox.insert(
            x,
            f'{animal.title()}                        ${animals[animal]["rate"]}/per pound',
        )
        x += 1

    # back button
    logout_button = tkinter.Button(
        root_frame,
        text="Back",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 10),
        command=lambda: main_menu(),
    )
    logout_button.grid(row=9, column=0, columnspan=1, pady=20)


################################################


# creates main menu
def main_menu():
    for widget in root_frame.winfo_children():
        widget.destroy()
    # welcome message label
    welcome_label = tkinter.Label(
        root_frame,
        text=f"Welcome to the Ranch Ranger",
        bg="#333333",
        fg="#F5DEB3",
        font=("Arial", 30),
    )
    welcome_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    # animal view button
    View_button = tkinter.Button(
        root_frame,
        text="View Animals",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 16),
        command=lambda: animal_menu(),
    )
    View_button.grid(row=1, column=0, columnspan=3, pady=30, sticky="e")
    # budget view button
    budget_button = tkinter.Button(
        root_frame,
        text="View Monthly Expenses",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 16),
        command=lambda: budget_menu(),
    )
    budget_button.grid(row=1, column=0, columnspan=3, pady=30, sticky="w")
    # log out button
    logout_button = tkinter.Button(
        root_frame,
        text="Log Out",
        bg="green",
        fg="#FFFFFF",
        font=("Arial", 10),
        command=lambda: login_ui(),
    )
    logout_button.grid(row=8, column=0, columnspan=2, pady=20)
    # display main menu image
    image = Image.open(
        "C:/Users/fastc/OneDrive/Desktop/VS code/Ranch Ranger/pictures/moms farm.png"
    )
    image = image.resize((400, 400), resample=Image.BICUBIC)
    img = ImageTk.PhotoImage(image)

    # create a label to display the image
    img_label = tkinter.Label(root_frame, image=img, bg="#333333")
    img_label.image = img
    img_label.grid(row=6, column=0, columnspan=2, pady=20)


################################################


# loads all the users from the users file to get all the usr&pwd
def load_users() -> List:
    with open("accounts.txt", "r") as object_file:
        accounts = object_file.readlines()
        return accounts


################################################
#!!!
# append to accounts file
def add_account(username, password):
    if username != "" and password != "":
        with open("accounts.txt", "a") as object_file:
            object_file.write(f"\n{username}   {password}")
        with open(f"{username}_data.json", "a") as object_file:
            object_file.write("{}")


################################################
#!!!
# creates login page logic for application
def login(accounts, username, password):
    global global_username, global_password
    for account in accounts:
        stored_username, stored_password = account.strip().split()
        if username == stored_username and password == stored_password:
            global_username = username.strip()
            global_password = password.strip()
            main_menu()
            return
    error_label = tkinter.Label(
        root_frame,
        text="Username or Password Incorrect",
        bg="#333333",
        fg="red",
        font=("Arial", 8),
    )
    error_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)


################################################


# login menu
def login_ui():
    for widget in root_frame.winfo_children():
        widget.destroy()
    # creating widgets
    create_account_label = tkinter.Label(
        root_frame,
        text="Create Account",
        bg="#333333",
        fg="#FF3399",
        font=("Arial", 30),
    )
    login_label = tkinter.Label(
        root_frame, text="Login", bg="#333333", fg="#F5DEB3", font=("Arial", 30)
    )
    username_label = tkinter.Label(
        root_frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    username_entry = tkinter.Entry(root_frame, font=("Arial", 16))
    password_entry = tkinter.Entry(root_frame, show="*", font=("Arial", 16))
    password_label = tkinter.Label(
        root_frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16)
    )
    login_button = tkinter.Button(
        root_frame,
        text="Login",
        bg="#F5DEB3",
        fg="#FFFFFF",
        font=("Arial", 16),
        command=lambda: login(load_users(), username_entry.get(), password_entry.get()),
    )
    create_account_button = tkinter.Button(
        root_frame,
        text="Create Account",
        bg="#F5DEB3",
        fg="#FFFFFF",
        font=("Arial", 16),
        command=lambda: add_account(username_entry.get(), password_entry.get()),
    )
    # placing widgets on the screen
    create_account_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=2, column=0)
    username_entry.grid(row=2, column=1, pady=20)
    password_label.grid(row=3, column=0)
    password_entry.grid(row=3, column=1, pady=20)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)
    create_account_button.grid(row=5, column=0, columnspan=2, pady=30)

    # load and display alpaca mascot
    image = Image.open(
        "C:/Users/fastc/OneDrive/Desktop/VS code/Ranch Ranger/pictures/alpaca.png"
    )
    image = image.resize((100, 100), resample=Image.NEAREST)
    img = ImageTk.PhotoImage(image)

    # create a label to display the image
    img_label = tkinter.Label(root_frame, image=img, bg="#333333")
    img_label.image = img
    img_label.grid(row=1, column=0, columnspan=2, pady=1)


################################################

if __name__ == "__main__":
    login_ui()

window.mainloop()
