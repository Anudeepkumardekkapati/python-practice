def fun(arr,target):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if arr[mid]>target:
            r=mid-1
        else:
            l=mid+1
    if (r== -1):
        return 'a'
    return arr[r]








arr=['c','e','g','k','y']
target='b'
ans=fun(arr,target)
print(ans)
