def insertionSort(arr):
    temp = 0
    for i in range(len(arr)):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j = j - 1
    return arr

my_list =[12,20,9,6,15,5]
ouput = insertionSort(my_list)
print(ouput)