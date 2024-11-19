def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    return arr
my_list = [12, 20, 9, 6, 15, 5]
output = insertionSort(my_list)
print(output)
