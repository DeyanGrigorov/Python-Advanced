from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        start = timer()
        func(*args)
        end = timer()
        result = end - start
        return result
    return wrapper





