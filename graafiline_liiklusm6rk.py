from tkinter import *
raam = Tk()
raam.title("Peatee")
tahvel = Canvas(raam, width=500, height=500, background="white")
tahvel.pack()
tahvel.create_polygon(250,50,50,250,250,450,450,250, fill="white",outline="black",width=5)
tahvel.create_polygon(250,80,80,250,250,420,420,250, fill="yellow",outline="black",width=3)
raam.mainloop()