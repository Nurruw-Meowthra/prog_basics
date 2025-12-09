from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width=800, height=800, background="white")

#ruudud valged 32tk
"""
Rida 1
"""
tahvel.create_rectangle(0,0,100,100, fill="black")
tahvel.create_rectangle(100,0,200,100)
tahvel.create_rectangle(200,0,300,100, fill="black")
tahvel.create_rectangle(300,0,400,100)
tahvel.create_rectangle(400,0,500,100, fill="black")
tahvel.create_rectangle(500,0,600,100)
tahvel.create_rectangle(600,0,700,100, fill="black")
tahvel.create_rectangle(700,0,800,100)
"""
Rida 2
"""
tahvel.create_rectangle(0,100,100,200)
tahvel.create_rectangle(100,100,200,200, fill="black")
tahvel.create_rectangle(200,100,300,200)
tahvel.create_rectangle(300,100,400,200, fill="black")
tahvel.create_rectangle(400,100,500,200)
tahvel.create_rectangle(500,100,600,200, fill="black")
tahvel.create_rectangle(600,100,700,200)
tahvel.create_rectangle(700,100,800,200, fill="black")
"""
Rida 3
"""
tahvel.create_rectangle(0,200,100,300, fill="black")
tahvel.create_rectangle(100,200,200,300)
tahvel.create_rectangle(200,200,300,300, fill="black")
tahvel.create_rectangle(300,200,400,300)
tahvel.create_rectangle(400,200,500,300, fill="black")
tahvel.create_rectangle(500,200,600,300)
tahvel.create_rectangle(600,200,700,300, fill="black")
tahvel.create_rectangle(700,200,800,300)
"""
Rida 4
"""
tahvel.create_rectangle(0,300,100,400)
tahvel.create_rectangle(100,300,200,400, fill="black")
tahvel.create_rectangle(200,300,300,400)
tahvel.create_rectangle(300,300,400,400, fill="black")
tahvel.create_rectangle(400,300,500,400)
tahvel.create_rectangle(500,300,600,400, fill="black")
tahvel.create_rectangle(600,300,700,400)
tahvel.create_rectangle(700,300,800,400, fill="black")
"""
Rida 5
"""
tahvel.create_rectangle(0,400,100,500, fill="black")
tahvel.create_rectangle(100,400,200,500)
tahvel.create_rectangle(200,400,300,500, fill="black")
tahvel.create_rectangle(300,400,400,500)
tahvel.create_rectangle(400,400,500,500, fill="black")
tahvel.create_rectangle(500,400,600,500)
tahvel.create_rectangle(600,400,700,500, fill="black")
tahvel.create_rectangle(700,400,800,500)
"""
Rida 6
"""
tahvel.create_rectangle(0,500,100,600)
tahvel.create_rectangle(100,500,200,600, fill="black")
tahvel.create_rectangle(200,500,300,600)
tahvel.create_rectangle(300,500,400,600, fill="black")
tahvel.create_rectangle(400,500,500,600)
tahvel.create_rectangle(500,500,600,600, fill="black")
tahvel.create_rectangle(600,500,700,600)
tahvel.create_rectangle(700,500,800,600, fill="black")
"""
Rida 7
"""
tahvel.create_rectangle(0,600,100,700, fill="black")
tahvel.create_rectangle(100,600,200,700)
tahvel.create_rectangle(200,600,300,700, fill="black")
tahvel.create_rectangle(300,600,400,700)
tahvel.create_rectangle(400,600,500,700, fill="black")
tahvel.create_rectangle(500,600,600,700)
tahvel.create_rectangle(600,600,700,700, fill="black")
tahvel.create_rectangle(700,600,800,700)
"""
Rida 8
"""
tahvel.create_rectangle(0,700,100,800)
tahvel.create_rectangle(100,700,200,800, fill="black")
tahvel.create_rectangle(200,700,300,800)
tahvel.create_rectangle(300,700,400,800, fill="black")
tahvel.create_rectangle(400,700,500,800)
tahvel.create_rectangle(500,700,600,800, fill="black")
tahvel.create_rectangle(600,700,700,800)
tahvel.create_rectangle(700,700,800,800, fill="black")



tahvel.pack()
raam.mainloop()