def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    n1, n2 = 0, 1
    for i in range(2, n+1): 
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n2

ans = fibo(9)
print(ans)
