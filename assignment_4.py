from tkinter import *
import time
import random

root = Tk()

text_elements = []


lowest_val = StringVar()
lowest_val.set("Lowest value is: Unknown")


def find_smallest():
    # Find the text box with the lowest value, display it in the label, remove it from the list
    global text_elements
    global lowest_val

    smallest_element = None
    smallest_value = None

    for t in text_elements:
        i = int(t.get("1.0", END).strip())

        if smallest_element:
            if i < smallest_value:
                smallest_element = t
                smallest_value = i
        else:
            smallest_element = t
            smallest_value = i

    if smallest_element:
        smallest_element.configure(background='black')
        text_elements.remove(smallest_element)
        lowest_val.set("Lowest value is: {}".format(smallest_value))


one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    t = Text(root, height=2, width=30)
    t.place(x=25, y=40 + (i * 40))
    t.insert(END, one_to_ten.pop(random.randint(0,len(one_to_ten)-1)))
    text_elements.append(t)


lowest_label = Label(root, textvariable=lowest_val)
lowest_label.place(x=400, y=150)

b = Button(root, text="Find smallest", command=find_smallest)
b.place(x=400, y=200)

root.geometry("640x480")
root.mainloop()
