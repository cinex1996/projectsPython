import random


def randomnumber() -> int:
    Randomnumber = random.randrange(1, 3)
    return Randomnumber


def savefile() -> str:
    f = open("file.txt", "w")
    f.write(str(randomnumber()))
    f.close()


def maingame():
    while True:
        numbersecond = random.randrange(1,3)
        print(numbersecond)
        numbersecond=str(numbersecond)
        f = open("file.txt", "r")
        number = f.read()
        if numbersecond == number:
            print("Zgadłeś")
            break
        else:
            print("Przegrałeś")


def main():
    savefile()
    maingame()


if __name__ == "__main__":
    main()
