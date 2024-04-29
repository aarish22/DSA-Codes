def binarySearch(arr,x,lowerBound,upperBound):
    while lowerBound <= upperBound:
        mid=lowerBound+(upperBound-lowerBound)//2
        if(arr[mid])==x:
            return mid
        elif(arr[mid]<x):
            return (arr,x,mid+1,upperBound)
        else:
            return (arr,x,lowerBound,mid-1)
    return -1

list=[23,45,64,55,66,45,45,23]
lowerBound=0
upperBound=len(list)-1
x=55
result=binarySearch(list,x,lowerBound,upperBound)

print(result)