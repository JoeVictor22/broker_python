import random
import tkinter as tk
from pprint import pprint


def select_choice():
    global choose
    pprint(choose.)

def create_choices():
    global topics, choose
    choose = []
    topics = get_topics()

    row = 3
    col = 0
    for value in topics:
        var = tk.IntVar()
        choose.append(var)
        c = tk.Checkbutton(master, text=value, variable=var, onvalue=1, offvalue=0, command=select_choice)

        if col == 4:
            row += 1
            col = 0

        c.grid(row=row, column=col, columnspan=1)
        col+=1

def get_topics():
    topics = []
    for _ in range(random.randint(0,15)):
        topics.append(f"option_{random.randint(0,9999)}")

    return topics

topics = get_topics()
choose = []
master = tk.Tk()

create_choices()
button_reset = tk.Button(master, text="Resetar", command=create_choices,bd=5)
button_reset.grid(row=0, column=0, columnspan=3)

tk.mainloop()







