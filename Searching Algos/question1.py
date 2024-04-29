## time complexity O(n)
## space complexity O(1)
def linearSearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1


list=[20,45,27,47,55,67,75,88,90]
x=67
result= linearSearch(list,x)
print(result)