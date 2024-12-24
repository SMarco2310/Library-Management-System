import random

class Book:
    def __init__(self, book_name, author, book_id):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id


class Library:
    def __init__(self):
        self.library = {}

    def add_book(self, book):
        self.library[book.book_name] = {'Author': book.author, 'Id': book.book_id}
        print(f"{book.book_name} successfully added")

    def remove_book(self, book_name):
        if book_name in self.library:
            del self.library[book_name]
            print(f"This {book_name} has successfully been removed")
        else:
            print("This book has not been found in the Library")


class Member:
    def __init__(self, member_name, member_username, member_id):
        self.member_name = member_name
        self.member_username = member_username
        self.member_id = member_id
        self.user_book = []

    def request_book(self, library, book_name):
        if len(self.user_book) == 0 and book_name in library.library:
            self.user_book.append(book_name)
            print(f"You've borrowed {book_name}")
        else:
            print(f"You've not yet return {self.user_book[0]}")
            print("\n If you want to borrow another Book you must to return the one that you have")
            
    def return_book(self, library, book_name):
        if book_name in self.user_book:
            self.user_book.remove(book_name)
            print(f"{self.member_name} has returned {book_name}.")
        else:
            print(f"{self.member_name} did not borrow {book_name}.")
