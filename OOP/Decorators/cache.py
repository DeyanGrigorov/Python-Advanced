def cache(func):
    def wrapper(n):
        result = func(n)
        wrapper.log[n] = result
        return result
    wrapper.log = {}
    return wrapper

def fibonacci(n):
    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
