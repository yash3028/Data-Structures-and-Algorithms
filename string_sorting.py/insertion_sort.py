def string_sort(s):
    li=list(s)
    n=len(li)
    for i in range(1,n):
        index=i
        while index>0 and li[index-1]>li[index]:
            li[index], li[index - 1] = li[index - 1], li[index]  
            index -= 1
    return li

ans=string_sort("yashwanth")
print(ans)