from exceptions import RECIPE_EXCEPTIONS
from recipe import Recipe

def get_recipes() -> list[Recipe]:
    filelist = []
    recipe_list = []
    try:
        import os
        paths = [os.getcwd() + "/recipe"]
        while not len(paths) == 0:
            actual_path = paths.pop()
            filelist = filelist + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".recipe") and f not in RECIPE_EXCEPTIONS]
            paths = paths + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if f not in RECIPE_EXCEPTIONS and not os.path.isfile(os.path.join(actual_path, f))]
    except:
        filelist = []
    for path in filelist:
        with open(path) as file:
            f = file.readlines()
        recipe_list.append(Recipe(path, f))
    if len(recipe_list) < 1:
        import sys
        print("Aucune recette trouvée", file=sys.stderr)
    return recipe_list

from exceptions import CRAFTER_EXCEPTIONS
from crafter import Crafter

def get_crafter() -> list[Crafter]:
    filelist = []
    crafter_list = []
    try:
        import os
        paths = [os.getcwd() + "/crafter"]
        while not len(paths) == 0:
            actual_path = paths.pop()
            filelist = filelist + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".crafter") and f not in CRAFTER_EXCEPTIONS]
            paths = paths + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if f not in CRAFTER_EXCEPTIONS and not os.path.isfile(os.path.join(actual_path, f))]
    except:
        filelist = []
    for path in filelist:
        with open(path) as file:
            f = file.readlines()
        crafter_list.append(Crafter(path, f))
    if len(crafter_list) < 1:
        import sys
        print("Aucune machine trouvée", file=sys.stderr)
    return crafter_list

from exceptions import INVENTORY_EXCEPTIONS
from inventory import Inventory
from inventory import Item

def separate_number_name(string:str):
    string = string.replace(" ", "").replace("\n", "")
    a = 0
    b = 0
    c = 0
    number = 1
    start = False
    end = False
    tmp = ""
    while string[0].isdigit():
        a = a*10 + int(string[0])
        start = True
        tmp += string[0]
        string = string[1:]
    if start and string[0] == "x":
        string = string[1:]
        number *= a
    else:
        string = tmp + string
    del tmp
    tmp = ""
    while string[-1].isdigit():
        b = b + int(string[-1]) * (10 ** c)
        c += 1
        end = True
        tmp += string[-1]
        string = string[:-1]
    if end and string[-1] == "x":
        string = string[:-1]
        number *= b
    else:
        string = string + tmp
    return string, number

def get_inv() -> Inventory:
    inventory = Inventory()
    with open("inventory.item") as file:
        f = file.readlines()
        for e in f:
            try:
                inventory.add(Item(*separate_number_name(e)))
            except:
                continue
    return inventory