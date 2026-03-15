def fun(arr,target):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif (arr[mid]>target):
            r=mid-1
        elif(arr[mid]<target):
            l=mid+1
        
        
        
        
        
        
        
    return -1

arr=[1,5,8,12,14,16,18,20,27]
target=200

ans=fun(arr,target)
print(ans)