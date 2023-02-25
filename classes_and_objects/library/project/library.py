from project.user import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        user_username = user.username

        try:
            self.books_available[author].remove(book_name)

            user.books.append(book_name)

            if user_username not in self.rented_books:
                self.rented_books[user_username] = {}

            self.rented_books[user_username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        except ValueError:

            user_who_rented_the_book = next(filter(lambda x: book_name in self.rented_books[x], self.rented_books))

            return f"The book \"{book_name}\" is already rented and" \
                   f" will be available in {self.rented_books[user_who_rented_the_book][book_name]} days!"

    def return_book(self, author: str, book_name: str, user: User):
        try:
            user.books.remove(book_name)

            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)

        except ValueError:

            return f"{user.username} doesn't have this book in his/her records!"
