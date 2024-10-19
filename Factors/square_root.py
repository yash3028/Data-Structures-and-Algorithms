import math
def divisors(n):
    i=1
    st=[]
    while i<=math.sqrt(n):
        if n%i==0:
            if (n/i==i):
                st.append(i)
            else:
                st.append(i)
                st.append(int(n/i))
        i+=1
    return st
ans=divisors(100)
print(ans)