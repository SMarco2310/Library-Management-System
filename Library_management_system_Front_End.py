import random
from Library_management_system_Back_End import Book, Member, Library

def main():
    library = Library()
    members = []
    print("Welcome to the library Management system📖📚\n")
    while True:
        user_answer = input("""
        I'm :
        1- A librarian
        2- A member\nEnter your Answer:""")
        if user_answer == "1":
            print("What would you like to do??\n")
            user_answer1 = input("""
            1- Add a Book to the Library
            2- Remove a Book from the Library\nEnter your choice here:""")
            if user_answer1 == "1":
                print("\nPlease enter the details of the book you want to add")
                book_name = input("\nPlease enter the name of the book: ")
                book_author = input("\nPlease enter the author of the book: ")
                book_id = random.randint(0, 1000)
                new_book = Book(book_name, book_author, book_id)
                library.add_book(new_book)
            elif user_answer1 == "2":
                print("What book would you like to remove\n")
                book_name = input("Please enter the book's name here: ")
                library.remove_book(book_name)
            else:
                print("Error: Unknown answer")
        elif user_answer == "2":
            print("Are you a new member of this library?? (Yes or No)\n")
            user_answer1 = input("Please enter your choice: ").title()
            if user_answer1 == "Yes":
                print("Please fill this form to start your membership")
                member_name = input("Enter your full name: ")
                member_username = input("Enter your username: ")
                member_id = random.getrandbits(20)
                new_member = Member(member_name, member_username, member_id)
                members.append(new_member)
            elif user_answer1 == "No":
                print("Would you like to: ")
                user_answer2 = input("1-Return a book\n2-Request a new book\nEnter your choice:")
                if user_answer2 == "1":
                    print("Enter the name of the book to return:")
                    book_name = input()
                    member_name = input("Enter your member name: ")
                    if any(member.name == member_name for member in members):
                        library.return_book(book_name)
                    else:
                        print("Member not found.")
                elif user_answer2 == "2":
                    print("What book would you like to borrow??")
                    book_name = input()
                    member_name = input("Enter your member name: ")
                    if any(member.name == member_name for member in members):
                        library.request_book(book_name)
                    else:
                        print("Member not found.")
                else:
                    print("Error: Unknown answer")
            else:
                print("Error: Unknown answer")
        else:
            print("Error: Unknown answer")

main()
