def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1): 
        for j in range(i):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  

my_list = [13, 46, 24, 52, 20, 9]
sorted_list = bubbleSort(my_list)
print("Sorted List:", sorted_list)