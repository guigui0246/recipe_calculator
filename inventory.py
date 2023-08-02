class Item():
    def __init__(self, name:str, quantity:int=1) -> None:
        self.name = name
        self.n = quantity

    def __repr__(self) -> str:
        return f"{self.n}x{self.name}"

    def __add__(self, other):
        self.n += other
        return self

    def __sub__(self, other):
        self.n -= other
        return self

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.n

class Inventory():
    pass

class Inventory():
    def __init__(self) -> None:
        self.content = []

    def __repr__(self) -> str:
        return "{\n" + str(self.content).replace(", ", "\n").removeprefix("[").removesuffix("]") + "\n}\n"

    def sub(self, Item:Item) -> None:
        name = Item.get_name()
        for e in self.content:
            if type(e) == Item and e.get_name() == name:
                e -= Item.get_quantity()
                return
        self.content.append(Item)

    def add(self, Item:Item) -> None:
        name = Item.get_name()
        for e in self.content:
            if type(e) == Item and e.get_name() == name:
                e += Item.get_quantity()
                return
        self.content.append(Item)

    def __add__(self, other:Inventory) -> Inventory:
        self.add(other)
        return self

    def __sub__(self, other:Inventory) -> Inventory:
        self.sub(other)
        return self
