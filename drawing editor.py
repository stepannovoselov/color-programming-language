import tkinter as tk
import datetime
from tkinter.messagebox import showinfo, showerror
from tkinter import filedialog
from PIL import Image

window = tk.Tk()
window.resizable(False, False)
window.title("Piet artist")

c = tk.Canvas(window, width=1000, height=720)
c.pack(side=tk.LEFT, padx=25, pady=25)


def on_leave(event, item):
    c.itemconfigure(item, outline="black", width=1)


def on_enter(event, item):
    c.itemconfigure(item, outline="black", width=3)
    c.tag_raise(item)


def on_click(event, item):
    global color
    c.itemconfigure(item, fill=color)
    c.tag_raise(item)


color = "a6caf0"
def change_color(c):
    global color
    color = c


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))



def save_png():
    img = Image.new("RGB", (60, 46), "lightblue")

    colors = [c.itemcget(i, "fill") for i in squares]

    iteration = 0
    for y in range(46):
        for x in range(60):
            r, g, b = (int(colors[iteration][1:3], 16), int(colors[iteration][3:5], 16), int(colors[iteration][5:7], 16))
            img.putpixel((x, y), (r, g, b))
            iteration += 1

    filename = f"output at {str(datetime.datetime.now().time()).split('.')[0].replace(':', '-')}"
    img.save(f"{filename}.png")
    showinfo("Успех!", f"Файл успешно сохранен как {filename}.png")


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def open_png():
    filename = filedialog.askopenfilename(title="Выберите картинку", filetypes=(("png files", "*.png"),))
    if filename != "":
        img = Image.open(filename)

        if (img.height, img.width) != (46, 60):
            showerror("Ошибка", "Файл должен быть размером 60x46")
            return

        iteration = 0
        for y in range(46):
            for x in range(60):
                hex = rgb_to_hex(img.getpixel((x, y)))
                c.itemconfigure(squares[iteration], fill="#" + str(hex))
                iteration += 1


square_size = 15
squares = []
for h in range(int(700 / square_size)):
    for w in range(int((1000 * 0.9) / square_size)):
        square = c.create_rectangle(w * square_size, h * square_size, (w + 1) * square_size, (h + 1) * square_size, fill="#a6caf0", width=1)
        c.tag_bind(square, "<Button-1>", lambda event, item=square: on_click(event, item))
        c.tag_bind(square, "<Enter>", lambda event, item=square: on_enter(event, item))
        c.tag_bind(square, "<Leave>", lambda event, item=square: on_leave(event, item))
        squares.append(square)

panel_frame = tk.Frame(window)
panel_frame.pack(side=tk.RIGHT)

buttons = [
    tk.Button(panel_frame, text="Желтый", font=("Comics sans", 9, "bold"), width=20, bg="#ffff00", command=lambda: change_color("#ffff00")),
    tk.Button(panel_frame, text="Зеленый", font=("Comics sans", 9, "bold"), width=20, bg="#00ff00", command=lambda: change_color("#00ff00")),
    tk.Button(panel_frame, text="Синий", font=("Comics sans", 9, "bold"), width=20, bg="#008cf0", command=lambda: change_color("#008cf0")),
    tk.Button(panel_frame, text="Красный", font=("Comics sans", 9, "bold"), width=20, bg="#ff0000", command=lambda: change_color("#ff0000")),
    tk.Button(panel_frame, text="Розовый", font=("Comics sans", 9, "bold"), width=20, bg="#ff00ff", command=lambda: change_color("#ff00ff")),
    tk.Button(panel_frame, text="Серый", font=("Comics sans", 9, "bold"), width=20, bg="#808080", command=lambda: change_color("#808080")),
    tk.Button(panel_frame, text="Оранжевый", font=("Comics sans", 9, "bold"), width=20, bg="#FF8C00", command=lambda: change_color("#FF8C00")),
    tk.Button(panel_frame, text="Хаки", font=("Comics sans", 9, "bold"), width=20, bg="#F0E68C", command=lambda: change_color("#F0E68C")),
    tk.Button(panel_frame, text="Циановый", font=("Comics sans", 9, "bold"), width=20, bg="#008B8B", command=lambda: change_color("#008B8B")),
    tk.Button(panel_frame, text="Аква", font=("Comics sans", 9, "bold"), width=20, bg="#7FFFD4", command=lambda: change_color("#7FFFD4")),

    tk.Button(panel_frame, text="Темно-желтый", font=("Comics sans", 9, "bold"), width=20, bg="#b57900", command=lambda: change_color("#b57900")),
    tk.Button(panel_frame, text="Темно-зеленый", font=("Comics sans", 9, "bold"), width=20, bg="#013220", command=lambda: change_color("#013220")),
    tk.Button(panel_frame, text="Темно-синий", font=("Comics sans", 9, "bold"), width=20, bg="#00508a", command=lambda: change_color("#00508a")),
    tk.Button(panel_frame, text="Темно-красный", font=("Comics sans", 9, "bold"), width=20, bg="#8b0000", command=lambda: change_color("#8b0000")),
    tk.Button(panel_frame, text="Темно-розовый", font=("Comics sans", 9, "bold"), width=20, bg="#9400d3", command=lambda: change_color("#9400d3")),

    tk.Button(panel_frame, text="Белый", font=("Comics sans", 9, "bold"), width=20, bg="#ffffff", command=lambda: change_color("#ffffff")),
    tk.Button(panel_frame, text="Черный", font=("Comics sans", 9, "bold"), fg="white", width=20, bg="#000000", command=lambda: change_color("#000000")),
    tk.Button(panel_frame, text="Нет цвета", font=("Comics sans", 9, "bold"), width=20, bg="#a6caf0", command=lambda: change_color("#a6caf0")),
]
[i.pack(padx=10, pady=5, fill=tk.X) for i in buttons]

tk.Label(panel_frame).pack(pady=5)

tk.Button(panel_frame, text="Сохранить PNG", command=save_png).pack()
tk.Button(panel_frame, text="Открыть PNG", command=open_png).pack()

window.mainloop()
