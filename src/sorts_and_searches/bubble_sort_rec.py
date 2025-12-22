def bubble_sort_rec(lst, sorted_lst):
    n = len(lst)
    if n <= 1:
        sorted_lst.insert(0, lst[0])
        return sorted_lst
    else:
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        sorted_lst.insert(0, lst[-1])
        return bubble_sort_rec(lst[:n-1], sorted_lst)

my_list = [4, 3, 2, 1]
print(f"My list before sorting: {my_list}")
my_new_list = bubble_sort_rec(my_list, [])
print(f"My list after sorting: {my_new_list}")








def bubble_sort_rec(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        return bubble_sort_rec(lst[:n-1])

my_list = [4, 3, 2, 1]
print(f"My list before sorting: {my_list}")
my_new_list = bubble_sort_rec(my_list)
print(f"My list after sorting: {my_new_list}")