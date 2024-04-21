from BankAccount import BankAccount


def main():
    Dava = BankAccount(12, "Marcin", 100)
    while True:
        print("Witam Panie ", Dava.name, " w czym możemy panu pomóc ")
        print("1-wpłacanie peniędzy do depozytu")
        print("2-wypłacanie pieniędzy z konta")
        print("3-zmiana imienia właściciela konta ")
        print("4-Wyświetlenie swoich informacji")
        print("5-Wyloguj się ze swojego konta bankowego")
        choice = int(input("Pana wybór: \n"))
        if choice == 1:
            deposit = Dava.deposit()
            print("Wpłaciłeś na swoje konto: \n")
            print(deposit)
        elif choice == 2:
            withdraw = Dava.withdraw()
            print(withdraw)
        elif choice == 3:
            changename = Dava.change_ownershitp()
            print(changename)
        elif choice == 4:
            Dava.display()
        elif choice == 5:
            print("Wylogowanie się z konta bankowego")
            break


if __name__ == "__main__":
    main()
