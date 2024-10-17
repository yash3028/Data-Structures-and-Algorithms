def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def lexo_sort(arr):
    return bubble(arr)
ans=lexo_sort(["bab","aab","ada"])
print(ans)
