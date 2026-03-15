

def left(nums,target):
    l=0
    r=len(nums)-1
    
    
    while(l<=r):
        mid=(r+l)//2
        if nums[mid]==target:
            r=mid-1
        elif(nums[mid]>target):
            r=mid-1
        else:
            l=mid+1
    if l>=len(nums):
        return -1
      
    if nums[l]!=target:
        return -1
     
    return l
    
  
def right(nums,target):
    l=0
    r=len(nums)-1
    while(l<=r):
        mid=(r+l)//2
        if nums[mid]==target:
            l=mid+1
        elif(nums[mid]>target):
            r=mid-1
        else:
            l=mid+1
    if r<0:
        return -1
    if nums[r]!=target:
        return -1
    return r
    
    
nums = []
target = 0
ans=left(nums,target)
ans1=right(nums,target)

print([ans,ans1])
        