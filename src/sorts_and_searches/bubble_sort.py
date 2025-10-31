def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

my_list = [2, 8, 5, 3, 9, 4, 1]
print(f"My list before sorting: f{my_list}")
bubble_sort(my_list)
print(f"My list after sorting: f{my_list}")