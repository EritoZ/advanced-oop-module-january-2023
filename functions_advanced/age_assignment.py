def age_assignment(*args, **kwargs):

    names = args
    ages_letters = kwargs

    name_age_dict = {name: ages_letters[name[0]] for name in names}

    name_age_dict = [f"{name} is {age} years old." for name, age in sorted(name_age_dict.items())]

    return '\n'.join(name_age_dict)


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))