def tags(tag):
    def decorator(func):
        def wrapper(*args):
            result = f"<{tag}>{func(*args)}</{tag}>"
            return result
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))