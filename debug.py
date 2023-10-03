import os.path
def debug(*args, **kwargs):
    with open(os.path.join(".", "debug.log"), "a") as f:
        return print("\"\"\"", *args, "\"\"\"", **kwargs, file=f)