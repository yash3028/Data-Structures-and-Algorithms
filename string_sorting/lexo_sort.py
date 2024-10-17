def lexo_sort(arr):
    arr.sort()
    st=[]
    for i in arr:
        st.append(i)
    return st
ans=lexo_sort(["bab","aab","csa"])
print(ans)
