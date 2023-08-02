from loader import get_recipes
recipes = get_recipes()
from loader import get_crafter
crafters = get_crafter()
from loader import get_inv
inventory = get_inv()

print(recipes, crafters, inventory, sep="\n")

def find_best_recipe(ressource:str, quantity:int=1):
    possible_recipes = []
    for r in recipes:
        if r.result == ressource:
            possible_recipes.append(r)
    #Add the crafters results to it
    #Find the fastest
    #Calculate the best recipe

print("\n\n\n\n", recipes[0].infos())