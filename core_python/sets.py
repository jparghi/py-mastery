"""Set examples: membership, unions, intersections."""

def unique_intersection(a, b):
    return set(a).intersection(b)

if __name__ == "__main__":
    print(unique_intersection([1,2,3,4], [3,4,5]))
