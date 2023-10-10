import pytest
from inventory import Inventory, Item
import os

#
# Item
#

@pytest.mark.item
def test_create_empty_item():
    assert Item("").n == 1
    assert Item("").name == ""

@pytest.mark.item
def test_create_named_item():
    assert Item("This is a name").name == "This is a name"

@pytest.mark.item
def test_create_number_of_item():
    assert Item("name", 5).n == 5
    assert Item("name", -5).n == -5
    assert Item("name", 0).n == 0

@pytest.mark.item
def test_repr_of_item():
    assert repr(Item("name", 3)) == "3xname"
    assert str(Item("name", 3)) == "3xname"

@pytest.mark.item
def test_get_methods_of_item():
    import random
    number = random.randint(-100, 100)
    assert Item("name", number).n == Item("name", number).get_quantity()
    assert Item("name", number).name == Item("name", number).get_name()

@pytest.mark.item
def test_add_of_item():
    import random
    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    assert (Item("name", number1)+number2).n == number1 + number2

@pytest.mark.item
def test_sub_of_item():
    import random
    number1 = random.randint(-100, 100)
    number2 = random.randint(-100, 100)
    assert (Item("name", number1)-number2).n == number1 - number2

@pytest.mark.item
def test_count():
    import loader
    loader.INVENTORY_EXCEPTIONS = []
    assert loader.separate_number_name("name") == ("name", 1)
    assert loader.separate_number_name("2xname2x3") == ("name2", 6)
    assert loader.separate_number_name("2xname2") == ("name2", 2)
    assert loader.separate_number_name("name3x1x1") == ("name3x1", 1)
    loader.INVENTORY_EXCEPTIONS = ["name"]
    with pytest.raises(PermissionError):
        loader.separate_number_name("name")
    loader.INVENTORY_EXCEPTIONS = []

#
# Inventory
#

@pytest.mark.inventory
def test_create_empty_inventory():
    assert type(Inventory().content) == type([])
    assert len(Inventory().content) == 0

def test_repr_inventory():
    assert repr(Inventory()) == "{\n" + str([]).replace(", ", "\n").removeprefix("[").removesuffix("]") + "\n}\n"
    assert str(Inventory()) == "{\n" + str([]).replace(", ", "\n").removeprefix("[").removesuffix("]") + "\n}\n"
    inv = Inventory()
    inv.add(Item("name", 3))
    inv.add(Item("name2", 1))
    assert repr(inv) == "{\n" + str([Item("name", 3), Item("name2", 1)]).replace(", ", "\n").removeprefix("[").removesuffix("]") + "\n}\n"
    assert str(inv) == "{\n" + str([Item("name", 3), Item("name2", 1)]).replace(", ", "\n").removeprefix("[").removesuffix("]") + "\n}\n"

def test_add_inv():
    inv = Inventory()
    inv.add(Item("name", 3))
    inv.add(Item("name2", 1))
    assert str(inv.content) == str([Item("name", 3), Item("name2", 1)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv.add(Item("name", -1))
    assert str(inv.content) == str([Item("name", 2)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv2 = Inventory()
    inv2.add(Item("name2", 1))
    inv += inv2
    assert str(inv.content) == str([Item("name", 3), Item("name2", 1)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv2 = Inventory()
    inv2.add(Item("name", 1))
    inv += inv2
    assert str(inv.content) == str([Item("name", 4)])

def test_sub_inv():
    inv = Inventory()
    inv.add(Item("name", 3))
    inv.sub(Item("name2", 1))
    assert str(inv.content) == str([Item("name", 3), Item("name2", -1)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv.sub(Item("name", 1))
    assert str(inv.content) == str([Item("name", 2)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv2 = Inventory()
    inv2.sub(Item("name2", 1))
    inv -= inv2
    assert str(inv.content) == str([Item("name", 3), Item("name2", 1)])
    inv = Inventory()
    inv.add(Item("name", 3))
    inv2 = Inventory()
    inv2.add(Item("name", 1))
    inv -= inv2
    assert str(inv.content)== str([Item("name", 2)])

def test_iter_inv():
    inv = Inventory()
    i = Item("name", 3)
    i2 = Item("name2", 1)
    inv.add(i)
    inv.add(i2)
    assert list(iter(inv)) == list(iter([i, i2]))


