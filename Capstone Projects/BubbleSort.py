from random import randint

"""
This scripts creates a bubble sort algorithm
"""


def bubble_sort(array):
    unsorted = True
    while unsorted:
        unsorted = False
        for x in range(len(array)):
            if (x + 1) != len(array) and array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                unsorted = True
        # print (list)


# create list with random numbers using list comprehension
my_list = [randint(1, 100) for x in range(10)]
print("unsorted list: {}".format(my_list))
# bubble sort the list
bubble_sort(my_list)
print("sorted list: {}".format(my_list))
