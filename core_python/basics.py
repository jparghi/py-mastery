"""Basics: variables, loops, functions, list/dict ops."""

def greet(name: str) -> str:
    return f"Hello, {name}!"

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

def main():
    print(greet("World"))
    nums = [1, 2, 3, 4, 5]
    print("Sum:", sum_list(nums))

if __name__ == "__main__":
    main()
