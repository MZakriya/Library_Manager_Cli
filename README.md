
### README.md

```markdown
# Personal Library Manager (CLI)

A simple command-line application to manage your personal book collection. This app allows you to add, remove, search, and display books, as well as view basic statistics about your library.

---

## Features

- **Add a Book**: Add a new book to your library with details like title, author, publication year, genre, read status, and rating.
- **Remove a Book**: Remove a book from your library by its title.
- **Search for a Book**: Search for books by title or author.
- **Display All Books**: View all books in your library with their details.
- **Display Statistics**: View the total number of books and the percentage of books you've read.
- **Exit**: Exit the application.

---

## Prerequisites

- Python 3.x installed on your system.

---

## Setup

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/your-username/personal-library-manager.git
   cd personal-library-manager
   ```

2. **Run the Application**:
   - Save the script as `library_manager_cli.py`.
   - Open a terminal and navigate to the directory where the script is saved.
   - Run the script using Python:
     ```bash
     python library_manager_cli.py
     ```

---

## Usage

Once the application is running, you will see the following menu:

```
Welcome to the Personal Library Manager!

1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice:
```

### 1. Add a Book
- Enter the book's details (title, author, publication year, genre, read status, and rating).
- The book will be added to your library.

### 2. Remove a Book
- Enter the title of the book you want to remove.
- The book will be removed from your library if it exists.

### 3. Search for a Book
- Choose to search by title or author.
- Enter the search term.
- Matching books will be displayed.

### 4. Display All Books
- View all books in your library with their details (title, author, year, genre, read status, and average rating).

### 5. Display Statistics
- View the total number of books in your library and the percentage of books you've read.

### 6. Exit
- Exit the application.

---

## Example Workflow

1. **Add a Book**:
   ```
   Enter your choice: 1
   Enter the book title: The Great Gatsby
   Enter the author: F. Scott Fitzgerald
   Enter the publication year: 1925
   Enter the genre: Fiction
   Have you read this book? (yes/no): yes
   Rate the book (1-5): 5
   Book added successfully!
   ```

2. **Display All Books**:
   ```
   Enter your choice: 4
   Your Library:
   1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read - Rating: 5.0
   ```

3. **Exit**:
   ```
   Enter your choice: 6
   Goodbye!
   ```

---

## Data Storage

- The library data is stored in a JSON file (`user_data/library.json`) in the `user_data` directory.
- The `user_data` directory is automatically created if it doesn't exist.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Author

Muhammad Zakriya  
[[Your GitHub Profile]](https://github.com/MZakriya)  
ziky9892gmail.com
```

---

### Key Sections in the README:
1. **Title and Description**: A brief overview of the project.
2. **Features**: A list of features provided by the application.
3. **Prerequisites**: Requirements to run the application.
4. **Setup**: Instructions to set up and run the application.
5. **Usage**: A guide on how to use the application.
6. **Example Workflow**: A step-by-step example of using the application.
7. **Data Storage**: Information about where and how data is stored.
8. **License**: Information about the project's license.
9. **Contributing**: Guidelines for contributing to the project.
10. **Author**: Information about the author.

---
