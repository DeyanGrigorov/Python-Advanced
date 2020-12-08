def make_bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'

    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'

    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<u>{res}</u>'

    return wrapper




@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
