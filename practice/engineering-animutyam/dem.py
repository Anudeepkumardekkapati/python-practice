def fun(nums,k):

    nums = [1,2,1,2,3]
    k = 2

    l=0
    dici={}
    ans=0
    for i in range(len(nums)):
        i_val=nums[i]
        if i_val not in dici:
            dici[i_val]=1
        else:
            dici[i_val]=dici[i_val]+1
        print(dici)
        
        
        if i-l==k:
            l_val=nums[l]
            dici[l_val]=dici[l_val]-1
            if dici[l_val]==0:
                dici.pop(l_val)
            l=l+1
        ans=ans+i-l+1
    return ans
nums = [1,2,1,2,3]
k = 2
res=fun(nums,k)-fun(nums,k-1)
print(res)




            
        
        
        
        

            
            
        
    