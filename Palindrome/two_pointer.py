def is_palin(st):
    l,r=0,len(st)-1
    flag=True
    while l<r:
        if st[l]!=st[r]:
            flag=False
        l+=1
        r-=1
    return flag
ans=is_palin("aba")
print(ans)