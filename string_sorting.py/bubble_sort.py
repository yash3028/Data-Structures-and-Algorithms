def sort_string(s):
    li=list(s)
    n=len(li)
    for i in range(n):
        for j in range(0,n-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li
ans=sort_string("yashwanth")
print(ans)