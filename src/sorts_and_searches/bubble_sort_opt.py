def bubble_sort_optimized(lst):
    n = len(lst)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            print("Breaking early")
            break
my_list = [3, 2, 1]
print(f"My list before sorting: {my_list}")
bubble_sort_optimized(my_list)
print(f"My list after sorting: {my_list}")