import re
reg = r"(\d*d)?(\d*h)?(\d*m)?(\d*(?:\.|\,)?\d*s)?"
pattern = re.compile(reg, re.IGNORECASE)

def sec_to_time(time:float) -> str:
    day = 0
    hou = 0
    min = 0
    sec = time % 60
    time -= sec
    if (time > 0):
        time /= 60
        min = time % 60
        time -= min
        if (time > 0):
            time /= 60
            hou = time % 24
            time -= hou
            if (time > 0):
                time /= 24
                day = time
    if (sec == min == hou == day == 0):
        return "no time"
    return f"{f'{day:g}d' if (day > 0) else ''}{f'{hou:g}h' if (hou > 0) else ''}{f'{min:g}m' if (min > 0) else ''}{f'{sec:g}s' if (sec > 0) else ''}"

def time_to_sec(time:str) -> float:
    test = 0
    value = float("inf")
    for elem in pattern.findall(time):
        if (elem == ('', '', '', '')):
            continue
        if (test > 0):
            raise ValueError(f"Multiple time value at {time}")
        test+=1
    return value

print(sec_to_time(14770754.15))
print(time_to_sec(sec_to_time(14770754.15)))
print(sec_to_time(time_to_sec("1d1h1m1s")))
print(sec_to_time(time_to_sec("1d1h1s5m")))
