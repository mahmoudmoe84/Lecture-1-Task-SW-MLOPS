import random


class Library:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize attributes only once
            cls._instance.books = {}
            cls._instance.users = {}
        return cls._instance
    
    def _validate_input(self, value, name):
        """Validate that input is not empty or None"""
        if not value or not str(value).strip():
            raise ValueError(f"{name} cannot be empty")
        return str(value).strip()

    def _validate_positive_number(self, value, name):
        """Validate that number is positive"""
        try:
            num = int(value)
            if num <= 0:
                raise ValueError(f"{name} must be a positive number")
            return num
        except (ValueError, TypeError):
            raise ValueError(f"{name} must be a valid positive number")
    
    def add_books(self, book_title, book_author, num_copies):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        book_author = self._validate_input(book_author, "Book author")
        num_copies = self._validate_positive_number(num_copies, "Number of copies")
        
        if book_title in self.books:
            self.books[book_title][1] += num_copies
            print(f'Updated number of books of {book_title} to be {self.books[book_title][1]}')
        else:
            on_loan = 0
            self.books[book_title] = [book_author, num_copies, on_loan]
            print(f'Added new book {book_title} with total number of copies of {num_copies}')
    
    def generate_random_id(self):
        while True:
            user_id = f"{random.randint(0,999999):06d}"
            existing_users = [user_data[0] for user_data in self.users.values()]
            if user_id not in existing_users:
                return user_id
        
    def register_new_user(self, user_name):
        # Validate input
        user_name = self._validate_input(user_name, "User name")
        
        # Check if user already exists
        if user_name in self.users:
            print(f'User Already exists in the library management system with User ID = {self.users[user_name][0]}')
            return  # Exit early - user already exists
        
        # Register new user
        user_id = self.generate_random_id()
        self.users[user_name] = [user_id, []]  # [user_id, borrowed_books_list]
        print(f'Registered new user: {user_name} with user_id {user_id}')
    
    def find_book(self, book_title):
        # Validate input
        book_title = self._validate_input(book_title, "Book title")
        
        try:
            available_copies = self.books[book_title][1] - self.books[book_title][2]
            print(f"book {book_title} is authored by {self.books[book_title][0]} and has {available_copies} copies available")
        except KeyError:
            print(f"Book title doesn't exist, returns Error")
    
    def borrow_book(self, book_title, user_name):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        user_name = self._validate_input(user_name, "User name")
        
        # Check if book exists
        if book_title not in self.books:
            print(f"Book Title {book_title} doesn't exist in our book system")
            return
        # Check if user exists
        if user_name not in self.users:
            print(f'There is no User {user_name} in the system pls create user first')
            return
        # Check if user already has this book
        if book_title in self.users[user_name][1]:
            print(f"User Already has a loan copy of {book_title}")
            return
        # Check if book is available
        available_copies = self.books[book_title][1] - self.books[book_title][2]
        if available_copies <= 0:
            print(f"Book {book_title} is out of stock all copies are on loan")
            return
        # All checks passed - borrow the book
        self.books[book_title][2] += 1
        self.users[user_name][1].append(book_title)
        print(f"User {user_name} successfully borrowed book {book_title}")
        
    def books_on_loan(self):
        books_loaned = [(book_title, self.books[book_title][2]) for book_title in self.books if self.books[book_title][2] > 0]
        print(books_loaned)
        return books_loaned
        
    
    def return_book(self, book_title, user_name):
        # Validate inputs
        book_title = self._validate_input(book_title, "Book title")
        user_name = self._validate_input(user_name, "User name")
        
        if user_name not in self.users:
            print(f"User {user_name} not in the system")
            return
        if book_title not in self.books:
            print(f"Book {book_title} not in the system")
            return
        if book_title not in self.users[user_name][1]:
            print(f'User {user_name} doesn\'t have the book')
            return
        
        self.books[book_title][2] -= 1
        self.users[user_name][1].remove(book_title)
        print(f"User {user_name} returned book {book_title} successfully")
        
                            