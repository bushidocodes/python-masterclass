import math
import tkinter


def parabola(canvas, size):
    for x in range(-size, size):
        y = (x * x) / size
        plot(canvas, x, y)


def circle(canvas, radius, g, h, outline="red"):
    canvas.create_oval(
        g + radius, h + radius, g - radius, h - radius, outline=outline, width=2
    )


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(
        x, -y, x + 1, -y + 1, fill="red"
    )  # Invert y axis because Canvas y axis is flipped from math


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

mainCanvas = tkinter.Canvas(mainWindow, width=640, height=480)
mainCanvas.grid(row=0, column=0)
draw_axes(mainCanvas)

parabola(mainCanvas, 100)
parabola(mainCanvas, 200)
circle(mainCanvas, 50, 0, 0)
circle(mainCanvas, 100, 100, 100, outline="purple")

mainWindow.mainloop()
