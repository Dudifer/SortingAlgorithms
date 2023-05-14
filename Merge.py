def merge(A:list,i:int,j:int,k:int):
    i1=j-i+1
    i2=k-j
    l,r=[],[]
    for a in range(i1):
        l.append(A[i+l])
    for b in range(i2):
        r.append(A[j+b])
    l.append(int(float('inf')))
    r.append(int(float('inf')))
    a,b=0,0
    for c in range(k-i):
        if l[a]<=r[b]:
            A[c]=l[a]
            a+=1
        else:
            A[c]=r[b]
            b+=1
    return A
def mergeSort(A, i,k):
    if i<k:
        j=

