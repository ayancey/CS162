from tkinter import *
import random

root = Tk()

sorted_labels = []
all_labels = []


def shuffle():
    global all_labels
    global sorted_labels

    for l in sorted_labels:
        l.destroy()
    for l in all_labels:
        l.destroy()

    all_labels = []
    sorted_labels = []

    # Generate 100 random integers ranging between 1 and 100
    values = []
    for i in range(100):
        values.append(random.randint(1, 100))

    # Put those integers into labels, 5 rows of 20 labels
    for i in range(5):
        for j in range(20):
            l = Label(root, text=values.pop(0), background="gray", height=2, width=4, font=("Courier", 12))
            l.place(x=50 + (50 * j), y=50 + (i * 50))
            all_labels.append(l)


def reorder():
    global all_labels
    global sorted_labels

    # this actually sucks

    combined_labels = list(map(lambda l: ("green", l.cget("text")), sorted_labels)) + list(map(lambda l: ("gray", l.cget("text")), all_labels))

    for l in sorted_labels:
        l.destroy()
    for l in all_labels:
        l.destroy()

    all_labels = []
    sorted_labels = []

    for i in range(5):
        for j in range(20):
            old_label = combined_labels.pop(0)
            l = Label(root, text=old_label[1], background=old_label[0], height=2, width=4, font=("Courier", 12))
            l.place(x=50 + (50 * j), y=50 + (i * 50))
            if old_label[0] == "green":
                sorted_labels.append(l)
            else:
                all_labels.append(l)


def sort():
    global sorted_labels
    global all_labels

    sort_button.configure(state=DISABLED)
    shuffle_button.configure(state=DISABLED)
    demo_mode_checkbox.configure(state=DISABLED)

    sort_label.configure(text="Sorting list...")

    while all_labels:
        # Find lowest value in big stack
        lowest_label = None

        for l in all_labels:
            if lowest_label:
                if l.cget("text") < lowest_label.cget("text"):
                    lowest_label = l
            else:
                lowest_label = l

        # put it in little stack
        all_labels.remove(lowest_label)
        sorted_labels.append(lowest_label)

        # Color the lowest label gold
        lowest_label.configure(background="gold")

        root.update()

        if demo.get():
            root.after(500)
        else:
            root.after(50)
        reorder()

    sort_label.configure(text="List successfully sorted!")
    sort_button.configure(state=NORMAL)
    shuffle_button.configure(state=NORMAL)
    demo_mode_checkbox.configure(state=NORMAL)


# Initial shuffle
shuffle()

# Set up buttons, labels, etc...
sort_button = Button(root, text="Sort", command=sort)
sort_button.place(x=50, y=310)

sort_label = Label(root, text="<-- Sort list", font=("Courier", 12))
sort_label.place(x=100, y=310)

demo = IntVar()
demo_mode_checkbox = Checkbutton(root, text="Demo mode (animate slower)", variable=demo)
demo_mode_checkbox.place(x=50, y=15)

shuffle_button = Button(root, text="Shuffle", command=shuffle)
shuffle_button.place(x=1000, y=20)

root.title("Animated Sort")
root.resizable(False, False)
root.geometry("1100x350")
root.mainloop()
