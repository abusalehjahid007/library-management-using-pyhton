class Library:
    __book_list = []
    
    @classmethod
    def entry_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.__book_list.append(book)
        
    @classmethod
    def get_books(self):
        return self.__book_list
    
    @classmethod
    def find_book(self, id):
        for book in self.__book_list:
            if book.book_id == id:
                return book
        

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"You have successfully borrowed {self.__title}")
        else:
            print(f"{self.__title} is laready borrowed")
    
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"You have successfully returned {self.__title}")
        else:
            print(f"{self.__title} is already available")
            
    def view_book_info(self):
        if self.__availability:
            status = "Available"
        else:
            status = "Not Available"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status} ")
    
    
def menu():
    while True:
        print("\n-------Welcome to the Library-------")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        choice = input("\nEnter choice: ")
        if choice == '1':
            for book in Library.get_books():
                book.view_book_info()
        elif choice in ('2', '3'):
            id = input("Enter Book ID: ")
            book = Library.find_book(id)
            if book:
                if choice == '2':
                    book.borrow_book()
                else:
                    book.return_book()
            else:
                print("Book not found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")
                

Library.entry_book("101", "Python Programming", "Jahid")
Library.entry_book("102", "Data Science Basics", "Moon")
Library.entry_book("103", "Machine Learning", "Kibria")
Library.entry_book("104", "Algorithm Basics", "Rakib")
Library.entry_book("105", "OOP Basics", "Rony")

            
menu()