import tkinter as tk
from tkinter import Canvas, Text, Frame, Button, messagebox, Toplevel
import sqlite3
from datetime import datetime
import random

class CarRentalSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental System")

        self.canvas = Canvas(self.root, width=800, height=600)  # Adjust canvas size
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Expand canvas to fill window

        self.img = tk.PhotoImage(file="bg.jpg")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        self.main_frame = tk.Frame(self.canvas)  # Create frame inside canvas
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_widgets()

        self.db_connection = sqlite3.connect("car_rental.db")
        self.create_table()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Rentals
                          (id INTEGER PRIMARY KEY,
                           customer_name TEXT,
                           car_type TEXT,
                           car_model TEXT,
                           color TEXT,
                           license_plate TEXT,
                           duration INTEGER,
                           total_amount REAL,
                           transaction_id TEXT,
                           start_date TEXT,
                           end_date TEXT)''')
        self.db_connection.commit()

    def create_widgets(self):
        # Labels
        tk.Label(self.main_frame, text="Name of the customer:").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Car Type:").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Car Model:").grid(row=2, column=0)
        tk.Label(self.main_frame, text="Color:").grid(row=3, column=0)
        tk.Label(self.main_frame, text="License Plate Number:").grid(row=4, column=0)
        tk.Label(self.main_frame, text="Duration of Rental (days):").grid(row=5, column=0)
        tk.Label(self.main_frame, text="Total Amount:").grid(row=6, column=0)
        tk.Label(self.main_frame, text="Transaction ID:").grid(row=7, column=0)
        tk.Label(self.main_frame, text="Start Date (YYYY-MM-DD):").grid(row=8, column=0)
        tk.Label(self.main_frame, text="End Date (YYYY-MM-DD):").grid(row=9, column=0)

        # Entry fields
        self.customer_name_entry = tk.Entry(self.main_frame)
        self.customer_name_entry.grid(row=0, column=1)
        self.car_type_entry = tk.Entry(self.main_frame)
        self.car_type_entry.grid(row=1, column=1)
        self.car_model_entry = tk.Entry(self.main_frame)
        self.car_model_entry.grid(row=2, column=1)
        self.color_entry = tk.Entry(self.main_frame)
        self.color_entry.grid(row=3, column=1)
        self.license_plate_entry = tk.Entry(self.main_frame)
        self.license_plate_entry.grid(row=4, column=1)
        self.duration_entry = tk.Entry(self.main_frame)
        self.duration_entry.grid(row=5, column=1)
        self.total_amount_entry = tk.Entry(self.main_frame)
        self.total_amount_entry.grid(row=6, column=1)
        self.transaction_id_entry = tk.Entry(self.main_frame, state='disabled')
        self.transaction_id_entry.grid(row=7, column=1)
        self.start_date_entry = tk.Entry(self.main_frame)
        self.start_date_entry.grid(row=8, column=1)
        self.end_date_entry = tk.Entry(self.main_frame)
        self.end_date_entry.grid(row=9, column=1)

        # Button
        tk.Button(self.main_frame, text="Submit", command=self.submit_form).grid(row=10, columnspan=2)

        # Receipt Text
        self.receipt_text = Text(self.main_frame, width=60, height=15, wrap=tk.WORD)  # Adjust width and height
        self.receipt_text.grid(row=11, columnspan=2)

    def submit_form(self):
        try:
            # Retrieve data from entry fields
            customer_name = self.customer_name_entry.get()
            car_type = self.car_type_entry.get()
            car_model = self.car_model_entry.get()
            color = self.color_entry.get()
            license_plate = self.license_plate_entry.get()
            duration = int(self.duration_entry.get())
            total_amount = float(self.total_amount_entry.get())
            transaction_id = self.generate_transaction_id()
            start_date = self.start_date_entry.get()
            end_date = self.end_date_entry.get()

            # Insert data into SQLite database
            cursor = self.db_connection.cursor()
            cursor.execute('''INSERT INTO Rentals
                              (customer_name, car_type, car_model, color, license_plate,
                               duration, total_amount, transaction_id, start_date, end_date)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (customer_name, car_type, car_model, color, license_plate,
                            duration, total_amount, transaction_id, start_date, end_date))
            self.db_connection.commit()

            # Show success message
            messagebox.showinfo("Success", "Record created successfully!")

            # Display receipt
            self.display_receipt(customer_name, car_type, car_model, color, license_plate,
                                 duration, total_amount, transaction_id, start_date, end_date)

            # Clear entry fields after submission
            self.clear_entries()

            # Display database contents in a new window
            self.display_database()
        except Exception as e:
            # Show error message if there's an issue
            messagebox.showerror("Error", str(e))

    def clear_entries(self):
        self.customer_name_entry.delete(0, tk.END)
        self.car_type_entry.delete(0, tk.END)
        self.car_model_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.license_plate_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.total_amount_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)

    def generate_transaction_id(self):
        # Generate a transaction ID using current timestamp and a random number
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_number = random.randint(10000, 99999)
        return f"TRN{timestamp}{random_number}"

    def display_receipt(self, customer_name, car_type, car_model, color, license_plate,
                        duration, total_amount, transaction_id, start_date, end_date):
        receipt_content = f"Receipt:\nName of the Customer: {customer_name}\nCar Type: {car_type}\n" \
                          f"Car Model: {car_model}\nColor: {color}\nLicense Plate Number: {license_plate}\n" \
                          f"Duration of Rental: {duration} day(s)\nTotal Amount Paid: {total_amount}\n" \
                          f"Transaction ID: {transaction_id}\nRental start date and time: {start_date}\n" \
                          f"Rental end date and time: {end_date}"

        self.receipt_text.delete("1.0", tk.END)
        self.receipt_text.insert(tk.END, receipt_content)

    def display_database(self):
        # Create a new window to display database contents
        db_window = Toplevel(self.root)
        db_window.title("Database Contents")

        # Fetch data from the database
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Rentals")
        data = cursor.fetchall()

        # Display database contents in a Text widget
        db_text = Text(db_window)
        for row in data:
            db_text.insert(tk.END, f"{row}\n")
        db_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalSystem(root)
    root.mainloop()
