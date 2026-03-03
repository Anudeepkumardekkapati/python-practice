s=[1,2,3,2,2]
ans=0
l=0
dici={}
for r in range(len(s)):
    
    
    if s[r] in dici:
        dici[s[r]]=dici[s[r]]+1
    else:
        dici[s[r]]=1
    while(len(dici))>2:
        dici[s[l]]=dici[s[l]]-1
        if dici[s[l]]==0:
            dici.pop(s[l])
            
        
        
        
        l=l+1
    ans=max(ans,r-l+1)
print(ans)
        
    
        
        
        