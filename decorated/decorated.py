def make_decorated(func):
    def inner():
        print("Got decorated")
        func()

    return inner


@make_decorated
def ordinary():
    print("I am ordinary")


ordinary()
