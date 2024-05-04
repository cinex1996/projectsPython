import time


def timethis(func):
    def timeview():
        start = time.time()
        func()
        time.sleep(1)
        end = time.time()
        print("Czas trwania funkcji ", end - start)

    return timeview


@timethis
def timefunction():
    print("Czas trwania")


@property
def function():
    print("Test")


if __name__ == "__main__":
    timefunction()
    function()