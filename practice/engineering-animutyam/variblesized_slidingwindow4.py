nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
l=0
ans=0
temp=0

for i in range(len(nums)):
    if nums[i]==0:
        temp=temp+1
    
    
    
    while(temp>k):
        if nums[l]==0:
            temp=temp-1
        l=l+1
    # print(nums[l:i+1],temp,i-l+1)
    
    ans=max(ans,i-l+1)
print(ans)