arr = "AABABBA"
k = 1
l=0
maxf=0
ans=0
count={}



for r in range(len(arr)):
    
    count[arr[r]]=count.get(arr[r],0)+1
    # print(count)
    
    maxf=max(maxf,count[arr[r]])
    # print(r-l+1,maxf)
    
    while((r-l+1)-maxf)>k:
        count[arr[l]]=count[arr[l]]-1
        l=l+1
    ans=max(ans,r-l+1)
print(ans) 