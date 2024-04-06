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


def show_record_details():
    name = username_entry.get().strip().title()  # Convert to title case
    surname = surname_entry.get().strip().title()  # Convert to title case
    
    if not (name and surname):
        messagebox.showerror("Error", "Please enter both name and surname.")
        return
    
    conn = sqlite3.connect('customer_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE TRIM(UPPER(name))=? AND TRIM(UPPER(surname))=?", (name.upper(), surname.upper()))
    record = c.fetchone()
    conn.close()
    
    if record:
        receipt_window = tk.Toplevel(window)
        receipt_window.title("Transaction Receipt")
        receipt_window.geometry("400x200")
        receipt_frame = tk.Frame(receipt_window)
        receipt_frame.pack(expand=True, fill="both")
        
        fields = ["Name", "Surname", "Address", "Car Type", "Car Transmission", "Car Model"]
        values = record
        
        receipt_text = "\n".join([f"{field}: {value}" for field, value in zip(fields, values)])
        receipt_label = tk.Label(receipt_frame, text=receipt_text, font=("Helvetica", 12))
        receipt_label.pack(padx=20, pady=20)
    else:
        messagebox.showinfo("No Record", f"No transaction records found for {name} {surname}.")


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


def exit_program():
    window.destroy()


def sportscat(event):
    selectedcar = carselc_cb.get()
    if selectedcar == "Sports":
        carmodel_cb.config(values=["Audi R8", "Porsche 911", "Ferrari Pista 488"])
    elif selectedcar == "Sedan":
        carmodel_cb.config(values=["Honda Accord", "Honda Civic", "Audi E-tron"])
    elif selectedcar == "Suv":
        carmodel_cb.config(values=["Lamborghini Urus", "Range Rover", "Toyota Fortuner"])
    elif selectedcar == "Van":
        carmodel_cb.config(values=["Toyota Alphard", "Mercedes Benz Sprinter", "Hyundai Staria"])
    else:
        carmodel_cb.config(values=[])


window = tk.Tk()
window.title("Customer Details")
window.geometry('1920x1080')
window.configure(bg="#D74B76")

background_image = Image.open("Giansports.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for the customer details form
frame = tk.Frame(window, bg="#C3242A")
frame.place(relx=0.5, rely=0.5, anchor="center")
navbar_frame = tk.Frame(window, bg="#C3242A")
navbar_frame.place(relx=0.5, rely=0.15, anchor="n")

home_lb = tk.Label(navbar_frame, text="Home", bg="#C3242A", fg="white", font=("Poppins", 16))
rent_lb = tk.Label(navbar_frame, text="Rent A Car", bg="#C3242A", fg="white", font=("Poppins", 16))
showcars_lb = tk.Label(navbar_frame, text="Show Cars", bg="#C3242A", fg="white", font=("Poppins", 16))
return_lb = tk.Label(navbar_frame, text="Return a Car", bg="#C3242A", fg="white", font=("Poppins", 16))
updatecar_lb = tk.Label(navbar_frame, text="Update", bg="#C3242A", fg="white", font=("Poppins", 16))
showrecord_lb = tk.Label(navbar_frame, text="Show Receipt", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
showallrecords_lb = tk.Label(navbar_frame, text="Show All Reciept", bg="#C3242A", fg="white", font=("Poppins", 16))
ex_lb = tk.Label(navbar_frame, text="Exit", bg="#C3242A", fg="white", font=("Poppins", 16))

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
showrecord_lb.bind("<Button-1>", lambda event: show_record_details())
showallrecords_lb.bind("<Button-1>", lambda event: show_all_records())
ex_lb.bind("<Button-1>", lambda event: exit_program())

cust_label = tk.Label(frame, text="Enter Your Details to Show Receipt", bg="#C3242A", fg="#ffffff", font=("Poppins", 16))
username_lb = tk.Label(frame, text="Name", bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
username_entry = tk.Entry(frame, font=("Poppins", 12))
surname_lb = tk.Label(frame, text="Surname", bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
surname_entry = tk.Entry(frame, font=("Poppins", 12))

# Grid placement for customer details form
cust_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
username_lb.grid(row=1, column=0, padx=5, pady=5, sticky="e")
username_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
surname_lb.grid(row=2, column=0, padx=5, pady=5, sticky="e")
surname_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

add_button = tk.Button(frame, text="Submit", command=show_record_details, bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
add_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()
