import pyautogui as pg
from tkinter import Tk, Label, PhotoImage


def show_mouse_position(mouse_coordinates_label):
    x_coordinate = 'Координата абсциссы → : {:4d}'.format(pg.position().x)
    y_coordinate = 'Координата ординаты ↓ : {:4d}'.format(pg.position().y)

    label_text = x_coordinate + '\n' + y_coordinate

    mouse_coordinates_label.config(text=label_text)
    mouse_coordinates_label.after(50, lambda mouse=mouse_coordinates_label:
                                  show_mouse_position(mouse_coordinates_label))


if __name__ == "__main__":
    root = Tk()
    root.title("Координаты курсора на экране.")
    root.geometry('530x60')
    root.resizable(0, 0)

    icon = PhotoImage(file = "mouse_icon.png")
    root.iconphoto(False, icon)

    mouse_coordinates_label = Label(root)
    mouse_coordinates_label.pack()

    show_mouse_position(mouse_coordinates_label)

    root.mainloop()
