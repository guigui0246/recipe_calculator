class Crafter():
    def __init__(self, path:str, line:str) -> None:
        from default import DEFAULT_CRAFTER_DESCRIPTION
        import os
        self.name = path.removeprefix(os.getcwd()).replace("\\",".").replace("/",".").removesuffix(".crafter").removeprefix(".")
        self.info = line
        self.crafter = ""
        self.ressources = {}
        self.results = {}
        self.duration = 0
        self.speed = 1
        self._load()
        try:
            self.description
        except:
            from stime import sec_to_time
            self.description = DEFAULT_CRAFTER_DESCRIPTION.format(self.name, self.ressources, self.results, self.speed, self.duration, ("+" + sec_to_time(self.duration)) if self.duration >= 0 else ("-" + sec_to_time(-self.duration)))


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
            if i.startswith("Speed:") or i.startswith("Duration:"):
                last = "speed"
                e = i.removeprefix("Speed:").removeprefix("Duration:").strip()
                if e.startswith("+"):
                    import stime
                    self.duration += stime.time_to_sec(e[1:].strip())
                elif e.startswith("-"):
                    import stime
                    self.duration -= stime.time_to_sec(e[1:].strip())
                else:
                    for l in e.split("x"):
                        try:
                            self.speed *= float(l.strip())
                        except:
                            pass
        try:
            self.description.strip()
            while len(self.description) > 0 and self.description[-1] == '\n':
                self.description = self.description[:-1]
            self.description.strip()
        except AttributeError:
            pass

    def __repr__(self) -> str:
        return f"{self.name}"

    def infos(self) -> str:
        return self.description
