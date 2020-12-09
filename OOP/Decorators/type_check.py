def type_check(type):
    def decorator(func):
        def wrapper(n):
            if isinstance(n, type):
                return func(n)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
