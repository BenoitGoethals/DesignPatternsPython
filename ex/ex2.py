import decimal
from decimal import Decimal
from typing import Protocol


class Menu(Protocol):

    def get_price(self) -> Decimal:
        pass

    def describe(self) -> str:
        pass


class MenuItem(Menu):

    def __init__(self, name_menu: str, price: Decimal = Decimal(0)):
        self.name_menu = name_menu
        self.price = price

    def get_price(self) -> Decimal:
        return self.price

    def describe(self) -> str:
        return self.name_menu


class MenuSection(Menu):

    def __init__(self, name_menu: str = ""):
        self._name_menu = name_menu
        self._items: list[Menu] = []

    def add(self, menu: Menu) -> None:
        self._items.append(menu)

    def get_price(self) -> Decimal:
        return sum((item.get_price() for item in self._items), start=Decimal(0))

    def describe(self) -> str:
        return f"Menu Section: {self._name_menu}"


if __name__ == "__main__":
    menu = MenuSection("test")
    item1 = MenuItem("Vlss", Decimal(10))
    menu.add(item1)
    item2 = MenuItem("asdsa", Decimal(10))
    menu.add(item2)

    print(menu.describe())
    print(menu.get_price())
