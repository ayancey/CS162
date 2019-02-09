from tkinter import *
import random
from tkinter import simpledialog
import math

root = Tk()

# Generate 100 random integers ranging between 1 and 100
values = []
for i in range(100):
    values.append(random.randint(1, 100))
values = sorted(values)

# Put those integers into labels, in order, 5 rows of 20 labels
all_labels = []
for i in range(5):
    for j in range(20):
        l = Label(root, text=values.pop(0), background="gray", height=2, width=4, font=("Courier", 12))
        l.place(x=50 + (50 * j), y=50 + (i * 50))
        all_labels.append(l)


def search():
    v = simpledialog.askinteger("Input", "What would you like to search for?", parent=root, minvalue=1, maxvalue=99)
    candidate_labels = list(all_labels)

    def update_colors():
        for l in all_labels:
            l.configure(background="gray")
        for l in candidate_labels:
            l.configure(background="green")

    update_colors()

    while True:
        # If value is not found, make everything red
        if len(candidate_labels) == 1:
            for l in all_labels:
                l.configure(background="red")
            break

        update_colors()

        # Find the label in the middle of the list, always rounds up
        slice_index = math.ceil(len(candidate_labels) / 2)
        l = candidate_labels[slice_index]
        val = l.cget("text")
        l.configure(background="blue")

        # Animate
        root.update()
        root.after(1000)

        # Split the list in half based on if the value is greater than or less than the search variable
        if val > v:
            candidate_labels = candidate_labels[:slice_index]
        elif val < v:
            candidate_labels = candidate_labels[slice_index:]
        else:
            candidate_labels = [l]
            update_colors()
            root.update()
            break

        # Animate
        update_colors()
        root.update()
        root.after(1500)


b = Button(root, text="Search", command=search)
b.place(x=400, y=350)


root.geometry("1100x400")
root.mainloop()
