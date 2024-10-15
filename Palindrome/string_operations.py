def is_palin(st):
    if st==st[::-1]:
        return True
    else:
        return False
ans=is_palin("abca")
print(ans)