import tkinter as tk


# topics = get_topics()
from pprint import pprint

def create_form():
    create_choices(topics)
    button = tk.Button(master, text="Show", command=create_choices,bd=5)
    button.grid(row=2, column=1, columnspan=2)


def select_choice():
    global choose
    pprint(choose)

def create_choices(choices):
    global choose
    choose = []
    for idx, value in enumerate(choices):
        var = tk.IntVar()
        choose.append(var)
        c = tk.Checkbutton(master, text=value, variable=var, onvalue=1, offvalue=0, command=select_choice)
        c.grid(row=idx+3, column=0, columnspan=2)


topics = ["m1", "m2"]
choose = []
master = tk.Tk()
tk.mainloop()
create_form()



