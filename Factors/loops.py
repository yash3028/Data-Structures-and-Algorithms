def divisors(n):
    i=1
    st=[]
    while i<=n:
        if (n%i)==0:
            st.append(i)
        i+=1
    return st
ans=divisors(100)
print(ans)