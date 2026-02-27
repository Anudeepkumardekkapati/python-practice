nums = [9,4,1,7]
k = 3

ans=float("inf")
nums.sort()
print(nums)


for i in range(len(nums)):
    for j in range(i,len(nums)):
        # print(i,j)
        temp=[]
        
        for m in range(i,j+1):
            temp.append(nums[m])
        # print(temp)
        
        
        if len(temp)==k:
            print(temp)
            first=temp[0]
            last=temp[-1]
            ans=min(ans,last-first)
print(ans)