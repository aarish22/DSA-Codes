def searchArray(arr,target):
    m=len(arr)
    if m==0:
        return False
    n=len(arr[0])
    left,right=0,m*n-1
    while left<=right:
        mid=left+(right-left)//2
        mid_element=arr[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target < mid_element:
            right=mid-1
        else:
            left=mid+1
    return False
    
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
result=searchArray(arr,target)
print(result)