original_print = print
from sys import stdout
from typing import Generic, Literal, TextIO, TypeVar
TextIO = TypeVar('TextIO')
class SupportsWrite(Generic[TextIO]):
    pass

global PRINT_BUFFER
PRINT_BUFFER:dict[SupportsWrite,str] = {}

def print(*args, sep:str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False, **kwargs):
    global PRINT_BUFFER
    global LAST_END
    if file == None:
        file = stdout
    string = ''
    for i,e in enumerate(args):
        if isinstance(e, str):
            string += e
            continue
        string += str(e)
        if i != len(args) - 1 :
            string += sep if sep else ""
    string += end if end else ""
    if file in PRINT_BUFFER.keys():
        PRINT_BUFFER[file] += string
    else:
        PRINT_BUFFER[file] = string
    ret = original_print(string, sep=None, end="", flush=flush, file=file)
    return ret

def clear(file:SupportsWrite[str]|None=None):
    global PRINT_BUFFER
    if file == None:
        file = stdout
    if not file in PRINT_BUFFER.keys():
        return
    original_print("\033[F\033[K\r" * PRINT_BUFFER[file].count("\n"), file=file, end="")
    del PRINT_BUFFER[file]

def clear_cache(file:SupportsWrite[str]|None=None, all:bool=False):
    global PRINT_BUFFER
    if all:
        for i in list(PRINT_BUFFER.keys()):
            try:
                del PRINT_BUFFER[i]
            except:
                pass
        return
    if file == None:
        file = stdout
    if file in PRINT_BUFFER.keys():
        del PRINT_BUFFER[file]

import atexit
atexit.register(clear_cache, [], {all:True})