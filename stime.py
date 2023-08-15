from const import DAY_STRING
from const import HOUR_STRING
from const import MINUTE_STRING
from const import SECONDE_STRING
import re
reg = f"(\d*{DAY_STRING})?(\d*{HOUR_STRING})?(\d*{MINUTE_STRING})?(\d*(?:\.|\,)?\d*{SECONDE_STRING})?"
pattern = re.compile(reg, re.IGNORECASE)
from const import SECONDES_PER_MINUTES
from const import MINUTES_PER_HOURS
from const import HOURS_PER_DAY

def sec_to_time(time:float) -> str:
    day = 0
    hou = 0
    min = 0
    sec = time % SECONDES_PER_MINUTES
    time -= sec
    if (time > 0):
        time /= SECONDES_PER_MINUTES
        min = time % MINUTES_PER_HOURS
        time -= min
        if (time > 0):
            time /= MINUTES_PER_HOURS
            hou = time % HOURS_PER_DAY
            time -= hou
            if (time > 0):
                time /= HOURS_PER_DAY
                day = time
    if (sec == min == hou == day == 0):
        return "no time"
    return f"{f'{day:g}{DAY_STRING}' if (day > 0) else ''}{f'{hou:g}{HOUR_STRING}' if (hou > 0) else ''}{f'{min:g}{MINUTE_STRING}' if (min > 0) else ''}{f'{sec:g}{SECONDE_STRING}' if (sec > 0) else ''}"

def time_to_sec(time:str) -> float:
    test = 0
    value = 0
    for elem in pattern.findall(time):
        if (elem == ('', '', '', '')):
            continue
        if (test > 0):
            raise ValueError(f"Multiple time values at {time}\nThese values are :\n{pattern.findall(time)[:-1]}\n")
        test+=1
        value += int(elem[0][:-len(DAY_STRING)])*HOURS_PER_DAY*MINUTES_PER_HOURS*SECONDES_PER_MINUTES if not elem[0] == '' else 0
        value += int(elem[1][:-len(HOUR_STRING)])*MINUTES_PER_HOURS*SECONDES_PER_MINUTES if not elem[1] == '' else 0
        value += int(elem[2][:-len(MINUTE_STRING)])*SECONDES_PER_MINUTES if not elem[2] == '' else 0
        value += float(elem[3][:-len(SECONDE_STRING)]) if not elem[3] == '' else 0
    return value
