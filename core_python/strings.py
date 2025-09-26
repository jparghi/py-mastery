"""Common string utilities and interview-style functions."""

def is_palindrome(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

def reverse_words(sentence: str) -> str:
    return ' '.join(reversed(sentence.split()))

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(reverse_words("hello world from python"))         # python from world hello
