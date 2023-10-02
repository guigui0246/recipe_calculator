class Crafter():
    def __init__(self, path:str, line:str) -> None:
        import os
        self.name = path.removeprefix(os.getcwd()).replace("\\",".").replace("/",".").removesuffix(".crafter").removeprefix(".")
        self.info = line
        self.crafter = ""
        self.ressources = {}
        self.results = {}
        self.duration = 0
        self.speed = 1
        self._load()

    def _load(self):
        last=""
        for i in self.info.splitlines():
            i = i.strip()
            if i.startswith("Description:") or (last == "description" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Speed:")):
                try:
                    self.description += i.removeprefix("Description:").strip() + "\n"
                except AttributeError:
                    self.description = i.removeprefix("Description:").strip() + "\n"
                last = "description"
            if i == "":
                continue
            if i.startswith("Name:"):
                self.name = i.removeprefix("Name:").strip()
                last = "name"
            if i.startswith("Ressources:") or (last == "ressource" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Speed:")):
                last = "ressource"
                from loader import separate_number_name
                key,value = separate_number_name(i.removeprefix("Ressources:").strip())
                try:
                    self.ressources[key] += value
                except KeyError:
                    self.ressources[key] = value
            if i.startswith("Result:") or (last == "result" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Speed:")):
                last = "result"
                from loader import separate_number_name
                key,value = separate_number_name(i.removeprefix("Result:").strip())
                try:
                    self.results[key] += value
                except KeyError:
                    self.results[key] = value
            if i.startswith("Crafter:"):
                if self.crafter != "":
                    raise SyntaxError("multiple ids for the same crafter")
                last = "crafter"
                self.crafter = i.removeprefix("Crafter:").strip()
            if i.startswith("Speed:"):
                last = "speed"
                e = i.removeprefix("Speed:").strip()
                if e.startswith("+"):
                    import stime
                    self.duration += stime.time_to_sec()
                elif e.startswith("-"):
                    import stime
                    self.duration -= stime.time_to_sec()
                else:
                    for l in e.split("x"):
                        try:
                            self.speed *= float(l)
                        except:
                            pass
        try:
            self.description.strip()
        except AttributeError:
            pass

    def __repr__(self) -> str:
        return f"{self.name}"

    def infos(self) -> str:
        return self.description
