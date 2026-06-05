import tkinter as tk

todo_items = []


def create_task():
    text = input_field.get().strip()

    if not text:
        info_label.config(text="Введите задачу")
        return

    if len(text) > 20:
        info_label.config(text="Не больше 20 символов")
        return

    todo_items.append(text)
    tasks_box.insert(tk.END, text)

    input_field.delete(0, tk.END)

    info_label.config(text="Добавлено")


def delete_task():
    chosen = tasks_box.curselection()

    if len(chosen) == 0:
        info_label.config(text="Выберите задачу")
        return

    position = chosen[0]

    tasks_box.delete(position)
    del todo_items[position]

    info_label.config(text="Удалено")


window = tk.Tk()

window.title("Список дел")
window.geometry("430x480")
window.config(bg="#202020")


header = tk.Label(
    window,
    text="Мои задачи",
    font=("Verdana", 18, "bold"),
    bg="#202020",
    fg="white"
)
header.pack(pady=12)


input_field = tk.Entry(
    window,
    width=28,
    font=("Verdana", 13),
    bg="#303030",
    fg="white",
    insertbackground="white"
)
input_field.pack(pady=8)


add_btn = tk.Button(
    window,
    text="Добавить задачу",
    command=create_task,
    width=22,
    bg="#4b83f5",
    fg="white",
    font=("Verdana", 10)
)
add_btn.pack(pady=4)


delete_btn = tk.Button(
    window,
    text="Удалить задачу",
    command=delete_task,
    width=22,
    bg="#d9534f",
    fg="white",
    font=("Verdana", 10)
)
delete_btn.pack(pady=4)


tasks_box = tk.Listbox(
    window,
    width=38,
    height=13,
    font=("Verdana", 11),
    bg="#303030",
    fg="white",
    selectbackground="#4b83f5"
)
tasks_box.pack(pady=18)


info_label = tk.Label(
    window,
    text="",
    bg="#202020",
    fg="#90ee90",
    font=("Verdana", 9)
)
info_label.pack()


window.mainloop()
