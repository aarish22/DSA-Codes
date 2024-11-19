def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)-1):
            if arr[min_idx] > arr[j]:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  
                
my_list = [13,46,24,52,20,9]
output = selection_sort(my_list)
print(output)

    