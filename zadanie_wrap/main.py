from _ast import arg
from functools import wraps


def arg_check(arg):
    def check(old_func):
        def new_func():
            result = isinstance(arg, int)
            print(result)
            return result

        return new_func

    return check


@arg_check(arg)
def examp(num):
    pass

if __name__ == "__main__":
    examp(3)
