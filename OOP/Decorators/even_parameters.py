def even_parameters(func):
    def wrapper_func(*args):
        for arg in args:
            if not (isinstance(arg, int) and arg % 2 == 0):
                return 'Please use only even numbers!'
        return func(*args)
    return wrapper_func


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
