from core_python.basics import greet, sum_list
from core_python.strings import is_palindrome

def test_greet():
    assert greet("Jigish") == "Hello, Jigish!"

def test_sum_list():
    assert sum_list([1,2,3]) == 6

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("python") is False
