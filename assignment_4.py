import random
import time

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



test_list = rlistn(9)

# c = None
#
# while True:
#     if c:
#
#     else:
#         c = l.pop(0)
#     d = l.pop(0)
#     input()

print(test_list)

before = time.time()
print(bogo(list(test_list)))
print("bogo took {} seconds".format(time.time() - before))

print(test_list)

before = time.time()
print(my_sort(list(test_list)))
print("my sort took {} seconds".format(time.time() - before))
