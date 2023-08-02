class Recipe():
    def __init__(self, path:str, line:str) -> None:
        from default import DEFAULT_RECIPE_DESCRIPTION
        import os
        self.name = path.removeprefix(os.getcwd()).replace("\\",".").replace("/",".").removesuffix(".recipe").removeprefix(".")
        self.info = line
        self.ressources = {}
        self.results = {}
        self.duration = 0
        self.crafter_needed = False
        self.crafter = {}
        from stime import sec_to_time
        self.description = DEFAULT_RECIPE_DESCRIPTION.format(self.name, self.ressources, self.results, self.crafter, "" if self.crafter_needed else "not", sec_to_time(self.duration))
        pass

    def __repr__(self) -> str:
        return f"{self.name}"

    def infos(self) -> str:
        return self.description