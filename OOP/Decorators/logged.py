def logged(function):
    def wrapper_func(*args):
        args_formatted = ', '.join(map(str, args))

        result = function(*args)

        return '\n'.join([
            f'you called {function.__name__}({args_formatted})',
            f'it returned {result}'
        ])

    return wrapper_func


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
