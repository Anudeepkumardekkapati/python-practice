s = "aababcabc"
l=len(s)
i=0
li=0
temp=[]
ans=0

for r in range(l):
    # print(s[r],r)
    temp=temp+[s[r]]
    # print(temp)
    # print(r,li)
    
    if (r-li)==3:
        # temp.pop(li)
        temp.remove(s[li])
        # print(temp)
        # print(temp)
        li=li+1
    
    # print(temp)
    count=[]
    if r-li+1==3:
        count=len((set(temp)))
        # print(count)
        # print(count)
    if count==3:
        ans=ans+1
print(ans)
        


        
        
    
    
    