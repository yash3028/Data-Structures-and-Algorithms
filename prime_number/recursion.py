import math
def prime(n,index=2):
    if n<=1:
        return False
    if index>int(math.sqrt(n)):
        return True
    if n%index==0:
        return False
    return prime(n,index+1)
ans=prime(72)
print(ans)