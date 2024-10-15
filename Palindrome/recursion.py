def is_palin(st):
    if len(st)<=1:
        return True
    if st[0]!=st[-1]:
        return False
    return is_palin(st[1:-1])
st="abca"
print(is_palin(st))
