import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from PIL import Image, ImageTk
import os

def home():
    window.destroy()
    filename = "homepage.py"
    os.system("python " + filename)
def rent():
    window.destroy()
    filename = "cost.py"
    os.system("python " + filename)
def showcars():
    window.destroy()
    filename = "showcars.py"
    os.system("python " + filename)
def returncar():
    window.destroy()
    filename = "returnn.py"
    os.system("python " + filename)
def updatecar():
    window.destroy()
    filename = "update.py"
    os.system("python " + filename)
def showrecord():
    window.destroy()
    filename = "showrecords.py"
    os.system("python " + filename)
def show_all_records():
    conn = sqlite3.connect('customer_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    records = c.fetchall()
    conn.close()
    
    if records:
        records_window = tk.Toplevel(window)
        records_window.title("All Records")
        records_window.geometry("600x400")
        records_frame = tk.Frame(records_window)
        records_frame.pack(expand=True, fill="both")
        for record in records:
            fields = ["Name", "Surname", "Address", "Car Type", "Car Transmission", "Car Model"]
            record_text = "\n".join([f"{field}: {value}" for field, value in zip(fields, record)])
            record_label = tk.Label(records_frame, text=record_text, font=("Helvetica", 12))
            record_label.pack(padx=20, pady=10, anchor="w")
    else:
        messagebox.showinfo("No Record", "No transaction records found.")

def exit():
    window.destroy()


def delete_record():
    name = return_first.get()
    surname = return_surname.get()
    # Add your logic here to delete the record
    return_vehicle_popup(name, surname)

def return_vehicle_popup(name, surname):
    def confirm_return():
        nonlocal name, surname
        conn = sqlite3.connect('customer_database.db')
        c = conn.cursor()
        
        # Delete the record from the database
        c.execute("DELETE FROM customers WHERE name=? AND surname=?", (name, surname))
        conn.commit()
        
        messagebox.showinfo("Success", "The vehicle has been returned successfully.")
        window.destroy()  # Close the popup window
        
        # Close connection
        conn.close()

    def cancel_return():
        window.destroy()  # Close the popup window

    conn = sqlite3.connect('customer_database.db')
    c = conn.cursor()

    # Check if the customer exists in the database
    c.execute("SELECT * FROM customers WHERE name=? AND surname=?", (name, surname))
    customer_data = c.fetchone()

    if customer_data:
        window = tk.Toplevel()
        window.title("Return Vehicle")
        window.geometry("300x150")
        
        label = tk.Label(window, text=f"Do you want to return the vehicle for {name} {surname}?", font=("Poppins", 12))
        label.pack(pady=10)
        
        confirm_button = tk.Button(window, text="Confirm", command=confirm_return, bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
        confirm_button.pack(side="left", padx=10)
        
        cancel_button = tk.Button(window, text="Cancel", command=cancel_return, bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
        cancel_button.pack(side="right", padx=10)
        
        window.mainloop()
    else:
        messagebox.showerror("Error", "No customer name found! Please recheck the name.")

    # Close connection
    conn.close()


window = tk.Tk()
window.title("Customer Details")
window.geometry('1920x1080')
window.configure(bg="#C3242A")

background_image = Image.open("Giansports.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#C3242A")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Frame for the navbar
navbar_frame = tk.Frame(window, bg="#C3242A")
navbar_frame.place(relx=0.5, rely=0.15, anchor="n")

# Create labels for Home, Rent A Car, Show Cars, and Exit
home_lb = tk.Label(navbar_frame, text="Home", bg="#C3242A", fg="white", font=("Poppins", 16))
rent_lb = tk.Label(navbar_frame, text="Rent A Car", bg="#C3242A", fg="white", font=("Poppins", 16))
showcars_lb = tk.Label(navbar_frame, text="Show Cars", bg="#C3242A", fg="white", font=("Poppins", 16))
return_lb = tk.Label(navbar_frame, text="Return a Car", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
updatecar_lb = tk.Label(navbar_frame, text="Update", bg="#C3242A", fg="white", font=("Poppins", 16))
showrecord_lb = tk.Label(navbar_frame, text="Show Reciept", bg="#C3242A", fg="white", font=("Poppins", 16))
showallrecords_lb = tk.Label(navbar_frame, text="Show All Reciept", bg="#C3242A", fg="white", font=("Poppins", 16))
ex_lb = tk.Label(navbar_frame, text="Exit", bg="#C3242A", fg="white", font=("Poppins", 16))

# Pack labels parallel to each other
home_lb.pack(side="left", padx=10)
rent_lb.pack(side="left", padx=10)
showcars_lb.pack(side="left", padx=10)
return_lb.pack(side="left", padx=10)
updatecar_lb.pack(side="left", padx=10)
showrecord_lb.pack(side="left", padx=10)
showallrecords_lb.pack(side="left", padx=10)
ex_lb.pack(side="left", padx=10)

# Bind functionality to labels
home_lb.bind("<Button-1>", lambda event: home())
rent_lb.bind("<Button-1>", lambda event: rent())
showcars_lb.bind("<Button-1>", lambda event: showcars())
return_lb.bind("<Button-1>", lambda event: returncar())
updatecar_lb.bind("<Button-1>", lambda event: updatecar())
showrecord_lb.bind("<Button-1>", lambda event: showrecord())
ex_lb.bind("<Button-1>", lambda event: exit())

# Frame for the customer details form
frame = tk.Frame(window, bg="#C3242A")
frame.place(relx=0.5, rely=0.5, anchor="center")

username_lb2 = tk.Label(frame, text="Please enter your name to return a Vehicle", bg="#C3242A", fg="white", font=("Poppins", 12))
return_first_label = tk.Label(frame, text="Enter First name:", bg="#C3242A", fg="white", font=("Poppins", 12))
return_surname_label = tk.Label(frame, text="Enter Surname: ", bg="#C3242A", fg="white", font=("Poppins", 12))
return_first = tk.Entry(frame, font=("Poppins", 12), bg="#C3242A", fg="white")
return_surname = tk.Entry(frame, font=("Poppins", 12), bg="#C3242A", fg="white")
add2_button = tk.Button(frame, text="Delete", command=delete_record, bg="#C3242A", fg="white", font=("Poppins", 12))

username_lb2.grid(row=1, column=0, columnspan=2, pady=1, padx=5, sticky="news")
return_first_label.grid(row=2, column=0, pady=1, padx=5, sticky="e")
return_surname_label.grid(row=3, column=0, pady=1, padx=5, sticky="e")
return_first.grid(row=2, column=1, pady=1, padx=5, sticky="w")
return_surname.grid(row=3, column=1, pady=1, padx=5, sticky="w")
add2_button.grid(row=4, column=0, columnspan=2, pady=1 , padx=5, sticky="news")
window.mainloop()
