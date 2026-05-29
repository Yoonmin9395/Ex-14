import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Управление кафе-мороженым")
root.geometry("1040x560")
root.configure(bg="#efefef")
root.resizable(False, False)

left_frame = tk.LabelFrame(
    root,
    text = "Сорта мороженого (вкусы)",
    bg = "#9966cc",
    font = ("Arial", 11)
)
left_frame.place(x = 30, y = 70, width = 420, height = 420)

flavor_listbox = tk.Listbox(
    left_frame,
    font = ("Arial", 12),
    relief = "solid",
    borderwidth = 1
)
flavor_listbox.place(x = 10, y = 10, width = 390, height = 300)

for item in ["Фисташковое", "Шоколадное", "Клубничное"]:
    flavor_listbox.insert(tk.END, item)

flavor_entry = tk.Entry(left_frame)
flavor_entry.place(x = 110, y = 325, width = 160)

right_frame = tk.LabelFrame(
    root,
    text = "Типы мороженого",
    bg = "#9966cc",
    font = ("Arial", 11)
)
right_frame.place(x = 590, y = 70, width = 420, height = 420)

type_listbox = tk.Listbox(
    right_frame,
    font = ("Arial", 10),
    relief = "solid",
    borderwidth = 1
)
type_listbox.place(x = 10, y = 10, width = 390, height = 300)

for item in ["На палочке", "Мягкое"]:
    type_listbox.insert(tk.END, item)

type_entry = tk.Entry(right_frame)
type_entry.place(x = 110, y = 325, width = 160)

center_frame = tk.LabelFrame(
    root,
    bg = "#9966cc",
    relief = "solid",
    borderwidth = 1
)
center_frame.place(x = 460, y = 338, width = 120, height = 150)

info_label = tk.Label(
    center_frame,
    text = "Название:\nМороженое\nРадуга\nКухня:\nКафе-мороженое",
    justify = "left",
    anchor = "nw",
    bg = "white",
    font = ("Arial", 10),
    relief = "solid",
    borderwidth = 1
)
info_label.place(x = 5, y = 5, width = 108, height = 82)

btn_info = tk.Button(
    center_frame,
    text = "Добавить информацию",
    font = ("Arial", 7)
)
btn_info.place(x = 5, y = 93, width = 108)

btn_ready = tk.Button(
    center_frame,
    text = "Готово",
    font = ("Arial", 7)
)
btn_ready.place(x = 5, y = 118, width = 108)

def add_flavor():
    text = flavor_entry.get()

    if text:
        flavor_listbox.insert(tk.END, text)
        flavor_entry.delete(0, tk.END)

def delete_flavor():
    selected = flavor_listbox.curselection()

    if selected:
        flavor_listbox.delete(selected)

def check_flavor():
    text = flavor_entry.get()

    if text in flavor_listbox.get(0, tk.END):
        messagebox.showinfo("Проверка", "Вкус найден")
    else:
        messagebox.showwarning("Проверка", "Вкуса нет")

def add_type():
    text = type_entry.get()

    if text:
        type_listbox.insert(tk.END, text)
        type_entry.delete(0, tk.END)

def delete_type():
    selected = type_listbox.curselection()

    if selected:
        type_listbox.delete(selected)

def show_types():
    all_types = "\n".join(type_listbox.get(0, tk.END))
    messagebox.showinfo("Типы мороженого", all_types)

btn_add = tk.Button(
    left_frame,
    text = "Добавить",
    width = 10,
    command = add_flavor
)
btn_add.place(x = 50, y = 355)

btn_delete = tk.Button(
    left_frame,
    text = "Удалить",
    width = 10,
    command = delete_flavor
)
btn_delete.place(x = 150, y = 355)

btn_check = tk.Button(
    left_frame,
    text = "Проверить",
    width = 10,
    command = check_flavor
)
btn_check.place(x = 250, y = 355)

btn_add_type = tk.Button(
    right_frame,
    text = "Добавить тип",
    width = 12,
    command = add_type
)
btn_add_type.place(x=30, y=355)

btn_delete_type = tk.Button(
    right_frame,
    text = "Удалить тип",
    width = 12,
    command = delete_type
)
btn_delete_type.place(x=145, y=355)

btn_show_types = tk.Button(
    right_frame,
    text = "Список типов",
    width = 12,
    command = show_types
)
btn_show_types.place(x = 260, y = 355)

root.mainloop()
