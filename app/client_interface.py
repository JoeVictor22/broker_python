import tkinter as tk
from pprint import pprint


def select_choice():
    global choose
    for op in choose:

        pprint(op.get())


def create_choices():
    global topics, choose
    choose = []

    row = OPTIONS_ROW
    col = 0
    for value in topics:
        var = tk.BooleanVar()
        choose.append(var)
        c = tk.Checkbutton(
            master,
            text=value,
            variable=var,
            onvalue=1,
            offvalue=0,
            command=select_choice,
        )

        if col == 4:
            row += 1
            col = 0

        c.grid(row=row, column=col, columnspan=1)
        col += 1


OPTIONS_ROW = 5
TEXT_COL = 4
topics = []
choose = []
master = tk.Tk()
client = None
buffer = []
# message_len = 3

def create_message(messages):
    final_txt = ""
    for idx, message in enumerate(messages):
        final_txt += f"{message}\n"
    return final_txt



def start(cliente):
    global client, topics, buffer
    client = cliente
    topics = client.broker_topics
    create_choices()

    button_reset = tk.Button(
        master, text="Resetar tópicos", command=create_choices, bd=5
    )
    button_reset.grid(row=0, column=TEXT_COL + 1, columnspan=1)

    text_box = tk.Text(master, height=12, width=40)
    text_box.grid(row=0, column=0, columnspan=TEXT_COL, rowspan=OPTIONS_ROW)

    def set_text(buffer):
        text_box.delete(1.0, "end")
        text_box.insert("end", create_message(buffer))

    while True:
        topics = client.broker_topics
        client.update()
        master.update()
        client.set_topics(choose)
        set_text(cliente.buffer)
