from abc import ABC

from project.user import User


class Movie(ABC):

    DEFAULT_AGE_RESTRICTION = ...

    def __init__(self, title, year, owner: User, age_restriction):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        
        self.__year = value
        
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, value: User):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    def age_restriction_error_message(self):
        return f"{self.__class__.__name__} movies must be restricted for audience under" \
               f" {self.DEFAULT_AGE_RESTRICTION} years!"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.DEFAULT_AGE_RESTRICTION:
            raise ValueError(self.age_restriction_error_message())

        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}," \
               f" Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
