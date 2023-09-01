if __name__ == "__main__":
    RULES:list[str] = [
    ]

    if len(RULES) == 0:
        exit()

    import sys
    import os
    try:
        filelist = []
        paths = [os.getcwd()]
        while not len(paths) == 0:
            actual_path = paths.pop()
            filelist = filelist + [os.path.join(actual_path, f).removeprefix(os.getcwd()).removesuffix(".py").removeprefix("\\") for f in os.listdir(actual_path) if os.path.isfile(os.path.join(actual_path, f)) and f.endswith(".py")]
            paths = paths + [os.path.join(actual_path, f) for f in os.listdir(actual_path) if not os.path.isfile(os.path.join(actual_path, f))]
    except:
        filelist = []

    import_str = ""

    for i in filelist:
        if "test" in i:
            continue
        if "cache" in i:
            continue
        if "log" in i:
            continue
        import_str = import_str + f"from {i} import *\n"

    test = {}
    pass_count = 0
    test_output = ""

    log = open(os.path.join(os.getcwd(), "custom_tests.log"), "a")
    sys.stdout = sys.stderr = log
    for i in RULES:
        try:
            exec(import_str + f"test = ({i})", globals(), test)
            test_output = test_output + (f"\033[92mRule \"{i}\" passed\033[0m\n" if test["test"] else f"\033[31mRule \"{i}\" failed\033[0m\n")
            if test["test"]:
                pass_count += 1
        except:
            test_output = test_output + (f"\033[31mRule \"{i}\" crashed\033[0m\n")
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    print(test_output)

    percent = pass_count / len(RULES) * 100

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

    width = os.get_terminal_size().columns - 1

    string_end = f" {percent} %"
    string_start = "=" * int(percent / 100 * (width - len(string_end))) + ">"
    string = " " * (width - (len(string_end) + len(string_start)))
    string_bar = string_start + string
    print(color, end="")
    print(string_bar[:-1] + "|" + string_end, end="")
    print("\033[0m", end="\n")

