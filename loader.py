def get_recipes():
    from exceptions import RECIPE_EXCEPTIONS
    from recipe import Recipe
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
        recipe_list.append(Recipe(path, f))
    if len(recipe_list) < 1:
        import sys
        print("Aucune recette trouvée", file=sys.stderr)
    return recipe_list

def get_crafter():
    from exceptions import CRAFTER_EXCEPTIONS
    from crafter import Crafter
    filelist = []
    crafter_list = []
    try:
        import os
        paths = [os.getcwd() + "/crafter"]
        while not len(paths) == 0:
            actual_path = paths.pop()
            print(actual_path)
            filelist = filelist + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".crafter")]
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
