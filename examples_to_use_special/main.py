from abc import ABC, abstractmethod


class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class name(polygon):
    def noofsides(self):
        print("Pierwsza metoda abstrakcyjna")


R = name()
R.noofsides()
