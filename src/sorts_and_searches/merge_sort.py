def merge_sort(lst):
    if len(lst) > 1:
        print(lst)
        mid = len(lst) // 2  # Calculate the midpoint of array
        left_sub = lst[:mid]
        right_sub = lst[mid:]
        merge_sort(left_sub)  # Continue splitting left side of array
        merge_sort(right_sub)  # Now split right side of array
        merge(left_sub, right_sub, lst)  # Compare and merge
        # return lst  # Return sub_lst after all sorting and merging
    else:
        return  # Base case

def merge(l_sub, r_sub, sublst):
    temp = []
    l_ptr, r_ptr = 0, 0  # Pointers for traversing subarrays
    while l_ptr < len(l_sub) and r_ptr < len(r_sub):  # While there are still nums in either array
        num1 = l_sub[l_ptr]  # Number from left subarray
        num2 = r_sub[r_ptr]  # Number from right subarray

        # Compare nums, append the smallest of the two
        if num1 < num2:
            # Swap elements within sublst
            temp.append(num1)
            l_ptr += 1  # Increment pointer to point to next number
        else:
            # Swap elements within sublst
            temp.append(num2)
            r_ptr += 1  # Increment pointer to point to next number

    # If there are nums remaining in left subarray, append the rest to sub
    if l_ptr < len(l_sub):
        for num in l_sub[l_ptr:]:
            temp.append(num)

    # If there are nums remaining in right subarray, append the rest to sub
    if r_ptr < len(r_sub):
        for num in r_sub[r_ptr:]:
            temp.append(num)

    # Now make sublst the same as temp
    for index, num in enumerate(temp):
        sublst[index] = num
    return sublst


# my_list = [7, 3, 8, 5, 4, 2, 6, 1]
my_list = [1, 3, 2, 1]
sub_list = my_list
# print(merge_sort(my_list))  # This is used when the merge_sort function actually returns something
merge_sort(my_list)
print(my_list)  # Use this when merge_sort doesn't return anything