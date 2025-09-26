"""Recursion examples."""

def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n-1)

def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def subsets(nums):
    res = []
    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        backtrack(i+1, path)
        path.append(nums[i])
        backtrack(i+1, path)
        path.pop()
    backtrack(0, [])
    return res

if __name__ == "__main__":
    print(factorial(5))
    print(fib(10))
    print(subsets([1,2,3]))
