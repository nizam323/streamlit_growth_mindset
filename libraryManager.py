library = []

def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ")

    if read_input.lower() == "yes":
        read = True
    else:
        read = False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    found = False

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            found = True
            break

    if not found:
        print("Book not found.")

def search_book():
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        keyword = input("Enter the title: ")
        for book in library:
            if keyword.lower() in book["title"].lower():
                show_book(book)
    elif choice == "2":
        keyword = input("Enter the author: ")
        for book in library:
            if keyword.lower() in book["author"].lower():
                show_book(book)
    else:
        print("Invalid choice.")

def display_all_books():
    if len(library) == 0:
        print("No books in your library.")
    else:
        for book in library:
            show_book(book)

def show_book(book):
    read_status = "Read" if book["read"] else "Unread"
    print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def show_statistics():
    total = len(library)
    if total == 0:
        print("No books in your library.")
        return

    read_count = 0
    for book in library:
        if book["read"]:
            read_count += 1

    percent = (read_count / total) * 100
    print("Total books:", total)
    print("Percentage read:", round(percent, 1), "%")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_all_books()
    elif choice == "5":
        show_statistics()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
