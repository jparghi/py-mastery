"""Generator examples."""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def read_large_file(lines=5):
    # Simulate streaming
    for i in range(lines):
        yield f"line {i}"

if __name__ == "__main__":
    print(list(countdown(5)))
    for line in read_large_file(3):
        print(line)
