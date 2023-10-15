import pytest
from recipe import Recipe
import os

#
#   Loading
#

@pytest.mark.recipe_loading
def test_name():
    assert Recipe(os.getcwd() + "/name.recipe", "Result: This is a text").name == "name"
    assert Recipe(os.getcwd() + "/name.recipe", "Name: Here").name == "Here"

@pytest.mark.recipe_loading
def test_info():
    assert Recipe(os.getcwd() + "/name.recipe", "Result: This is a text").info == "Result: This is a text"

@pytest.mark.recipe_loading
def test_results():
    assert Recipe(os.getcwd() + "/name.recipe", "Result: copper_dust").results == {"copper_dust": 1}
    assert Recipe(os.getcwd() + "/name.recipe", "Result: copper_dustx2").results == {"copper_dust": 2}
    assert Recipe(os.getcwd() + "/name.recipe", "Result: copper_dust copper_ingot").results == {"copper_dust": 1, "copper_ingot":1}

@pytest.mark.recipe_loading
def test_crafter():
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter: fast_oven").crafter == ["fast_oven"]
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter: fast_oven\t;  slow_oven").crafter == ["fast_oven", "slow_oven"]
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter: fast_oven\t;;;  slow_oven").crafter == ["fast_oven", "slow_oven"]

@pytest.mark.recipe_loading
def test_ressource():
    assert Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust").ressources == {"copper_dust": 1}
    assert Recipe(os.getcwd() + "/name.recipe", "Ressources: 3xcopper_dust").ressources == {"copper_dust": 3}
    assert Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust copper_ingot").ressources == {"copper_dust": 1, "copper_ingot":1}

@pytest.mark.recipe_loading
def test_crafter_needed():
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter needed: True").crafter_needed == True
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter needed").crafter_needed == True
    assert Recipe(os.getcwd() + "/name.recipe", "Crafter needed: False").crafter_needed == False
    assert Recipe(os.getcwd() + "/name.recipe", "Name: Here").crafter_needed == False

@pytest.mark.recipe_loading
def test_duration():
    import const
    from stime import time_to_sec
    assert Recipe(os.getcwd() + "/name.recipe", f"Duration: 1{const.DAY_STRING}1{const.MINUTE_STRING}").duration == time_to_sec(f"1{const.DAY_STRING}1{const.MINUTE_STRING}")

@pytest.mark.recipe_loading
def test_description():
    assert Recipe(os.getcwd() + "/name.recipe", "Description: Ingot of copper").description == "Ingot of copper"
    assert Recipe(os.getcwd() + "/name.recipe", "Description: Ingot of copper\n\nAnd of copper\n").description == "Ingot of copper\n\nAnd of copper"
    from default import DEFAULT_RECIPE_DESCRIPTION
    from stime import sec_to_time
    a = Recipe(os.getcwd() + "/name.recipe", "This is a text")
    assert a.infos() == a.description == DEFAULT_RECIPE_DESCRIPTION.format(a.name, a.ressources, a.results, a.crafter, "" if a.crafter_needed else "not", sec_to_time(a.duration))

#
# Utilisation
#

@pytest.mark.recipe
def test_repr():
    repr(Recipe(os.getcwd() + "/name.crafter", f"")) == "name"

@pytest.mark.recipe
def test_uses_dict():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert a.uses() == {"copper_dust":1}
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: 3xcopper_dust  	  	\n  	  	Result:  	  3xcopper_ingot copper_dust")
    assert a.uses() == {"copper_dust":2}

@pytest.mark.recipe
def test_uses_item():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert a.uses("copper_dust")
    assert not a.uses("copper_ingot")

@pytest.mark.recipe
def test_uses_unknown():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert not a.uses("name")

@pytest.mark.recipe
def test_uses_dict():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert a.produce() == {"copper_ingot":1}
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: 3xcopper_dust copper_ingot 	  	\n  	  	Result:  	  3xcopper_ingot")
    assert a.produce() == {"copper_ingot":2}

@pytest.mark.recipe
def test_uses_item():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert a.produce("copper_ingot")
    assert not a.produce("copper_dust")

@pytest.mark.recipe
def test_uses_unknown():
    a = Recipe(os.getcwd() + "/name.recipe", "Ressources: copper_dust  	  	\n  	  	Result:  	  copper_ingot")
    assert not a.produce("name")
