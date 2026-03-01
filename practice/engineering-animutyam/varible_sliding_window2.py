arr=[0,1,3,1,1,6,7,1,0,1]

l=0
ans=0
temp=0
k=2


for i in range(len(arr)):
    if arr[i]==1:
        temp=temp+1
    
    
    
    while(temp>k):
        if arr[l]==1:
            temp=temp-1
            
        l=l+1
    ans=max(ans,i-l+1)
print(ans)