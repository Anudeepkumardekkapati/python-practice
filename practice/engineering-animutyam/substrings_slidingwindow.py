s="xyzzaz"
l=0
ans=0
n=len(s)
dici={}
k=3
for r in range(n):
    if(s[r]) in dici:
        dici[s[r]]=dici[s[r]]+1
    else:
        dici[s[r]]=1
    # print(dici)
    
    
    if r-l==k:
        dici[s[l]]-=1
        if dici[s[l]]==0:
            dici.pop(s[l])
        l=l+1
    if(len(dici)) ==k:
        # print(dici)
        ans=ans+1
print(ans)
        
        
        
