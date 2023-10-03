import pytest
from crafter import Crafter
import os

#
#   Loading
#

@pytest.mark.crafter_loading
def test_name():
    assert Crafter(os.getcwd() + "/name.crafter", "Result: This is a text").name == "name"
    assert Crafter(os.getcwd() + "/name.crafter", "Name: Here").name == "Here"

@pytest.mark.crafter_loading
def test_info():
    assert Crafter(os.getcwd() + "/name.crafter", "Result: This is a text").info == "Result: This is a text"

@pytest.mark.crafter_loading
def test_results():
    assert Crafter(os.getcwd() + "/name.crafter", "Result: copper_dust").results == {"copper_dust": 1}

@pytest.mark.crafter_loading
def test_crafter():
    assert Crafter(os.getcwd() + "/name.crafter", "Crafter: fast_oven").crafter == "fast_oven"

@pytest.mark.crafter_loading
def test_ressource():
    assert Crafter(os.getcwd() + "/name.crafter", "Ressources: copper_dust").ressources == {"copper_dust": 1}

@pytest.mark.crafter_loading
def test_speed():
    assert Crafter(os.getcwd() + "/name.crafter", "Speed: x3").speed == 3
    assert Crafter(os.getcwd() + "/name.crafter", "Speed: 0.3x").speed == 0.3
    assert Crafter(os.getcwd() + "/name.crafter", "Speed: 0.3x10").speed == 3
    assert Crafter(os.getcwd() + "/name.crafter", "").speed == 1

@pytest.mark.crafter_loading
def test_duration():
    import const
    from stime import time_to_sec
    assert Crafter(os.getcwd() + "/name.crafter", f"Duration: +1{const.DAY_STRING}1{const.MINUTE_STRING}").duration == time_to_sec(f"1{const.DAY_STRING}1{const.MINUTE_STRING}")
    assert Crafter(os.getcwd() + "/name.crafter", f"Duration: -1{const.DAY_STRING}4{const.MINUTE_STRING}").duration == -time_to_sec(f"1{const.DAY_STRING}4{const.MINUTE_STRING}")

@pytest.mark.crafter_loading
def test_description():
    assert Crafter(os.getcwd() + "/name.crafter", "Description: Ingot of copper").description == "Ingot of copper"
    assert Crafter(os.getcwd() + "/name.crafter", "Description: Ingot of copper\n\nAnd of copper\n").description == "Ingot of copper\n\nAnd of copper"
    from default import DEFAULT_CRAFTER_DESCRIPTION
    from stime import sec_to_time
    a = Crafter(os.getcwd() + "/name.crafter", "This is a text")
    assert a.infos() == a.description == DEFAULT_CRAFTER_DESCRIPTION.format(a.name, a.ressources, a.results, a.crafter, "" if a.crafter_needed else "not", sec_to_time(a.duration))
