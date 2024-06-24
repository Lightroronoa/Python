from tkinter import *
import math


def btn_click(num):
    global eqn_text

    eqn_text += str(num)

    eqn_lable.set(eqn_text)


def calculate():
    global eqn_text

    try:
        total = str(eval(eqn_text))

        eqn_lable.set(total)

        eqn_text = total

    except NameError:
        if "π" in eqn_text:
            eqn_text = eqn_text.replace("π", f"{math.pi}")
            calculate()

    except SyntaxError:

        eqn_lable.set("Syntax Error")

        eqn_text = ""

    except ZeroDivisionError:

        eqn_lable.set("Indeterminant")

        eqn_text = ""


def clear():

    global eqn_text

    eqn_lable.set("")

    eqn_text = ""

windows = Tk()
windows.title("Calculator")
windows.geometry("350x450")
windows.configure(bg='black')

eqn_text = ""
eqn_lable = StringVar()
lable = Label(
    windows,
    textvariable=eqn_lable,
    font=("Arial", 20),
    bg="lightgray",
    width=30,
    height=2,
)
lable.pack()

frame = Frame(windows)
frame.pack()

btn1 = Button(
    frame,
    text="1",
    command=lambda: btn_click(1),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn1.grid(row=0, column=0)


btn2 = Button(
    frame,
    text="2",
    command=lambda: btn_click(2),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0,
    bg="lightgray",
)
btn2.grid(row=0, column=1)

btn3 = Button(
    frame,
    text="3",
    command=lambda: btn_click(3),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray")
btn3.grid(row=0, column=2)


btn4 = Button(
    frame,
    text="4",
    command=lambda: btn_click(4),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn4.grid(row=1, column=0)


btn5 = Button(
    frame,
    text="5",
    command=lambda: btn_click(5),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn5.grid(row=1, column=1)

btn6 = Button(
    frame,
    text="6",
    command=lambda: btn_click(6),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn6.grid(row=1, column=2)

btn7 = Button(
    frame,
    text="7",
    command=lambda: btn_click(7),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray",
)
btn7.grid(row=2, column=0)

btn8 = Button(
    frame,
    text="8",
    command=lambda: btn_click(8),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray",
)
btn8.grid(row=2, column=1)

btn9 = Button(
    frame,
    text="9",
    command=lambda: btn_click(9),
    height=4,
    width=10,
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn9.grid(row=2, column=2)

btn0 = Button(
    frame,
    text="0",
    height=4,
    width=10,
    command=lambda: btn_click(0),
    relief="sunken",
    borderwidth=0, bg="lightgray"
)
btn0.grid(row=3, column=0)

btn_add = Button(
    frame,
    text="+",
    command=lambda: btn_click("+"),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_add.grid(row=0, column=3)

btn_sub = Button(
    frame,
    text="-",
    command=lambda: btn_click("-"),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_sub.grid(row=1, column=3)

btn_mul = Button(
    frame,
    text="*",
    command=lambda: btn_click("*"),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_mul.grid(row=2, column=3)

btn_fr = Button(
    frame,
    text="(",
    command=lambda: btn_click("("),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_fr.grid(row=4, column=0)

btn_bk = Button(
    frame,
    text=")",
    command=lambda: btn_click(")"),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_bk.grid(row=4, column=1)


btn_dot = Button(
    frame,
    text=".",
    command=lambda: btn_click("."),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_dot.grid(row=3, column=1)

btn_div = Button(
    frame,
    text="/",
    command=lambda: btn_click("/"),
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_div.grid(row=3, column=2)


btn_pi = Button(
    frame,
    text="π",
    command=lambda: btn_click("π"),
    height=4,
    width=10,
    bg="darkgray",
    borderwidth=0,
    relief="sunken",
)
btn_pi.grid(row=4, column=2)

btn_equal = Button(
    frame,
    text="=",
    command=calculate,
    height=4,
    width=10,
    bg="#cc5500",
    borderwidth=0,
    relief="sunken",
    activebackground="#FFAE42"
)
btn_equal.grid(row=4, column=3)

btn_clear = Button(
    frame,
    text="C",
    command=clear,
    height=4,
    width=10,
    bg="darkgray",
    relief="sunken",
    borderwidth=0,
)
btn_clear.grid(row=3, column=3)


windows.mainloop()
