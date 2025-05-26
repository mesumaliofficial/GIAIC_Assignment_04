from tkinter import *

root = Tk()
root.title("Canvas Eraser Example")

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

cell_size = 50
rows = 10
cols = 10
cells = []

for i in range(rows):
    row = []
    for j in range(cols):
        x1 = j * cell_size
        y1 = i * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
        row.append(rect)
    cells.append(row)

eraser_size = 60
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, outline="red", width=2)

def move_eraser(event):
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)
    erase_overlapping(x, y)

def erase_overlapping(x, y):
    x1, y1 = x, y
    x2, y2 = x + eraser_size, y + eraser_size

    for i in range(rows):
        for j in range(cols):
            rect_id = cells[i][j]
            rx1, ry1, rx2, ry2 = canvas.coords(rect_id)

            if not (x2 < rx1 or x1 > rx2 or y2 < ry1 or y1 > ry2):
                canvas.itemconfig(rect_id, fill="white")

canvas.bind("<B1-Motion>", move_eraser)

root.mainloop()
