from loader import get_recipes
recipes = get_recipes()
from loader import get_crafter
crafters = get_crafter()
from loader import get_inv
inventory = get_inv()

print(recipes, crafters, inventory, sep="\n")

def find_best_recipe(ressource:str):
    pass
