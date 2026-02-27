k = 3
count=0
threshold = 4
arr = [2,2,2,2,5,5,5,8]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        # print(i,j)
        temp=[]
        for r in range(i,j+1):
            temp.append(arr[r])
        # print(temp)
        if len(temp)==k:
            # print(temp)
            sums=sum(temp)
            avg=sums//k
            # print(avg)
            if avg>=threshold:
                count=count+1
                # print(avg)
print(count)
        