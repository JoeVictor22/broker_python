import random
import tkinter as tk
from pprint import pprint


def select_choice():
    global choose
    for op in choose:

        pprint(op.get())

def create_choices():
    global topics, choose
    choose = []
    topics = get_topics()

    row = OPTIONS_ROW
    col = 0
    for value in topics:
        var = tk.BooleanVar()
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

OPTIONS_ROW = 5
TEXT_COL = 4
topics = get_topics()
choose = []
master = tk.Tk()

create_choices()
button_reset = tk.Button(master, text="Resetar tópicos", command=create_choices,bd=5)
button_reset.grid(row=0, column=TEXT_COL+1, columnspan=1)


text_box = tk.Text(
    master,
    height=12,
    width=40
)
message = "oaskdoakjgpaojapofhjkasdpokspf ohgklsdjh pokhpofjh oaskdoakjgpaojapofhjkasdpokspf ohgklsdjh pokhpofjh "
text_box.grid(row = 0, column=0, columnspan=TEXT_COL, rowspan=OPTIONS_ROW)
text_box.insert('end', message)
text_box.config(state='disabled')

tk.mainloop()







