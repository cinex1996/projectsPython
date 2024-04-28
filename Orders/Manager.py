from Order import Order


class Manager:
    dictionary = {}
    id = 0

    def askuser(self):
        while True:
            product = input("Nazwa produktu")
            howmanyproduct = int(input("Podaj ilość produktów"))
            priceproduct = int(input("Podaj cenę za sztukę"))
            self.id += 1
            if product in self.dictionary:
                x = self.dictionary.get(product)
                howmanyproduct = howmanyproduct + x
                self.dictionary.update({product: howmanyproduct})
                print(self.dictionary)
            else:
                self.dictionary.update({"id_produktu": self.id, product: howmanyproduct, "Cena za produkt": priceproduct})
                print(self.dictionary)


def main():
    manager = Manager()
    manager.askuser()
    print(manager.dictionary)


if __name__ == "__main__":
    main()
