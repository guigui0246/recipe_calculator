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
        self.crafter:list[str] = []
        self._load()
        try:
            self.description
        except:
            from stime import sec_to_time
            self.description = DEFAULT_RECIPE_DESCRIPTION.format(self.name, self.ressources, self.results, self.crafter, "" if self.crafter_needed else "not", sec_to_time(self.duration))

    def _load(self):
        last=""
        for i in self.info.splitlines():
            i = i.strip()
            if i.startswith("Description:") or (last == "description" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Crafter needed:") and not i.startswith("Duration:")):
                try:
                    self.description += i.removeprefix("Description:").strip() + "\n"
                except AttributeError:
                    self.description = i.removeprefix("Description:").strip() + "\n"
                last = "description"
            if i == "":
                continue
            if i.strip() == "Crafter needed":
                self.crafter_needed = True
            if i.startswith("Name:"):
                self.name = i.removeprefix("Name:").strip()
                last = "name"
            if i.startswith("Ressources:") or (last == "ressource" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Crafter needed:") and not i.startswith("Duration:")):
                last = "ressource"
                from loader import separate_number_name
                key,value = separate_number_name(i.removeprefix("Ressources:").strip())
                try:
                    self.ressources[key] += value
                except KeyError:
                    self.ressources[key] = value
            if i.startswith("Result:") or (last == "result" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Crafter needed:") and not i.startswith("Duration:")):
                last = "result"
                from loader import separate_number_name
                key,value = separate_number_name(i.removeprefix("Result:").strip())
                try:
                    self.results[key] += value
                except KeyError:
                    self.results[key] = value
            if i.startswith("Crafter:") or (last == "crafter" and not i.startswith("Name:") and not i.startswith("Ressources:") and not i.startswith("Result:") and not i.startswith("Crafter:") and not i.startswith("Crafter needed:") and not i.startswith("Duration:")):
                last = "crafter"
                liste = i.removeprefix("Crafter:").strip().split(",")
                for e in liste:
                    if ";" in e:
                        liste.remove(e)
                        liste += e.strip().split(";")
                self.crafter += liste
            if i.startswith("Crafter needed:"):
                last = "crafter_need"
                if (i.removeprefix("Crafter needed:").strip() == "False") or (i.removeprefix("Crafter needed:").strip() == "0"):
                    self.crafter_needed = False
                else:
                    self.crafter_needed = bool(i.removeprefix("Crafter needed:").strip())
            if i.startswith("Duration:"):
                last = "duration"
                import stime
                self.duration = stime.time_to_sec(i.removeprefix("Duration:").strip())
        try:
            self.description.strip()
            if len(self.description) > 0 and self.description[-1] == '\n':
                self.description = self.description[:-1]
        except AttributeError:
            pass
        for i in range(len(self.crafter)):
            self.crafter[i] = self.crafter[i].strip()
        while "" in self.crafter:
            self.crafter.remove("")

    def __repr__(self) -> str:
        return f"{self.name}"

    def infos(self) -> str:
        return self.description

    def produce(self, ressource:str|None=None) -> bool | dict[str, float]:
        "Return if a ressource is produced. If ressource is None return the dict of produced ressources"
        if ressource == None:
            dct = {}
            for i in self.results.keys():
                dct[i] = self.results[i]
            for i in self.ressources.keys():
                try:
                    dct[i] -= self.ressources[i]
                except KeyError:
                    dct[i] = -self.ressources[i]
            for i in dct.keys():
                if dct[i] <= 0:
                    dct.pop(i)
            return dct
        try:
            self.results[ressource]
        except KeyError:
            return False
        if self.results[ressource] <= 0:
            return False
        try:
            self.ressources[ressource]
        except KeyError:
            return True
        else:
            return self.results[ressource] > self.ressources[ressource]

    def uses(self, ressource:str|None=None) -> bool | dict[str, float]:
        "Return if a ressource is used. If ressource is None return the dict of used ressources"
        if ressource == None:
            dct = {}
            for i in self.ressources.keys():
                dct[i] = self.ressources[i]
            for i in self.results.keys():
                try:
                    dct[i] -= self.results[i]
                except KeyError:
                    dct[i] = -self.results[i]
            for i in dct.keys():
                if dct[i] <= 0:
                    dct.pop(i)
            return dct
        try:
            self.ressources[ressource]
        except KeyError:
            return False
        if self.ressources[ressource] <= 0:
            return False
        try:
            self.results[ressource]
        except KeyError:
            return True
        else:
            return self.results[ressource] < self.ressources[ressource]