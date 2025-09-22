# Library Management System

A simple Python project for managing books and users in a library. This was built as a learning exercise to practice object-oriented programming concepts.

## What This Does

This is a basic library system where you can add books, register users, and let people borrow and return books. It's a command-line program that uses Python classes and functions to organize everything.

## What It Can Do

The program has these main features:
- Add books to the library (with author and number of copies)
- Register new users (gives them a random ID number)
- Search for books 
- Let users borrow books (if available)
- Let users return books
- Show which books are currently borrowed

## Things to Note
- Users get a random 6-digit ID when they register
- You can't borrow the same book twice
- It keeps track of how many copies are available vs borrowed
- Has some basic error checking (like if you enter text instead of numbers)

## How the Code is Organized

I split the code into a few files to keep things organized:

### `classes_lib_system.py`
This has the main Library class with all the important functions:
- `add_books()` - adds books or updates quantities
- `register_new_user()` - creates new users
- `find_book()` - searches for books
- `borrow_book()` - handles borrowing
- `return_book()` - handles returns
- `books_on_loan()` - shows borrowed books
- `generate_random_id()` - makes user IDs

### `functions.py`
Just some helper functions for the menu and navigation

### `main.py`
The main program that runs everything and shows the menu

## How to Run It

### What You Need
- Python 3 (any recent version should work)

### Setup
1. Download all the files and put them in the same folder
2. Make sure you have these files:
   - `main.py`
   - `classes_lib_system.py`
   - `functions.py` 
   - `__init__.py`

### Running
Just run this in your terminal:
```bash
python main.py
```

## How to Use It

When you run the program, you'll see a menu with 7 options. Just type the number and press enter.

### The Menu Options

**1. Add Book**
- Type in the book title, author, and how many copies you have
- If the book already exists, it adds more copies
- If it's new, it creates a new entry

**2. Add User** 
- Just enter someone's name
- The system gives them a random ID number
- If they're already registered, it tells you their ID

**3. Find Book**
- Enter a book title to search for it
- Shows the author and how many copies are available
- Says "doesn't exist" if it's not in the system

**4. Borrow Book**
- Enter the user name and book title
- Only works if:
  - The user is registered
  - The book exists
  - There are copies available
  - The user doesn't already have that book

**5. Return Book**
- Enter user name and book title
- Updates everything when they return it

**6. Borrowed Books**
- Shows all the books that are currently borrowed

**7. Exit**
- Quits the program

After each action, you can either go back to the main menu or exit.

## How the Data is Stored

The program keeps everything in memory using Python dictionaries (it doesn't save to files).

Books are stored like this:
```python
books = {
    "book_title": [author, total_copies, copies_currently_borrowed]
}
```

Users are stored like this:
```python
users = {
    "user_name": [user_id, [list_of_books_they_borrowed]]
}
```

## Example of Using It

**Adding a book:**
```
Enter Book Title: Harry Potter
Author Name: J.K. Rowling  
Enter num of Copies: 3
```
Output: `Added new book Harry Potter with total number of copies of 3`

**Registering someone:**
```
Enter User Name: Alice
```
Output: `Registered new user: Alice with user_id 123456`

**Borrowing a book:**
```
Enter User Name: Alice
Enter Book Title: Harry Potter
```
Output: `User Alice successfully borrowed book Harry Potter`

## Things That Might Go Wrong

The program tries to handle some common mistakes:
- If you type letters instead of numbers for the menu, it asks again
- If you try to borrow a book for someone who isn't registered, it tells you
- If you search for a book that doesn't exist, it says so
- If all copies of a book are borrowed, it won't let you borrow more
- You can't borrow the same book twice
- Basic stuff like that

## What You Need to Run It

- Just Python 3 (no special libraries needed)
- All the project files in the same folder

The files are:
```
project-oop-library-management-system/
├── __init__.py
├── main.py  
├── classes_lib_system.py
├── functions.py
└── README.md
```

## Things I Could Add Later

Some ideas for making this better:
- Save the data to a file so it doesn't disappear when you close the program
- Add due dates for borrowed books
- Let people search by author
- Add a limit on how many books someone can borrow
- Make a simple GUI instead of just text
- Add book categories

## Notes

This is a learning project to practice Python classes and functions. It's pretty basic but covers the main concepts of object-oriented programming that we're studying.

---
