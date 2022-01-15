
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from DVA_C01_bank import *
from DVA_C01_bank import AWSQuestionBank

root = Tk()
width = 1000
height = 400
root.geometry(f'{width}x{height}')

qb = AWSQuestionBank()
db = qb.query()
user_ans_list = {}

font_q = ("Helvatica", 13, 'bold')
font_a = ("Helvatica", 11)


def forward(qid):   # qid = question_id

    global current_qid
    global user_ans

    current_qid = IntVar()
    current_qid.set(qid)

    global label_q
    global btn_next
    global btn_prev

    btn_prev = Button(root, text="Previous", command=lambda: backward(qid-1))
    btn_prev.grid(row=6, column=1, padx=10, ipadx=10, sticky=E+S)

    if qid == len(db):
        btn_next = Button(root, text="Next", state=DISABLED)
        btn_next.grid(row=6, column=2, padx=10, ipadx=20, sticky=E+S)
    else:
        btn_next = Button(root, text="Next", command=lambda: forward(qid + 1))
        btn_next.grid(row=6, column=2, padx=10, ipadx=20, sticky=E+S)

    question = qb.query(qid)
    question = list(question[0])

    ANSWERS = [(question[2], "A"),
               (question[3], "B"),
               (question[4], "C"),
               (question[5], "D"),
               (question[6], "E")]

    user_ans = StringVar()
    user_ans.set(None)

    label_q = Label(root, text=f'{str(question[0])}) {question[1]}', wraplength=width,
                    font=font_q)
    label_q.grid(row=0, column=0, columnspan=3, sticky=W+N)

    for idx, (response, value) in enumerate(ANSWERS):
        if response[6] == "":
            pass
        else:
            radio_r = Radiobutton(root, value=value, variable=user_ans, text=f"{value}) {response}",
                                  wraplength=width-200, font=font_a)
            radio_r.grid(row=idx, column=0, sticky=W)
            print(idx, (response, value))


def backward(qid):

    global current_qid
    global user_ans

    current_qid = IntVar()
    current_qid.set(qid)

    user_ans = StringVar()
    user_ans.set(None)

    global label_q
    global btn_next
    global btn_prev

    btn_next = Button(root, text="Next", command=lambda: forward(qid+1))
    btn_next.grid(row=6, column=2, padx=10, ipadx=20, sticky=E+S)

    if qid == 1:
        btn_prev = Button(root, text="Previous", state=DISABLED)
        btn_prev.grid(row=6, column=1, padx=10, ipadx=10, sticky=E+S)
    else:
        btn_prev = Button(root, text="Previous", command=lambda: backward(qid-1))
        btn_prev.grid(row=6, column=1, padx=10, ipadx=10, sticky=E+S)

    question = qb.query(qid)
    question = list(question[0])

    ANSWERS = [(question[2], "A"),
               (question[3], "B"),
               (question[4], "C"),
               (question[5], "D"),
               (question[6], "E")]

    label_q = Label(root, text=f'{str(question[0])}) {question[1]}', wraplength=width,
                    font=font_q)
    label_q.grid(row=0, column=0, columnspan=3, sticky=W+N)

    for idx, (response, value) in enumerate(ANSWERS):
        if response[6] == "":
            pass
        else:
            radio_r = Radiobutton(root, value=value, variable=user_ans, text=f"{value}) {response}",
                                  wraplength=width-200, font=font_a)
            radio_r.grid(row=idx, column=0, sticky=W)


def save_answer(value):

    id = current_qid.get()
    user_ans_list[id] = value
    print(user_ans_list)


def start():
    btn_start.destroy()
    forward(1)


# Labels
label_q = Label(root, text='Welcome to the AWS practice exam!\nThis is a mock test to help you prepare towards your actual AWS exam.\nI made this programme because the exam price is quite yikes!',
                font=font_q)
label_q.grid(row=0, column=1, ipady=30, columnspan=3)

# Buttons
btn_start = Button(root, text="Start test now", command=start)
btn_start.grid(row=6, column=2, padx=10, ipadx=20, sticky=E+S)

btn_ans = Button(root, text="Answer", command=lambda: save_answer(user_ans.get()))
btn_prev = Button(root, text="Previous", command=lambda: backward(0))
btn_next = Button(root, text="Next", command=lambda: forward(1))

btn_ans.grid(row=6, column=0, padx=10, ipadx=10, sticky=E+W+S+N)
#btn_prev.grid(row=6, column=1, padx=10, ipadx=10, sticky=E+S)
#btn_next.grid(row=6, column=2, padx=10, ipadx=20, sticky=E+S)

qb.query()

root.mainloop()