def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == 'even':
        return list(filter(lambda x: x % 2 == 0, numbers))
    return list(filter(lambda x: x % 2 != 0, numbers))

