arr=[9,3,4,8,1]
l=0
k=10
ans=0
temp=0
for i in range(len(arr)):
    temp=temp+arr[i]
    # print(temp)
    while(temp>k):
        temp=temp-arr[l]
        l=l+1
    ans=max(ans,i-l+1)
    # print(arr[l:i+1],sum(arr[l:i+1]),ans)
print(ans)
        
    