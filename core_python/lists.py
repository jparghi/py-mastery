"""List operations and simple problems."""

def remove_duplicates(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def two_sum(nums, target):
    idx = {}
    for i, n in enumerate(nums):
        if target - n in idx:
            return (idx[target - n], i)
        idx[n] = i
    return None

if __name__ == "__main__":
    print(remove_duplicates([1,1,2,3,2,4]))
    print(two_sum([2,7,11,15], 9))
