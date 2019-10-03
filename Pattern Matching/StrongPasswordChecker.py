from re import compile, search

REGEX = compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+')


def is_strong_password(password):
    return len(password) >= 8 and bool(search(REGEX, ''.join(sorted(password))))
