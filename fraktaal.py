from tkinter import *

raam = Tk()
raam.title("Vicsek Fractal")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.pack()

def draw_vicsek(x, y, size, level):
    if level == 0:
        tahvel.create_rectangle(x, y, x + size, y + size, fill="black", outline="")
    else:
        new_size = size / 3
           
        # 1. Top Center
        draw_vicsek(x, y, new_size, level - 1)
        
        # 2. Middle Left
        draw_vicsek(x + 2 * new_size, y, new_size, level - 1)
        
        # 3. Center
        draw_vicsek(x + new_size, y + new_size, new_size, level - 1)
        
        # 4. Middle Right
        draw_vicsek(x, y + 2 * new_size, new_size, level - 1)
        
        # 5. Bottom Center
        draw_vicsek(x + 2 * new_size, y + 2 * new_size, new_size, level - 1)

def keyReleased(event):
    if event.char.isdigit():
        level = int(event.char)
        
        tahvel.delete("all")
        
        print(f"Drawing Level {level}...")
        draw_vicsek(50, 50, 500, level)
        print("Done.")

    elif event.keysym == 'Escape':
        raam.destroy()

raam.bind('<Key>', keyReleased)

raam.mainloop()