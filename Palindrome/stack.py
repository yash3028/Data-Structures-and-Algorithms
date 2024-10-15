def is_palin(st):
    arr=[]
    for i in st:
        arr.append(i)
    for i in st:
        if i!=arr.pop():
            return False
        else:
            continue
    return True
ans=is_palin("abccbaabcba")
print(ans)

    