def TargetSearch(arr,x):
    lower=0
    upper=len(arr)-1
    while(lower<=upper):
        if(arr[lower]+arr[upper]==x):
            return lower,upper
        elif(arr[lower]+arr[upper]>=x):
            upper=upper-1
        else:
            lower=lower+1
    return -1
        
my_list=[20,40,60,80,90,120,240]
target=210
result=TargetSearch(my_list,target)
print(result)