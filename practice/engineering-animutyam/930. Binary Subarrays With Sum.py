def atmost(nums,k):
    if k<0:
        return 0
    l=0
    temp=0
    ans=0
    for i in range(len(nums)):
        if nums[i]==1:
            temp=temp+1
        
        
        while(temp>k):
            if nums[l]==1:
                temp=temp-1
                
            l=l+1
        ans=ans+(i-l+1)
    return(ans)
       
nums = [0,0,0,0,0]
goal = 0
res=atmost(nums,goal)-atmost(nums,goal-1)
print(res)


            
        
    
        