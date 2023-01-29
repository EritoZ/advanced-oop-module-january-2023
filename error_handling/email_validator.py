import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def check_email(email_address):

    if '@' in email_address:
        at_index = email_address.index('@')
        name = email_address[:at_index]

        if len(name) < 5:
            raise NameTooShortError("Name must be more than 4 characters")

    else:
        raise MustContainAtSymbolError("Email must contain @")

    if re.search(r'\.com|\.bg|\.net|\.org', email_address) is None:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    return 'Email is valid'


command = input()

while command != 'End':
    email = command

    print(check_email(email))

    command = input()
