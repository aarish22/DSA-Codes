def selectionSort(arr):
    temp = 0
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i,len(arr)):
            if arr[min] > arr[j]:
                temp = arr[min]
                arr[min] = arr[j]
                arr[j] = temp
    return arr  
                
my_list = [13,46,24,52,20,9]
output = selectionSort(my_list)
print(output)
