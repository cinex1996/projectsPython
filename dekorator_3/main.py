def count(func):
    dictionary = {"Liczba wywołanej funkcji ": 0}

    def function():
        func()
        value = dictionary.get("Liczba wywołanej funkcji ")
        howmany = value + 1
        dictionary.update({"Liczba wywołanej funkcji ": howmany})
        print(dictionary)

    return function


@count
def main():
    print("Cześć")


@count
def number():
    pass


if __name__ == "__main__":
    main()
    main()
    main()
    main()
    main()
    number()