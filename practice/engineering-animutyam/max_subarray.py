arr=[5,9,1,8,7]
ans=0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        # print(i,j)
        temp=[]
        sums=0
        for k in range(i,j+1):
            temp.append(arr[k])
            sums=sums+arr[k]

        if len(temp)==3:
            # print(temp)
            # print(sums)
            ans=max(ans,sums)
print(ans)
           