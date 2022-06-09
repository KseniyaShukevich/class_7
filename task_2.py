from abc import ABC, abstractmethod


class Clothes(ABC):
    all_expense = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.all_expense += self.expense

    def __str__(self):
        return f'Пальто.\nРазмер: {self.size}.\nРасход: {format(self.expense, ".2f")}.\
        \nВесь расход: {format(Coat.all_expense, ".2f")}.\n'

    @property
    def expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.all_expense += self.expense

    def __str__(self):
        return f'Костюм.\nРазмер: {self.height}.\nРасход: {format(self.expense, ".2f")}.\
        \nВесь расход: {format(Suit.all_expense, ".2f")}.\n'

    @property
    def expense(self):
        return self.height * 2 + 0.3


coat_1 = Coat(10)
coat_2 = Coat(12)
suit_1 = Suit(10)
suit_2 = Suit(12)

print(coat_2)
print(suit_2)
