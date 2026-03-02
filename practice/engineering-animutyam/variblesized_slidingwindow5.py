arr = "TTFF"
k =2
l=0
cnf=0
cnt=0

ans=0



for r in range(len(arr)):
    if arr[r]=='T':
        cnt=cnt+1
    else:
        cnf=cnf+1
    # print(cnt,cnf)
    
    
    while(min(cnf,cnt))>k:
        
        
        if arr[l]=="T":
            cnt=cnt-1
        else:
            cnf=cnf-1
        l=l+1
    ans=max(ans,r-l+1)
print(ans)
        
        
        
