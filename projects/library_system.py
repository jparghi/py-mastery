"""Small OOP project: Library system (books, members, borrow/return)."""

from datetime import date, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed_by = None
        self.due_date = None

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def borrow(self, member_name, title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == title and b.borrowed_by is None), None)
        if member and book:
            book.borrowed_by = member
            book.due_date = date.today() + timedelta(days=14)
            member.borrowed.append(book)
            return True
        return False

    def return_book(self, member_name, title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member: return False
        for b in member.borrowed:
            if b.title == title:
                b.borrowed_by = None
                b.due_date = None
                member.borrowed.remove(b)
                return True
        return False

def demo():
    lib = Library()
    lib.add_book("Clean Code", "Robert C. Martin")
    lib.add_book("Fluent Python", "Luciano Ramalho")
    lib.add_member("Olivia")
    lib.borrow("Olivia", "Clean Code")
    print([(b.title, b.borrowed_by.name if b.borrowed_by else None) for b in lib.books])
    lib.return_book("Olivia", "Clean Code")
    print([(b.title, b.borrowed_by.name if b.borrowed_by else None) for b in lib.books])

if __name__ == "__main__":
    demo()
