import random

from Card import Card


def _create_cards() -> list[Card]:
    emptytable=[]
    for i in range(len(card.valuescards)):
        for a in range(len(figurecards)):
            new_card=Card(a,i)
            emptytable.append(new_card)
    return emptytable


class Deck:
    card=Card()
    def __init__(self):
        self.cards = _create_cards()

    def shuffe(self, table):
        random.shuffle(table)
        return table

    def deal(self, table):
        print("Usunięta wartość ", table.pop(-1))
        print(table[-1])
        return table
