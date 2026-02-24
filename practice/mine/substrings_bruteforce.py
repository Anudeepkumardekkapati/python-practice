s = "aababcabc"

ans=0
for i in range(len(s)):
   
    for j in range(i,len(s)):
        # print(i,j)
        temp=[]
        for k in range(i,j+1):
            temp.append(s[k])
        # print(temp)
        
        
        if len((temp))==3 and len(set((temp)))==3:
            print(temp)
            ans=ans+1
print(ans)