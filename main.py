from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=200, bg='white')
canvas.pack(pady=20)

point_1 = 10, 10
point_2 = 100, 100

for i in range(1):
    canvas.create_line(point_1[0], point_1[1], point_2[0], point_2[1], fill='#1AE2C2')
    canvas.create_line(point_1[0], point_2[1], point_2[0], point_1[1], fill='#1AE2C2')

    canvas.create_oval(point_1[0], point_1[1], point_2[0], point_2[1])

    canvas.create_rectangle(point_1[0] + (point_2[0] - point_1[0]) * 0.25, point_1[1],
                            point_1[0] + (point_2[0] - point_1[0]) * 0.75, point_2[1])


root.mainloop()
