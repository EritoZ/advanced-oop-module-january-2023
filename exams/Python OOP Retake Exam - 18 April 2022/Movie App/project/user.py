class User:

    def __init__(self, username, age):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

        self.__age = value

    def __str__(self):
        message = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]

        if self.movies_liked:
            liked_movies = (movie.details() for movie in self.movies_liked)

            message.extend(liked_movies)

        else:
            message.append("No movies liked.")

        message.append("Owned movies:")

        if self.movies_owned:
            owned_movies = (movie.details() for movie in self.movies_owned)

            message.extend(owned_movies)

        else:
            message.append("No movies owned.")

        return '\n'.join(message)
