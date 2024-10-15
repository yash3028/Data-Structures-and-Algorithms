st="aba"
arr=[]
for i in st:
    arr.append(i)
for i in st:
    if i!=arr.pop():
        print(False)
        break
    else:
        print(True)
        break
    