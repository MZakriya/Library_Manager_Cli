import json
import os

# Directory to store library data
USER_DATA_DIR = "user_data"

# Create the user data directory if it doesn't exist
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

# File to store library data
LIBRARY_FILE = os.path.join(USER_DATA_DIR, "library.json")

# Function to load library data
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save library data
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    rating = int(input("Rate the book (1-5): "))

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read_status": read_status,
        "ratings": [rating]
    }
    library.append(book)
    save_library(library)
    print("Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")

    initial_count = len(library)
    library[:] = [book for book in library if book["title"].lower() != title.lower()]
    if len(library) < initial_count:
        save_library(library)
        print("Book removed successfully!")
    else:
        print("Book not found in the library.")

# Function to search for a book
def search_book(library):
    search_option = input("Search by (title/author): ").lower()
    search_term = input(f"Enter the {search_option}: ")

    matching_books = []
    for book in library:
        if search_term.lower() in book[search_option].lower():
            matching_books.append(book)

    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, 1):
            avg_rating = sum(book["ratings"]) / len(book["ratings"]) if book["ratings"] else 0
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'} - Rating: {avg_rating:.1f}")
    else:
        print("No matching books found.")

# Function to display all books
def display_books(library):
    if library:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            avg_rating = sum(book["ratings"]) / len(book["ratings"]) if book["ratings"] else 0
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'} - Rating: {avg_rating:.1f}")
    else:
        print("Your library is empty.")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main function to run the CLI app
def main():
    print("Welcome to the Personal Library Manager!")
    library = load_library()

    while True:
        print("\n1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()