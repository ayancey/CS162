import tkinter
from assignment_1 import Radio

window = tkinter.Tk()

mode = tkinter.IntVar()


def change_mode():
    print(mode.get())


my_radio = Radio()


tkinter.Radiobutton(window, text="FM", variable=mode, value=0, command=change_mode).pack()
tkinter.Radiobutton(window, text="AM", variable=mode, value=1, command=change_mode).pack()
tkinter.Radiobutton(window, text="SAT", variable=mode, value=2, command=change_mode).pack()
tkinter.Radiobutton(window, text="AUX", variable=mode, value=3, command=change_mode).pack()


tkinter.mainloop()
