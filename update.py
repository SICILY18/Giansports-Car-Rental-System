import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from PIL import Image, ImageTk
import os

def update_sportscat(event, combobox):
    selected_car = event.widget.get()
    if selected_car == "Sports":
        combobox.config(values=["Audi R8", "Porsche 911", "Ferrari Pista 488"])
    elif selected_car == "Sedan":
        combobox.config(values=["Honda Accord", "Honda Civic", "Audi E-tron"])
    elif selected_car == "Suv":
        combobox.config(values=["Lamborghini Urus", "Range Rover", "Toyota Fortuner"])
    elif selected_car == "Van":
        combobox.config(values=["Toyota Alphard", "Mercedes Benz Sprinter", "Hyundai Staria"])
    else:
        combobox.config(values=[])
        
        
def update_record():
    name = update_name_entry.get()
    surname = update_surname_entry.get()
    new_cartype = update_cartype_cb.get()
    new_cartrans = update_cartrans_cb.get()
    new_carmodel = update_carmodel_cb.get()

    if not (name and surname and new_cartype and new_cartrans and new_carmodel):
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    conn = sqlite3.connect('customer_database.db')
    c = conn.cursor()

    # Check if the customer exists in the database
    c.execute("SELECT * FROM customers WHERE name=? AND surname=?", (name, surname))
    customer_data = c.fetchone()

    if customer_data:
        # Update the record in the database
        c.execute("UPDATE customers SET cartype=?, cartrans=?, carmodel=? WHERE name=? AND surname=?", (new_cartype, new_cartrans, new_carmodel, name, surname))
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully.")
    else:
        messagebox.showerror("Error", "No customer found with the provided name and surname.")

    conn.close()

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


window = tk.Tk()
window.title("Customer Details")
window.geometry('1920x1080')
window.configure(bg="#D74B76")

background_image = Image.open("Giansports.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#GLOBAL VARS TO SA LABAS TO NG MGA FUNCTIONS 
global update_name_entry, update_surname_entry, update_cartype_cb, update_cartrans_cb, update_carmodel_cb

# Frame for the navbar
navbar_frame = tk.Frame(window, bg="#C3242A")
navbar_frame.place(relx=0.5, rely=0.15, anchor="n")

# Create labels for Home, Rent A Car, Show Cars, and Exit
home_lb = tk.Label(navbar_frame, text="Home", bg="#C3242A", fg="white", font=("Poppins", 16))
rent_lb = tk.Label(navbar_frame, text="Rent A Car", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
showcars_lb = tk.Label(navbar_frame, text="Show Cars", bg="#C3242A", fg="white", font=("Poppins", 16))
ex_lb = tk.Label(navbar_frame, text="Exit", bg="#C3242A", fg="white", font=("Poppins", 16))

# Pack labels parallel to each other
home_lb.pack(side="left", padx=10)
rent_lb.pack(side="left", padx=10)
showcars_lb.pack(side="left", padx=10)
ex_lb.pack(side="left", padx=10)

# Bind functionality to labels
home_lb.bind("<Button-1>", lambda event: home())
rent_lb.bind("<Button-1>", lambda event: rent())
showcars_lb.bind("<Button-1>", lambda event: showcars())
ex_lb.bind("<Button-1>", lambda event: exit())

# Frame for the customer details form
frame2 = tk.Frame(window, bg="#C3242A")
frame2.place(relx=0.5, rely=0.5, anchor="center")


navbar_frame = tk.Frame(window, bg="#C3242A")
navbar_frame.place(relx=0.5, rely=0.15, anchor="n")

# Create labels for Home, Rent A Car, Show Cars, and Exit
home_lb = tk.Label(navbar_frame, text="Home", bg="#C3242A", fg="white", font=("Poppins", 16))
rent_lb = tk.Label(navbar_frame, text="Rent A Car", bg="#C3242A", fg="white", font=("Poppins", 16))
showcars_lb = tk.Label(navbar_frame, text="Show Cars", bg="#C3242A", fg="white", font=("Poppins", 16))
return_lb = tk.Label(navbar_frame, text="Return a Car", bg="#C3242A", fg="white", font=("Poppins", 16))
updatecar_lb = tk.Label(navbar_frame, text="Update", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
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
showallrecords_lb.bind("<Button-1>", lambda event: show_all_records())
ex_lb.bind("<Button-1>", lambda event: exit())
# Frame for the customer details form
frame2 = tk.Frame(window, bg="#C3242A")
frame2.place(relx=0.5, rely=0.5, anchor="center")

update_name_label = tk.Label(frame2, text="Enter Name:", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
update_surname_label = tk.Label(frame2, text="Enter Surname:", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
update_cartype_label = tk.Label(frame2, text="Select New Car Type:", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
update_cartrans_label = tk.Label(frame2, text="Select New Car Transmission:", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
update_carmodel_label = tk.Label(frame2, text="Select New Car Model:", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))

update_name_entry = tk.Entry(frame2)
update_surname_entry = tk.Entry(frame2)
update_cartype_cb = ttk.Combobox(frame2, values=["Sports", "Sedan", "Suv", "Van"])
update_cartrans_cb = ttk.Combobox(frame2, values=["Manual", "Automatic"])
update_carmodel_cb = ttk.Combobox(frame2, values=[])

update_button = tk.Button(frame2, text="Update", command=update_record)

update_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
update_surname_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
update_cartype_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
update_cartrans_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
update_carmodel_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

update_name_entry.grid(row=0, column=1, padx=10, pady=5)
update_surname_entry.grid(row=1, column=1, padx=10, pady=5)
update_cartype_cb.grid(row=2, column=1, padx=10, pady=5)
update_cartrans_cb.grid(row=3, column=1, padx=10, pady=5)
update_carmodel_cb.grid(row=4, column=1, padx=10, pady=5)

update_button.grid(row=5, columnspan=2, pady=10)

# Bind function to ComboboxSelected event to update car models based on the selected car type
update_cartype_cb.bind("<<ComboboxSelected>>", lambda event: update_sportscat(event, update_carmodel_cb))

window.mainloop()
