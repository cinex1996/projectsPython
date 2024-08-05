def logged(func):
    def check(*args):
        print(f"Wywołana przez ciebie funkcja to {func.__name__} z argumentami {args} która"
              f" zwraca wartość {func(*args)}")

    return check


@logged
def func(*args):
    return 3 + len(args)


if __name__ == "__main__":
    func(4, 4, 4)
