import pytest
from recipe import Recipe
import os

#
#   Loading
#

@pytest.mark.recipe_loading
def test_name():
    assert Recipe(os.getcwd() + "/name.recipe", "This is a text").name == "name"

@pytest.mark.recipe_loading
def test_info():
    assert Recipe(os.getcwd() + "/name.recipe", "This is a text").info == "This is a text"

@pytest.mark.recipe_loading
def test_description():
    from default import DEFAULT_RECIPE_DESCRIPTION
    from stime import sec_to_time
    a = Recipe(os.getcwd() + "/name.recipe", "This is a text")
    assert a.infos() == a.description == DEFAULT_RECIPE_DESCRIPTION.format(a.name, a.ressources, a.results, a.crafter, "" if a.crafter_needed else "not", sec_to_time(a.duration))
