from tkinter import *
raam = Tk()
raam.title("Põhja-Sakala valla lipp")
tahvel = Canvas(raam, width=500, height=300, background="white")
tahvel.pack()

# upper red rectangle
tahvel.create_rectangle(0,75,500,150, fill="red")

# lower red rectangle
tahvel.create_rectangle(0,230,500,300, fill="red")

raam.mainloop()