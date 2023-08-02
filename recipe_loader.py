from exceptions import RECIPE_EXCEPTIONS
from recipe import Recipe

def get_recipes():
    filelist = []
    recipe_list = []
    try:
        import os
        paths = [os.getcwd() + "/recipe"]
        while not len(paths) == 0:
            actual_path = paths.pop()
            print(actual_path)
            filelist = filelist + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".recipe")]
            paths = paths + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if f not in RECIPE_EXCEPTIONS and not os.path.isfile(os.path.join(actual_path, f))]
    except:
        filelist = []
    for path in filelist:
        with open(path) as file:
            f = file.readlines()
        for i in f:
            e = i.split()
            for j in range(len(e)):
                if e[j] == "":
                    e.remove("")
                    j -= 1
            if len(e) == 2:
                recipe_list.append(Recipe())
            else:
                import sys
                print(f"La ligne \"{i}\" est invalide est n'a donc pas été chargée", file = sys.stderr)
    if len(recipe_list) < 1:
        import sys
        print("Aucune recette trouvée", file=sys.stderr)
    return recipe_list
