original_print = print
from sys import stdout
from typing import Generic, Literal, TextIO, TypeVar
global PRINT_BUFFER
PRINT_BUFFER = {}
LAST_END = {}
TextIO = TypeVar('TextIO')
class SupportsWrite(Generic[TextIO]):
    pass

def print(*args, sep:str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False, **kwargs):
    global PRINT_BUFFER
    global LAST_END
    if file == None:
        file = stdout
    if LAST_END.get(file, False):
        string = '\n'
    else:
        string = ''
    for i,e in enumerate(args):
        if isinstance(e, str):
            string += e
            continue
        string += str(e)
        if i != len(args) - 1 :
            string += sep if sep else ""
    if end != "\n":
        string += end if end else ""
        LAST_END[file] = False
    else:
        LAST_END[file] = True
    if file in PRINT_BUFFER.keys():
        PRINT_BUFFER[file] += string
    else:
        PRINT_BUFFER[file] = string
    return original_print(string, sep=None, end="", flush=kwargs["flush"] if "flush" in kwargs.keys() else False, file=file)

def clear(file:SupportsWrite[str]|None=None):
    global PRINT_BUFFER
    global LAST_END
    if file == None:
        file = stdout
    if not file in PRINT_BUFFER.keys():
        return
    original_print("\b" * len(PRINT_BUFFER[file]), end="")
    original_print(" " * len(PRINT_BUFFER[file]), end="")
    original_print("\b" * len(PRINT_BUFFER[file]), end="")
    del LAST_END[file]
    del PRINT_BUFFER[file]

def clear_cache(file:SupportsWrite[str]|None=None, all:bool=False):
    global PRINT_BUFFER
    global LAST_END
    if all:
        for i in list(PRINT_BUFFER.keys()):
            try:
                del PRINT_BUFFER[i]
                if LAST_END[i]:
                    original_print("", file=i)
                del LAST_END[i]
            except:
                pass
        return
    if file == None:
        file = stdout
    if file in PRINT_BUFFER.keys():
        del PRINT_BUFFER[file]
        if LAST_END[file]:
            original_print("", file=i)
        del LAST_END[file]

import atexit
atexit.register(clear_cache, [], {all:True})