nums = [-2,-1,-1,1,2,3]



def pos(nums):
    
    l=0
    count=0
    r=len(nums)-1
    while(l<=r):
        mid=(r+l)//2
        if nums[mid]>0:
            l=mid+1
            count=count+1
    return count



nums = [-2,-1,-1,1,2,3]
ans=pos(nums)
print(ans,ans)