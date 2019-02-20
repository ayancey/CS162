from tkinter import *
import random
from tkinter import simpledialog
import math

root = Tk()

values = []
sorted_labels = []
all_labels = []


# def shuffle():
#     global values
#     global all_labels
#
#     # Remove previous labels
#     if all_labels:
#         for l in all_labels:
#             l.destroy()


def sort():
    global sorted_labels
    global all_labels

    lowest_label = None

    for l in all_labels:
        if lowest_label:
            if l.cget("text") < lowest_label.cget("text"):
                lowest_label = l
        else:
            lowest_label = l

    all_labels.remove(lowest_label)
    sorted_labels.append(lowest_label)

    # Set all labels to gray
    for label in all_labels:
        label.configure(background="gray")

    # Set only candidate labels to green
    for label in sorted_labels:
        label.configure(background="green")



    # v = simpledialog.askinteger("Input", "What would you like to search for?", parent=root, minvalue=1, maxvalue=99)
    # # stop if empty value
    # if not v:
    #     return
    #
    # sort_button.configure(state=DISABLED)
    # shuffle_button.configure(state=DISABLED)
    # demo_mode_checkbox.configure(state=DISABLED)
    #
    # sort_label.configure(text="Target: {}".format(v))
    #
    # candidate_labels = all_labels
    #
    # def update_colors():
    #     # Set all labels to gray
    #     for label in all_labels:
    #         label.configure(background="gray")
    #
    #     # Set only candidate labels to green
    #     for label in candidate_labels:
    #         label.configure(background="green")
    #
    # while True:
    #     # If there's only one value or less left, we couldn't find the number in the list
    #     if len(candidate_labels) <= 1:
    #         for l in all_labels:
    #             l.configure(background="red")
    #         sort_label.configure(text="Did not find target number {}".format(v))
    #         sort_button.configure(state=NORMAL)
    #         shuffle_button.configure(state=NORMAL)
    #         demo_mode_checkbox.configure(state=NORMAL)
    #         break
    #
    #     update_colors()
    #
    #     # Find the label in the middle of the list, always rounds down
    #     slice_index = math.floor(len(candidate_labels) / 2)
    #     middle_label = candidate_labels[slice_index]
    #     middle_value = middle_label.cget("text")
    #     middle_label.configure(background="blue")
    #
    #     # Animate
    #     root.update()
    #     if demo.get():
    #         root.after(1000)
    #     else:
    #         root.after(250)
    #
    #     # Split the list in half based on if the value is greater than or less than the search variable
    #     if middle_value > v:
    #         candidate_labels = candidate_labels[:slice_index]
    #     elif middle_value < v:
    #         candidate_labels = candidate_labels[slice_index:]
    #     else:
    #         # If it's not greater than, or less than, it must be equal to!
    #         candidate_labels = [middle_label]
    #         update_colors()
    #         sort_label.configure(text="Found target number {}".format(v))
    #         sort_button.configure(state=NORMAL)
    #         shuffle_button.configure(state=NORMAL)
    #         demo_mode_checkbox.configure(state=NORMAL)
    #         break
    #
    #     # Animate
    #     update_colors()
    #     root.update()
    #     if demo.get():
    #         root.after(2000)
    #     else:
    #         root.after(500)


# Generate 100 random integers ranging between 1 and 100
values = []
for i in range(100):
    values.append(random.randint(1, 100))

for i in range(5):
    for j in range(20):
        l = Label(root, text=values.pop(0), background="gray", height=2, width=4, font=("Courier", 12))
        l.place(x=50 + (50 * j), y=50 + (i * 50))
        all_labels.append(l)


# Put those integers into labels, 5 rows of 20 labels


# Set up buttons, labels, etc...
sort_button = Button(root, text="Sort", command=sort)
sort_button.place(x=50, y=310)

sort_label = Label(root, text="<-- Sort list", font=("Courier", 12))
sort_label.place(x=100, y=310)

demo = IntVar()
demo_mode_checkbox = Checkbutton(root, text="Demo mode (animate slower)", variable=demo)
demo_mode_checkbox.place(x=50, y=15)

shuffle_button = Button(root, text="Shuffle")
shuffle_button.place(x=1000, y=20)

root.title("Animated Sort")
root.resizable(False, False)
root.geometry("1100x350")
root.mainloop()
