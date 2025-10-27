my_list = [3, 7, 8, 5, 4, 2, 6, 1]
#print(my_list[:4])  # Note, stop is exclusive

# ---------------------------------------------- This works at splitting the arrays recursively
# def merge_sort(lst):
#     if len(lst) > 1:
#         mid = len(lst) // 2  # Calculate the midpoint of array
#         left_sub = lst[:mid]
#         right_sub = lst[mid:]
#         print(f"left sub {left_sub}")
#         print(f"right sub {right_sub}")
#         merge_sort(left_sub)
#         merge_sort(right_sub)


def merge_sort(lst):
    sub_lst = []
    if len(lst) > 1:
        mid = len(lst) // 2  # Calculate the midpoint of array
        left_sub = lst[:mid]
        right_sub = lst[mid:]
        print(f"left sub {left_sub}")
        print(f"right sub {right_sub}")
        merge_sort(left_sub)
        merge_sort(right_sub)
        sub_lst = merge(left_sub, right_sub, sub_lst)
        return sub_lst

def merge(l_sub, r_sub, sub):
    l_ptr, r_ptr = 0  # Pointers for traversing subarrays
    while l_ptr < len(l_sub) or r_ptr < len(r_sub):  # While there are still nums in either array
        num1 = l_sub[l_ptr]  # Number from left subarray
        num2 = r_sub[r_ptr]  # Number from right subarray

        # Compare nums, append the smallest of the two
        if num1 < num2:
            sub.append(num1)
        else:
            sub.append(num2)

    # If there are nums remaining in left subarray, append the rest to sub
    if l_ptr < len(l_sub):
        for num in l_sub[l_ptr:]:
            sub.append(num)

    # If there are nums remaining in right subarray, append the rest to sub
    if r_ptr < len(r_sub):
        for num in r_sub[r_ptr:]:
            sub.append(num)
    return sub

merge_sort(my_list)