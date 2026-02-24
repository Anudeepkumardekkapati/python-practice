arr=[5,9,1,8,7]
len=len(arr)
l=0
r=0
temp=0
ans=0
for r in range(len):
    # print(arr[r])
    temp=temp+arr[r]
    # print(temp)

    if (r-l)==3:
        temp=temp-arr[l]
        l=l+1
    # print(temp)

    if(r-l+1)==3:
        # print(temp)
        ans=max(ans,temp)
print(ans)
