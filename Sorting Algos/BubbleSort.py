def bubbleSort(arr):
    temp = 0
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return print(arr)
                        
my_list = [13,46,24,52,20,9]
bubbleSort(my_list)