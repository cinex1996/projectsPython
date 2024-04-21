class BankAccount:
    def __init__(self, number_account, name_owner, your_money):
        self.number = number_account
        self.name = name_owner
        self.money = your_money

    def deposit(self) -> int:
        deposit = int(input("Jaką kwotę chcesz wpłacić na swoje konto bankowe"))
        self.money = self.money + deposit - 2
        return self.money

    def withdraw(self):
        withdraw = int(input("Jaką kwotę chcesz wypłacić ze swojego konta bankowego "))
        if withdraw > self.money:
            print("Przykro mi nie możemy wypłacić twoich pieniedzy ponieważ masz niewystarczającą ilośc")
        else:
            self.money = self.money - withdraw
        print(self.money)

    def change_ownershitp(self) -> str:
        name = input("Podaj nowe imie właściciela konta bankowego ")
        self.name = name
        return self.name

    def display(self):
        print("Właściciel konto to ", self.name, " numer jego konta to ", self.number, "Stan jego konta wynosi na "
                                                                                       "chilę obecną ", self.money)
