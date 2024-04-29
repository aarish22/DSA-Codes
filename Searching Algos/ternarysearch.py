# 20,15,47,56,59,63,65,79,82
# mid1=first_index+(last_index-first_index)//3
# mid2=last_index-(last_index-first_index)//3
# mid1=2
# mid2=6
# key=79
def ternarySearch(arr, key, lower_limit, upper_limit):
    if upper_limit >= lower_limit:
        mid_1 = lower_limit + (upper_limit - lower_limit) // 3
        mid_2 = upper_limit - (upper_limit - lower_limit) // 3

        if arr[mid_1] == key:  # O(n)
            return mid_1
        if arr[mid_2] == key:
            return mid_2

        if key < arr[mid_1]: # O(n/3)
            return ternarySearch(arr, key, lower_limit, mid_1 - 1)
        elif key > arr[mid_2]:
            return ternarySearch(arr, key, mid_2 + 1, upper_limit)
        else:
            return ternarySearch(arr, key, mid_1 + 1, mid_2 - 1)

    return -1

my_list = [15, 20, 47, 56, 59, 63, 65, 79, 82]
target = 82
upper_limit = len(my_list) - 1
lower_limit = 0
print(ternarySearch(my_list, target, lower_limit, upper_limit))
