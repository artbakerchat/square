import random
from tkinter import *
def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)
root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
for x in range(0, 100):
    random_rectangle(400, 400)
root.mainloop()