from tkinter import *
import time

root = Tk()

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

def create_rect(x, y, text):

    return canvas.create_rectangle(15 + x, 15 + y, x + 75, y + 75)
    #canvas.create_text(65 + x, 65 + y, text=text)

nice = create_rect(100, 100, "hey")

for s in range(0, 100):
    canvas.move(nice, s, s)
    root.update()
    time.sleep(0.1)

root.geometry("1024x768")
root.mainloop()
