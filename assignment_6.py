import random
import time
from tkinter import *
import random
from tkinter import simpledialog
import math

root = Tk()


# fun with sorting


def is_sorted(l):
    last = None
    for o in l:
        if last:
            if o < last:
                return False
            last = o
        else:
            last = o
    return True


def bogo(l):
    while not is_sorted(l):
        random.shuffle(l)
    return l


def rlistn(n):
    new_list = []
    for i in range(n):
        new_list.append(random.randint(1, 100))
    return new_list


# i think this is selection sort
def my_sort(l):
    left = []
    for e in l:
        if left:
            i = len(left)
            while True:
                if i < 0:
                    left.insert(0, e)
                    break

                m = left[i - 1]

                if e > m:
                    left.insert(i, e)
                    break
                else:
                    i -= 1
        else:
            left.append(e)

    return left


def insertion_sort(unsorted_list):
    sorted_list = [unsorted_list.pop(0)]
    for i in unsorted_list:
        lowest_index = 0
        for index, value in enumerate(sorted_list):
            if i > value:
                lowest_index = index + 1
        sorted_list.insert(lowest_index, i)
    return sorted_list


def sort():
    while not is_sorted(map(lambda jk: int(jk.cget("text")), all_labels)):
        i = 0
        while i < len(all_labels) - 1:
            for l in all_labels:
                l.configure(background="gray")

            compare_1 = all_labels[i]
            compare_2 = all_labels[i + 1]

            compare_1.configure(background="green")
            compare_2.configure(background="green")

            if int(compare_1.cget("text")) > int(compare_2.cget("text")):
                x_1 = compare_1.winfo_x()
                y_1 = compare_1.winfo_y()

                x_2 = compare_2.winfo_x()
                y_2 = compare_2.winfo_y()

                x_dist = (x_2 - x_1) / 2
                y_dist = (y_2 - y_1) / 2

                for aakakaka in range(2):
                    x_1 += x_dist
                    y_1 += y_dist
                    compare_1.place(x=x_1, y=y_1)
                    root.update()
                    #root.after(10)

                for aakakaka2 in range(2):
                    x_2 -= x_dist
                    y_2 -= y_dist
                    compare_2.place(x=x_2, y=y_2)
                    root.update()
                    #root.after(10)

                all_labels[i] = compare_2
                all_labels[i + 1] = compare_1

            root.update()
            #root.after(10)

            i += 1



# Generate 100 random integers ranging between 1 and 100
values = []
for i in range(100):
    values.append(random.randint(1, 100))


# Put those integers into labels, 5 rows of 20 labels
all_labels = []
for i in range(5):
    for j in range(20):
        l = Label(root, text=values.pop(0), background="gray", height=2, width=4, font=("Courier", 12))
        l.place(x=50 + (50 * j), y=50 + (i * 50))
        all_labels.append(l)



# test_list = rlistn(9)

# c = None
#
# while True:
#     if c:
#
#     else:
#         c = l.pop(0)
#     d = l.pop(0)
#     input()

#print(test_list)

#before = time.time()
#print(bogo(list(test_list)))
#print("bogo took {} seconds".format(time.time() - before))

#print(test_list)

#before = time.time()
#print(my_sort(list(test_list)))
#print("my sort took {} seconds".format(time.time() - before))

sort_button = Button(root, text="Sort", command=sort)
sort_button.place(x=50, y=310)


root.title("Animated Sort")
root.resizable(False, False)
root.geometry("1100x350")
root.mainloop()
