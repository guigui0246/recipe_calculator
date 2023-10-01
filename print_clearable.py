original_print = print
original_input = input
import io
from sys import stdout, stdin, stderr
from typing import Generic, Literal, TextIO, TypeVar
TextIO = TypeVar('TextIO')
class SupportsWrite(Generic[TextIO]):
    pass

global PRINT_BUFFER
PRINT_BUFFER:dict[SupportsWrite,str] = {}

def print(*args, sep:str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False, **kwargs):
    global PRINT_BUFFER
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
    return original_print(string, sep=None, end="", flush=flush, file=file)

def input(__prompt, **kwargs):
    global PRINT_BUFFER
    string = ''
    if isinstance(__prompt, str):
        string += __prompt
    else:
        string += str(__prompt)
    if stdout in PRINT_BUFFER.keys():
        PRINT_BUFFER[stdout] += string
    else:
        PRINT_BUFFER[stdout] = string
    try:
        ret = original_input(string, **kwargs)
    except EOFError:
        return None
    if stdin in PRINT_BUFFER.keys():
        PRINT_BUFFER[stdin] += ret+"\n"
    else:
        PRINT_BUFFER[stdin] = ret+"\n"
    return ret

def clear(file:SupportsWrite[str]|None=None, remove_errors:bool=False):
    global PRINT_BUFFER
    if file == None:
        file = stdout
    if not file in PRINT_BUFFER.keys():
        return
    try:
        original_print("\033[F\033[K\r" * PRINT_BUFFER[file].count("\n"), file=file, end="")
    except io.UnsupportedOperation:
        original_print("\033[F\033[K\r" * PRINT_BUFFER[file].count("\n"), file=stdout, end="")
        if not remove_errors:
            original_print(RuntimeWarning("File could not be written for clear! Using stdout."), file=stderr)
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