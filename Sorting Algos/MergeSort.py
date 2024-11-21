def merge_sort1(arr):
    if len(arr) > 1:
        mid_idx = len(arr) // 2
        left_arr = arr[:mid_idx]
        right_arr = arr[mid_idx:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i, j, k = 0, 0, 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
mylist = [12, 46, 57, 68, 64]
merge_sort1(mylist)
print(mylist)  
