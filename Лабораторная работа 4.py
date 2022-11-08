import tkinter as tk
from Generation import gen


def clicked():
    txt.delete(0, 30)
    p = str(gen())
    u = p[:5] + "-" + p[5:9] + "-" + p[9:13]
    txt.insert(0, u)


window = tk.Tk()
window.title("Генератор ключей NFS")
window.geometry('700x394')
window.resizable(width=False, height=False)
window.image = tk.PhotoImage(file="m_NFS.png")
bg_logo = tk.Label(window, image=window.image)
bg_logo.grid(row=0, column=0)
txt = tk.Entry(window, width=30)
txt.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
label = tk.Label(text="Ваш ключ:")
label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
btn = tk.Button(window, text="Сгенерировать ключ", command=clicked)
btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()
