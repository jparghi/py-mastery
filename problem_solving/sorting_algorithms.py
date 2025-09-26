"""Classic sorting algorithms: bubble, merge, quick."""

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(L, R):
    i=j=0
    out=[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i]); i+=1
        else:
            out.append(R[j]); j+=1
    out.extend(L[i:]); out.extend(R[j:])
    return out

def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr)//2]
    lesser = [x for x in arr if x < pivot]
    equal  = [x for x in arr if x == pivot]
    greater= [x for x in arr if x > pivot]
    return quick_sort(lesser) + equal + quick_sort(greater)

if __name__ == "__main__":
    data = [5,3,8,4,2,7,1,10]
    print(bubble_sort(data))
    print(merge_sort(data))
    print(quick_sort(data))
