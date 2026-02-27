nums = [1,4,3,2]
nums.sort()
print(nums)
ans=0
for i in range(0,len(nums),2):
    ans=ans+nums[i]
print(ans)