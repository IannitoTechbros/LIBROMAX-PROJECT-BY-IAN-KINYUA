from database.setup import SessionLocal
from models.author import Author
from models.book import Book

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Add a new author")
        print("3. Delete a book")
        print("4. Delete an author")
        print("5. View all books")
        print("6. View all authors")
        print("7. View books by author")
        print("8. Find a book by title")
        print("9. Find an author by name")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            add_author()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            delete_author()
        elif choice == "5":
            view_all_books()
        elif choice == "6":
            view_all_authors()
        elif choice == "7":
            view_books_by_author()
        elif choice == "8":
            find_book_by_title()
        elif choice == "9":
            find_author_by_name()
        elif choice == "10":
            print("Thank you for choosing Ian's Libromaster system.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    session = SessionLocal()
    title = input("Enter book title: ")
    genre = input("Enter book genre: ")
    published_year = int(input("Enter book published year: "))
    author_id = int(input("Enter author ID: "))
    
    book = Book(title=title, genre=genre, published_year=published_year, author_id=author_id)
    session.add(book)
    session.commit()
    session.close()
    print("\n Book added successfully.")

def add_author():
    session = SessionLocal()
    name = input("Enter author name: ")
    birth_year = int(input("Enter author birth year: "))
    nationality = input("Enter author nationality: ")
    
    author = Author(name=name, birth_year=birth_year, nationality=nationality)
    session.add(author)
    session.commit()
    session.close()
    print("Author added successfully.")

def delete_book():
    session = SessionLocal()
    book_id = int(input("Enter book ID to delete: "))
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully.")
    else:
        print("Book not found.")
    session.close()

def delete_author():
    session = SessionLocal()
    author_id = int(input("Enter author ID to delete: "))
    author = session.query(Author).get(author_id)
    if author:
        session.delete(author)
        session.commit()
        print("Author deleted successfully.")
    else:
        print("Author not found.")
    session.close()

def view_all_books():
    session = SessionLocal()
    books = session.query(Book).all()
    if not books:
        print("No books available.")
    else:
        print("Books:")
        for book in books:
            print(f"Title: {book.title}, Genre: {book.genre}, Published Year: {book.published_year}, Author: {book.author.name}, Author's Id:{book.author.id}, ")
    session.close()


def view_all_authors():
    session = SessionLocal()
    authors = session.query(Author).all()
    if not authors:
        print("No authors available.")
    else:
        print("Authors:")
        for author in authors:
            print(author)
    session.close()

def view_books_by_author():
    session = SessionLocal()
    author_id = int(input("Enter author ID to view their books: "))
    books = session.query(Book).filter_by(author_id=author_id).all()
    if not books:
        print("No books available for this author.")
    else:
        print("Books by Author:")
        for book in books:
            print(f"Title: {book.title}, Genre: {book.genre}, Published Year: {book.published_year}")
    session.close()

def find_book_by_title():
    session = SessionLocal()
    title = input("Enter book title to search: ")
    book = session.query(Book).filter_by(title=title).first()
    if book:
        print(book)
    else:
        print("Book not found.")
    session.close()

def find_author_by_name():
    session = SessionLocal()
    name = input("Enter author name to search: ")
    author = session.query(Author).filter_by(name=name).first()
    if author:
        print(author)
    else:
        print("Author not found.")
    session.close()
