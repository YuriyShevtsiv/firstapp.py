import tkinter as tk
root = tk.Tk()
root.title("Мій перший GUI-додаток Tkinter")
root.geometry("450x300")
root.config(bg="#f0f0f0")
def update_label_content():
    """
    Отримує текст з поля вводу Entry, оновлює вміст Label
    і змінює колір тексту Label на жовтий (використовуючи .config()).
    """
    # Отримуємо текст із поля вводу
    input_text = text_entry.get()

    # Перевіряємо, чи введено текст, і встановлюємо відповідний вміст
    if input_text:
        new_text = f"Введено текст: '{input_text}'"
    else:
        new_text = "Кнопку натиснуто! Введіть текст вище."
    # Оновлюємо лейбл, виконуючи завдання 2 (зміна тексту) та завдання 3 (зміна кольору)
    main_label.config(
        text=new_text,
        fg="yellow" # Зміна кольору тексту на жовтий (завдання 2)
    )

frame1 = tk. Frame(root, bg="#d9d9d9", padx=15, pady=15)
frame1.pack(pady=15, padx=15)

# Фрейм 2: для поля вводу та кнопки
frame2 = tk.Frame(root, bg="#cccccc", padx=15, pady=15)
frame2.pack(pady=10, padx=15)

main_label = tk. Label(
    frame1,
    text="Привіт! Створи великий зелений лейбл.",
    font=("Arial", 20, "bold"),
    fg="green", # Встановлюємо зелений колір тексту
    bg="#d9d9d9"
)
main_label.pack()


text_entry = tk.Entry(
    frame2,
    width=35,
    font=("Arial", 12),
    bd=2,
    relief=tk.SUNKEN
)
text_entry.pack(pady=10)


action_button = tk. Button(
    frame2,
    text="Оновити лейбл",
    command=update_label_content,
    font=("Arial", 12),
    bg="#007bff",
    fg="white",
    activebackground="#0056b3"
)
action_button.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()