import tkinter as tk
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
def exit():
    window.destroy()

window = tk.Tk()
window.title("Homepage")
window.geometry('1920x1080')
window.configure(bg="#C3242A")

background_image = Image.open("Giansports.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#C3242A")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create labels for Home and Rent A Car
home_lb = tk.Label(frame, text="Home", bg="#C3242A", fg="#F5DD61", font=("Poppins", 16))
rent_lb = tk.Label(frame, text="Rent A Car", bg="#C3242A", fg="white", font=("Poppins", 16))
showcars_lb = tk.Label(frame, text="Show Cars", bg="#C3242A", fg="white", font=("Poppins", 16))
return_lb = tk.Label(frame, text="Return a Car", bg="#C3242A", fg="white", font=("Poppins", 16))
updatecar_lb = tk.Label(frame, text="Update", bg="#C3242A", fg="white", font=("Poppins", 16))
showrecord_lb = tk.Label(frame, text="Show Reciept", bg="#C3242A", fg="white", font=("Poppins", 16))
ex_lb = tk.Label(frame, text="Exit", bg="#C3242A", fg="white", font=("Poppins", 16))

# Pack labels
home_lb.pack(pady=5)
rent_lb.pack(pady=5)
showcars_lb.pack(pady=5)
rent_lb.pack(pady=5)
showcars_lb.pack(pady=5) 
return_lb.pack(pady=5)
updatecar_lb.pack(pady=5)
showrecord_lb.pack(pady=5)
ex_lb.pack(pady=5)

# Bind functionality to labels
home_lb.bind("<Button-1>", lambda event: home())
rent_lb.bind("<Button-1>", lambda event: rent())
showcars_lb.bind("<Button-1>", lambda event: showcars())
return_lb.bind("<Button-1>", lambda event: returncar())
updatecar_lb.bind("<Button-1>", lambda event: updatecar())
showrecord_lb.bind("<Button-1>", lambda event: showrecord())
ex_lb.bind("<Button-1>", lambda event: exit())
window.mainloop()
