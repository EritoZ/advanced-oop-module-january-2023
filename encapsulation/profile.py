import re


class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        if len(value) not in range(5, 16):
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @password.setter
    def password(self, value):
        outcome = re.search(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$", value)

        if outcome is None:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.__password)}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

correct_profile.password = '12345678'
