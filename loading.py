from print_clearable import print, clear, clear_cache

def print_percent(percent, file=None):
    if percent < 30:
        color = "\033[31m"
    elif percent < 50:
        color = "\033[33m"
    elif percent < 70:
        color = "\033[93m"
    elif percent < 95:
        color = "\033[32m"
    else:
        color = "\033[92m"

    import os
    try:
        width = os.get_terminal_size().columns - 1
    except:
        width = 1080

    string_end = f" {percent} %"
    string_start = "=" * int(percent / 100 * (width - len(string_end))) + ">"
    string = " " * (width - (len(string_end) + len(string_start)))
    string_bar = string_start + string
    print(color, string_bar[:-1] + "|" + string_end, "\033[0m", sep="", end="\n", file=file, flush=True)

class Loading:
    def __init__(self, valeur_initiale=0, file=None):
        self._valeur = valeur_initiale
        self.file = file
        self.ligne_precedente_effacee = False

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, nouvelle_valeur):
        self._valeur = nouvelle_valeur
        if self._valeur > 0 and not self.ligne_precedente_effacee:
            clear(self.file)
        print_percent(self._valeur, self.file)
        if self._valeur >= 100:
            clear_cache(self.file)
        self._valeur = nouvelle_valeur

global LOADING