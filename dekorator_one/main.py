def add_stars(func):
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner


@add_stars
def menu(*args, **kwargs):
    print(args[0])


menu("Hello World !!", amount=17)
