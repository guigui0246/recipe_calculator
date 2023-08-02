class Crafter():
    def __init__(self, path:str, line:str) -> None:
        import os
        self.name = path.removeprefix(os.getcwd()).replace("\\",".").replace("/",".").removesuffix(".crafter").removeprefix(".")
        self.info = line
        pass

    def __repr__(self) -> str:
        return f"{self.name}"