arr=[12,1,3,1,1,6,7,1,8,1]
l=0
ans=0
odds=0
k=2

for i in range(len(arr)):
    if arr[i]%2 !=0:
        # print(arr[i])
        odds=odds+1
    
    
    
    
    while(odds>k):
        if arr[l]%2 !=0:
            odds=odds-1
        l=l+1
    print(arr[l:i+1],odds,i-l+1)
    
    
    ans=max(ans,i-l+1)
print(ans)
        
    
    
    
    
    

        
    