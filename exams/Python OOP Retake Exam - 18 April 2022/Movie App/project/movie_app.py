from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    @staticmethod
    def __find_user(name, somewhere):
        return next(filter(lambda u: u.username == name, somewhere))

    @staticmethod
    def __check_if_movie_not_in_collection(movie: Movie, movies_collection):
        if movie not in movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    @staticmethod
    def __check_if_not_movie_owner(movie: Movie, username):
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    def register_user(self, username: str, age: int):
        try:
            self.__find_user(username, self.users_collection)

            raise Exception("User already exists!")

        except StopIteration:
            new_user = User(username, age)

            self.users_collection.append(new_user)

            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        try:
            user: User = self.__find_user(username, self.users_collection)

        except StopIteration:
            raise Exception("This user does not exist!")

        self.__check_if_not_movie_owner(movie, username)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        attributes_to_change = kwargs.items()

        self.__check_if_movie_not_in_collection(movie, self.movies_collection)

        self.__check_if_not_movie_owner(movie, username)

        for attribute, new_value in attributes_to_change:
            if attribute == 'title':
                movie.title = new_value

            elif attribute == "year":
                movie.year = new_value

            else:
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        self.__check_if_movie_not_in_collection(movie, self.movies_collection)

        self.__check_if_not_movie_owner(movie, username)

        movie.owner.movies_owned.remove(movie)

        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user: User = self.__find_user(username, self.users_collection)

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1

        user.movies_liked.append(movie)

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):

        user: User = self.__find_user(username, self.users_collection)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1

        user.movies_liked.remove(movie)

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        message = (movie.details() for movie in sorted_movies)

        return '\n'.join(message)

    def __str__(self):
        message = []

        if self.users_collection:
            message.append(f"All users: {', '.join(user.username for user in self.users_collection)}")

        else:
            message.append("All users: No users.")

        if self.movies_collection:
            message.append(f"All movies: {', '.join(movie.title for movie in self.movies_collection)}")

        else:
            message.append("All movies: No movies.")

        return '\n'.join(message)
