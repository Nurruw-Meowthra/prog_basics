from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=500, height=500, background="white")

#Walls
tahvel.create_rectangle(100,200,400,450, fill="coral3")
#Roof
tahvel.create_polygon(55,200,250,50,450,200, fill="indianred4")

#Window
tahvel.create_rectangle(200,250,300,350, fill="deepskyblue2")
tahvel.create_rectangle(201,295,299,305, fill="saddlebrown", outline="saddlebrown")
tahvel.create_rectangle(245,251,255,349, fill="saddlebrown", outline="saddlebrown")


tahvel.pack()
raam.mainloop()