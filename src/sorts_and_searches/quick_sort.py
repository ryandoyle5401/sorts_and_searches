import math


def quick_sort(lst, start, end):
    pivot = select_pivot(start, end)
    partition(lst, pivot, end)

def partition(lst, pivot, end):
    lst[pivot], lst[end] = lst[end], lst[pivot]  # Swap pivot with last element in list
    pivot = end  # Set pivot equal to end so the index of pivot is up to date
    i = -1  # Index used as a boundary between elements less than pivot and elements greater than pivot
    j = 0  # Index used to keep track of the last element scanned in list

    while j < end:
        if lst[j] <= lst[pivot]:
            i += 1  # Increment the boundary
            lst[j], lst[i] = lst[i], lst[j]
        j += 1  # Increment to scan next element in list

    i += 1
    lst[pivot], lst[i] = lst[i], lst[pivot]  # Swap pivot into its final position
    # print(lst)  # Used to verify that pivot gets swapped into correct final position



def select_pivot(start, end):
    return math.floor((start + end) / 2)  # Select middle element as pivot

my_list = [8, 2, 4, 7, 1, 3, 9, 6, 5]
quick_sort(my_list, 0, len(my_list) - 1)