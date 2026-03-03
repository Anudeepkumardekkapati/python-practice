s = "abcabcbb"
l=0
ans=0
sets=set()
for r in range(len(s)):
    if s[r] not in sets:
        sets.add(s[r])
    else:
        while(s[r] in sets):
            sets.remove(s[l])
         
            l=l+1
        sets.add(s[r])
        print(sets)
    ans=max(ans,len(sets)) # ans=max(ans,r-l+1)
print(ans)