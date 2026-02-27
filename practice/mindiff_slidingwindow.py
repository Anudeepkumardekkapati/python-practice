nums=[1,2,3,4]
nums.sort()
print(nums)
k = 3
r=0
l=0
ans=float("inf")
li=len(nums)



for r in range(li):
    
    
    
    if r-l==k:
       
        l=l+1
    
    # print(nums[l:r+1])    
        
        
    if r-l+1==k:
        # print(nums[l:r+1])
        first=nums[l]
        last=nums[r]
        ans=min(ans,last-first)
print(ans)