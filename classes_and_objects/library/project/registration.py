from project.library import Library
from project.user import User


class Registration:

    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        try:
            library.user_records.remove(user)

        except ValueError:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user: User = next(filter(lambda x: x.user_id == user_id, library.user_records))

            if user.username == new_username:
                return f"Please check again the provided username - " \
                       f"it should be different than the username used so far!"

            user.username = new_username

            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        except StopIteration:

            return f"There is no user with id = {user_id}!"
