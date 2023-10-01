from loading import Loading
LOAD = Loading()
NUMBER_OF_LOADING_STEP = 3
from loader import get_recipes
recipes = get_recipes()
LOAD.valeur = 100/NUMBER_OF_LOADING_STEP * 1
from loader import get_crafter
crafters = get_crafter()
LOAD.valeur = 100/NUMBER_OF_LOADING_STEP * 2
from loader import get_inv
inventory = get_inv()
LOAD.valeur = 100/NUMBER_OF_LOADING_STEP * 3

print(recipes, crafters, inventory, sep="\n")

def find_best_recipe(ressource:str, quantity:int=1):
    possible_recipes = []
    for r in recipes:
        if r.produce(ressource):
            possible_recipes.append(r)
    #Add the crafters results to it
    #Find the fastest
    #Calculate the best recipe

print("\n\n\n\n", recipes[0].infos())