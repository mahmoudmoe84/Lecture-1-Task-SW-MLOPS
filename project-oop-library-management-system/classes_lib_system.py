import random
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        # self.borrowed_books={}
    
    def add_books(self, book_title,book_author,num_copies):
        
        if book_title in self.books:
            self.books[book_title][1] +=num_copies
            print(f'Updated number of books of {book_title} to be {self.books[book_title][1]}')
        else:
            on_loan = 0
            self.books[book_title] = [book_author,num_copies,on_loan]
            # self.borrowed_books[book_title] =0
            print(f'Added new book {book_title} with total number of copies of {num_copies}')
    
    def generate_random_id(self):
        while True:
            user_id = f"{random.randint(0,999999):06d}"
            existing_users = [user_data[0] for user_data in self.users.values()]
            if user_id not in existing_users:
                return user_id
        
        
    def register_new_user(self,user_name):
        
        if user_name in self.users:
            print(f'User Already exists in the library management system with User ID = {self.users[user_name][0]}')

        else:
            user_id =self.generate_random_id()
            books_with_user = []
            self.users[user_name] = [user_id,books_with_user]
            print(f'Registered new user: {user_name} with user_id {user_id}')
    
    def find_book(self,book_title):
        try:
            available_copies = self.books[book_title][1] - self.books[book_title][2]
            print(f"book {book_title} is authored by {self.books[book_title][0]} and has {available_copies} copies available")
        except KeyError:
            print(f"Book title doesnt exist, returns Error")
    
    def borrow_book(self,book_title,user_name):
        if book_title in self.books:
            available_copies =self.books[book_title][1] - self.books[book_title][2]
            if available_copies>0:
                if book_title not in self.users[user_name][1]:
                    if user_name in self.users :
                        self.books[book_title][2] +=1
                        self.users[user_name][1].append(book_title)
                        print(f"User {user_name} successfully borrowed book {book_title}")
                    else:
                        print(f'There is no User {user_name} in the system pls create user first')
                else: 
                    print(f"User Already has a loand copy of {book_title}")
            else:
                print(f"Book {book_title} is out of stock all copies are on loan")
        else:
            print(f"Book Title {book_title} doesn't exist in our book system")
        
    def books_on_loan(self):
        return print([(book_title, self.books[book_title][2]) for book_title in self.books if self.books[book_title][2] > 0])
        
    
    def return_book(self,book_title,user_name):
        if user_name not in self.users:
            print(f"User {user_name} not in the system")
            return
        if book_title not in self.books:
            print(f"Book {book_title} not in the system")
            return
        self.books[book_title][2]-=1
        self.users[user_name][1].remove(book_title)
        print(f"User {user_name} returned book {book_title} successfully")
        
                            