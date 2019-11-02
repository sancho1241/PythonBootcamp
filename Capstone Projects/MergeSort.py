from random import randint

"""
Capstone Project from the Python Bootcamp by Jose Portilla
Merge Sort
"""


def merge_sort(array, left_index, right_index):

    if left_index<right_index: # as long as there are at least two elements
        middle = int((left_index + right_index) / 2)
        merge_sort(array, left_index, middle)
        merge_sort(array, middle+1, right_index)
        merge_arrays(array, left_index, middle, right_index)

def merge_arrays(array, left_index, middle, right_index):
    #create temp arrays

    left_array = [0] * (middle-left_index+1)
    right_array = [0] * (right_index-middle)

    left_array = array[left_index:middle+1]
    right_array = array[middle+1:]

    counter_left=0
    counter_right=0
    array_counter=left_index

    while counter_left < len(left_array) and counter_right < len(right_array):
        if (left_array[counter_left] <= right_array[counter_right]):
            array[array_counter] = left_array[counter_left]
            counter_left+=1
        else:
            array[array_counter] = right_array[counter_right]
            counter_right+=1
        array_counter+=1

    while counter_left < len(left_array):
        array[array_counter]=left_array[counter_left]
        counter_left+=1
        array_counter+=1

    while   counter_right < len(right_array):
        array[array_counter]=right_array[counter_right]
        counter_right+=1
        array_counter+=1


# create list with random numbers using list comprehension
my_list = [randint(1, 100) for x in range(10)]
print("unsorted list: {}".format(my_list))
# merge sort the list
merge_sort(my_list, 0, len(my_list)-1)
print("sorted list: {}".format(my_list))
