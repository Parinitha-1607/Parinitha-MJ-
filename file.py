import os

FILE_NAME = "library.txt"

# Function to add a book
def add_book(book_id, title, author):
    with open(FILE_NAME, "a") as f:
        f.write(f"{book_id},{title},{author}\n")
    print("Book added successfully!")

# Function to view all books
def view_books():
    if not os.path.exists(FILE_NAME):
        print("No books found!")
        return
    with open(FILE_NAME, "r") as f:
        print("\n--- Library Books ---")
        for line in f:
            book_id, title, author = line.strip().split(",")
            print(f"ID: {book_id}, Title: {title}, Author: {author}")

# Function to search for a book by ID
def search_book(book_id):
    found = False
    with open(FILE_NAME, "r") as f:
        for line in f:
            b_id, title, author = line.strip().split(",")
            if b_id == book_id:
                print(f"Book Found → ID: {b_id}, Title: {title}, Author: {author}")
                found = True
                break
    if not found:
        print("Book not found!")

# Function to delete a book by ID
def delete_book(book_id):
    if not os.path.exists(FILE_NAME):
        print("No books to delete!")
        return
    lines = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        deleted = False
        for line in lines:
            b_id, title, author = line.strip().split(",")
            if b_id != book_id:
                f.write(line)
            else:
                deleted = True
        if deleted:
            print("Book deleted successfully!")
        else:
            print("Book not found!")

# --- Demo Menu ---
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        add_book(book_id, title, author)
    elif choice == "2":
        view_books()
    elif choice == "3":
        book_id = input("Enter Book ID to search: ")
        search_book(book_id)
    elif choice == "4":
        book_id = input("Enter Book ID to delete: ")
        delete_book(book_id)
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")