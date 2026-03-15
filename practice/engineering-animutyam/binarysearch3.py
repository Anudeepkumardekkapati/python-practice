def pos(nums):
    l=0
    r=len(nums)-1
    while(l<=r):
        mid=(l+r)//2
        if nums[mid]==0:
            r=mid-1
        elif(nums[mid]>0):
            r=mid-1
        else:
            l=mid+1
    return(l)
    
    
def neg(nums):
    l=0
    r=len(nums)-1
    while(l<=r):
        mid=(r+l)//2
        if (nums[mid]==1):
            r=mid-1
        elif(nums[mid]>1):
            r=mid-1
        else:
            l=mid+1
    return(len(nums)-l)
        
nums = [-2,-5,-1,-1,1,2,3,6,7,9]
ans1=pos(nums)
ans2=neg(nums)
print(max(ans1,ans2))