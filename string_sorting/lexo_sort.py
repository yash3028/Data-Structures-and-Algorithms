def compare(s1,s2):
    n1=len(s1)
    n2=len(s2)
    n=min(n1,n2)
    for i in range(n):
        if s1[i]>s2[i]:
            return True
        elif s1[i]<s2[i]:
            return False
    if n1>n2:
        return True
    else:
        return False
    
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if compare(arr[j],arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def lexo_sort(arr):
    return bubble(arr)
    
ans=lexo_sort(["aadb","aade","aavb"])
print(ans)
