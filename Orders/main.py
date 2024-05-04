class Order:
    def __init__(self, count, name, price, howmany):
        self.count = count
        self.name = name
        self.price = price
        self.howmany = howmany


class Manager:
    dictionary = {}
    count = 0
    number = 0

    def add_order(self):
        while True:
            self.count += 1
            self.number += 1
            name = input("Podaj nazwę produktu")
            price = int(input("Podaj cenę produktu"))
            howmany = int(input("Podaj ilość tego produktu"))
            new_Order = Order(str(self.count), name, str(price), str(howmany))
            self.dictionary.update(
                {"Id": new_Order.count, "name": new_Order.name, "price": new_Order.price, "Howmany":
                    new_Order.howmany})
            stop = input("Przerwać działanie programu y/n")
            if stop == 'y':
                break

            print({"Id": new_Order.count, "name": new_Order.name, "price": new_Order.price, "Howmany":
                new_Order.howmany})

    def viev_dictionary(self):
        for key, value in self.dictionary.items():
            print(f"{key}: {value}")

    def remove(self, id_to_sell):
        for ordinary in self.dictionary:
            if ordinary == id_to_sell:
                self.dictionary[ordinary] -= 1


manager = Manager()
manager.add_order()
