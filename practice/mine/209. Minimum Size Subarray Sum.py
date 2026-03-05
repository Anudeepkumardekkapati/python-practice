target = 11
nums = [1,1,1,1,1,1,1,1]
if (sum(nums)<target):
    ans=0
    
else:   
    l=0
    sums=0
    count=0
    ans=float('inf')
    for r in range(len(nums)):
        sums=sums+nums[r]
        count=count+1
        
            
        
        
        while(sums>=target):
            lval=nums[l]
            sums=sums-lval
            ans=min(ans,(count))
            count=count-1
            # print(count,sums)
            
            
            
            l=l+1
        
print(ans)


    
            

    
    