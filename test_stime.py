import pytest
from const import DAY_STRING
from const import HOUR_STRING
from const import MINUTE_STRING
from const import SECONDE_STRING
from const import SECONDES_PER_MINUTES
from const import MINUTES_PER_HOURS
from const import HOURS_PER_DAY
from const import NO_TIME_STRING

#
#   TIME TO SEC (string to float)
#

from stime import time_to_sec

@pytest.mark.time_to_sec
def test_1_minute_to_sec():
    assert time_to_sec(f"1{MINUTE_STRING}") == SECONDES_PER_MINUTES

@pytest.mark.time_to_sec
def test_1_hour_to_sec():
    assert time_to_sec(f"1{HOUR_STRING}") == SECONDES_PER_MINUTES * MINUTES_PER_HOURS

@pytest.mark.time_to_sec
def test_1_day_to_sec():
    assert time_to_sec(f"1{DAY_STRING}") == SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY

@pytest.mark.time_to_sec
def test_1_sec_to_sec():
    assert time_to_sec(f"1{SECONDE_STRING}") == 1

@pytest.mark.time_to_sec
def test_1515_sec_to_sec():
    assert time_to_sec(f"15.15{SECONDE_STRING}") == 15.15

@pytest.mark.time_to_sec
def test_1_hour_1_sec_to_sec():
    assert time_to_sec(f"1{HOUR_STRING}1{SECONDE_STRING}") == SECONDES_PER_MINUTES * MINUTES_PER_HOURS + 1

@pytest.mark.time_to_sec
def test_1_day_1_minute_to_sec():
    assert time_to_sec(f"1{DAY_STRING}1{MINUTE_STRING}") == SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY + SECONDES_PER_MINUTES

@pytest.mark.time_to_sec
def test_1_day_1_hour_1_minute_1_sec_to_sec():
    assert time_to_sec(f"1{DAY_STRING}1{HOUR_STRING}1{MINUTE_STRING}1{SECONDE_STRING}") == SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY + SECONDES_PER_MINUTES + SECONDES_PER_MINUTES * MINUTES_PER_HOURS + 1

@pytest.mark.time_to_sec
def test_0_to_sec():
    assert time_to_sec("") == 0

@pytest.mark.time_to_sec
def test_neg_to_sec():
    with pytest.raises(ValueError):
        time_to_sec("-1h")

@pytest.mark.time_to_sec
def test_s_not_in_range_to_sec():
    with pytest.raises(ValueError):
        time_to_sec(f"{SECONDES_PER_MINUTES + 1}s")

@pytest.mark.time_to_sec
def test_m_not_in_range_to_sec():
    with pytest.raises(ValueError):
        time_to_sec(f"{MINUTES_PER_HOURS + 15}m")

@pytest.mark.time_to_sec
def test_h_not_in_range_to_sec():
    with pytest.raises(ValueError):
        time_to_sec(f"{HOURS_PER_DAY + 10}h")

@pytest.mark.time_to_sec
def test_multiple_to_sec():
    with pytest.raises(ValueError):
        time_to_sec("1h3m2d1h")

#
#   SEC TO TIME (float to string)
#

from stime import sec_to_time

@pytest.mark.sec_to_time
def test_1_hour_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES * MINUTES_PER_HOURS) == f"1{HOUR_STRING}"

@pytest.mark.sec_to_time
def test_1_minute_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES) == f"1{MINUTE_STRING}"

@pytest.mark.sec_to_time
def test_1_day_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY) == f"1{DAY_STRING}"

@pytest.mark.sec_to_time
def test_1_sec_to_time():
    assert sec_to_time(1) == f"1{SECONDE_STRING}"

@pytest.mark.sec_to_time
def test_0_to_time():
    assert sec_to_time(0) == NO_TIME_STRING

@pytest.mark.sec_to_time
def test_neg_to_time():
    with pytest.raises(ValueError):
        sec_to_time(-1)

@pytest.mark.sec_to_time
def test_1515_sec_to_time():
    assert sec_to_time(15.15) == f"15.15{SECONDE_STRING}"

@pytest.mark.sec_to_time
def test_1_hour_1_sec_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES * MINUTES_PER_HOURS + 1) == f"1{HOUR_STRING}1{SECONDE_STRING}"

@pytest.mark.sec_to_time
def test_1_day_1_minute_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY + SECONDES_PER_MINUTES) == f"1{DAY_STRING}1{MINUTE_STRING}"

@pytest.mark.sec_to_time
def test_1_day_1_hour_1_minute_1_sec_to_time():
    assert sec_to_time(SECONDES_PER_MINUTES * MINUTES_PER_HOURS * HOURS_PER_DAY + SECONDES_PER_MINUTES + SECONDES_PER_MINUTES * MINUTES_PER_HOURS + 1) == f"1{DAY_STRING}1{HOUR_STRING}1{MINUTE_STRING}1{SECONDE_STRING}"
