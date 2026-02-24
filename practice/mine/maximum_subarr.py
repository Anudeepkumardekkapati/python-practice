arr=[5,9,1,8,7]
l=len(arr)
ans=[]
for i in range(l):

    for j in range(l):
        # print(i,j)
        temp=[]
        for k in range(i,j+1):
            temp.append(arr[k])
        ans.append(temp)
high=ans[0]
final_list=[]
for i in range(len(ans)):
    max_ans=(sum(ans[i]))
    if(len(ans[i]))==3:
        
        final_list.append(sum(ans[i]))
print(max(final_list))