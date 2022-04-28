import tkinter as tk

# WINDOW = tk.Tk()


limite = 200

def show_values():

    limite = input.get()

    print(f"{w.get()}, {input.get()}")


master = tk.Tk()
w = tk.Scale(master, from_=0, to=limite,length=600, tickinterval=10, orient=tk.HORIZONTAL)
w.pack()
label = tk.Label(master, text="Valor")
label.pack(side=tk.LEFT)
input = tk.Entry(master, bd =5)
input.pack(side = tk.RIGHT)

tk.Button(master, text='Show', command=show_values).pack()

tk.mainloop()