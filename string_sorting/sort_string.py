def sort_string(s):
    li=list(s)
    n=len(li)
    for i in range(n):
        for j in range(0,n-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return "".join(li)

def lexo(arr):
    st=[]
    for i in arr:
        st_sort=sort_string(i)
        st.append(st_sort)
    return st

ans=lexo(["bab", "aab", "csa"])
print(ans)