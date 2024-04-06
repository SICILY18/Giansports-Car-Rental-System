import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from PIL import Image, ImageTk
import os

def search_car_availability():
    car_model = car_model_combobox.get()
    if car_model:
        conn = sqlite3.connect('customer_database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customers WHERE carmodel = ?", (car_model,))
        row = c.fetchone()
        conn.close()

        if row:
            messagebox.showinfo("Car Availability", f"Car model '{car_model}' is not available for rent because it has already been rented.")
        else:
            messagebox.showinfo("Car Availability", f"Car model '{car_model}' is available for rent.")
    else:
        messagebox.showerror("Error", "Please select a car model to search.")

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
window.title("Show Available Cars")
window.geometry('1920x1080')
window.configure(bg="#D74B76")

background_image = Image.open("Giansports.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for the navbar
navbar_frame = tk.Frame(window, bg="#C3242A")
navbar_frame.place(relx=0.5, rely=0.15, anchor="n")

home_lb = tk.Label(navbar_frame, text="Home", bg="#C3242A", fg="white", font=("Poppins", 16))
rent_lb = tk.Label(navbar_frame, text="Rent A Car", bg="#C3242A", fg="white", font=("Poppins", 16))
showcars_lb = tk.Label(navbar_frame, text="Show Cars", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
return_lb = tk.Label(navbar_frame, text="Return a Car", bg="#C3242A", fg="white", font=("Poppins", 16))
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
showallrecords_lb.bind("<Button-1>", lambda event: show_all_records())
ex_lb.bind("<Button-1>", lambda event: exit())

# Frame for the customer details form
frame = tk.Frame(window, bg="#C3242A")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Label and Combobox for car model selection
car_model_label = tk.Label(frame, text="Select Car Model:", bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
car_model_label.grid(row=0, column=0, padx=10, pady=10)

car_model_combobox = ttk.Combobox(frame, width=20)
car_model_combobox['values'] = ["Audi R8", "Porsche 911", "Ferrari Pista 488", "Honda Accord", "Honda Civic", "Audi E-tron", "Lamborghini Urus", "Range Rover", "Toyota Fortuner", "Toyota Alphard", "Mercedes Benz Sprinter", "Hyundai Staria"]
car_model_combobox.grid(row=0, column=1, padx=10, pady=10)

# Button to search car availability
search_button = tk.Button(frame, text="Search", command=search_car_availability, bg="#C3242A", fg="#ffffff", font=("Poppins", 12))
search_button.grid(row=0, column=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
