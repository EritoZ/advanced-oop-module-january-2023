from project.movie_specification.movie import Movie


class Thriller(Movie):

    DEFAULT_AGE_RESTRICTION = 16

    def __init__(self, title, year, owner, age_restriction=DEFAULT_AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)
