"""Exception handling patterns."""

def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return float('inf')

if __name__ == "__main__":
    print(safe_div(10, 2))
    print(safe_div(10, 0))
