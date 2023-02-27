from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        try:
            library.user_records.remove(user)

        except ValueError:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user: User = next(filter(lambda x: x.user_id == user_id, library.user_records))

            if user.username == new_username:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"

            if user.username in library.rented_books:
                books_data = library.rented_books.pop(user.username)

                library.rented_books[new_username] = books_data

            user.username = new_username

            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        except StopIteration:

            return f"There is no user with id = {user_id}!"
