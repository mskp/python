class Library:

    def __init__(self, books_list): self.books = books_list

    def available_books(self):
        for book in self.books: 
            print(book)

    def issue_book(self, book_name):
        if book_name in self.books: 
            self.books.remove(book_name); 
            print(f"Book {book_name} has been issued.")

            return True
        
        else: 
            print("Book not available")

            return False

    def return_or_donate_book(self, book_name): 
        self.books.append(book_name)
        print("Book returned")

class Student:

    def request_book(self): 
        self.book = input("Enter the name of the book: ")

        return self.book

    def return_book(self):
        self.book = input("Enter the name of the book: ")
        return self.book

myLib = Library(["Data Structures and Algorithms",
 "Cloud Computing",
  "Computer Graphics",
   "Java", "C++", "Python"])
   
mohan = Student()

while True:
    print("""\nSelect from the options below:-
    1. Issue a book
    2. Return book
    3. Show available books
    4. Exit\n""")
    ch = int(input("Enter your choice:- "))
    
    match ch:
        case 1: 
            print()
            myLib.issueBook(mohan.requestBook())

        case 2: 
            print()
            myLib.returnOrDonateBook(mohan.returnBook())

        case 3: 
            print()
            myLib.availableBooks()

        case 4: 
            print("Thanks for using our service")
            exit()

        case _: print("Invalid choice")