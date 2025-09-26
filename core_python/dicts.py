"""Dictionary (HashMap) examples."""

from collections import Counter

def char_frequency(s: str):
    return dict(Counter(s))

if __name__ == "__main__":
    print(char_frequency("banana"))
