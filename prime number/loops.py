def prime(n):
    if n<=1:
        return False
    for i in range(2,(n//2)+1):
        if (n%i)==0:
            return False
    return True
ans=prime(7919)
print(ans)