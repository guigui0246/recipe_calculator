import pytest
import loader
import os
from inventory import Item
from crafter import Crafter

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.mark.loading
def test_inv_load(tmpdir, monkeypatch):
    monkeypatch.chdir(tmpdir)
    with open(os.path.join(".", "inventory.item"), "w") as f:
        f.write("name\n2xname2x3\n2xname2\n\n\nname3x1x1\n\n")
    assert str(loader.get_inv().content) == str([Item("name", 1), Item("name2", 8), Item("name3x1", 1)])

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.mark.loading
def test_crafter_load(tmpdir, monkeypatch):
    monkeypatch.chdir(tmpdir)
    tmpdir.mkdir("crafter")
    with open(os.path.join(".", "crafter", "name.crafter"), "w") as f:
        f.write("")
    assert str(loader.get_crafter()) == str([Crafter(os.path.join(os.getcwd(), "crafter", "name.crafter"), "")])

@pytest.mark.usefixtures("tmpdir", "monkeypatch", "capfd")
@pytest.mark.loading
def test_crafter_load_nothing(tmpdir, monkeypatch, capfd):
    monkeypatch.chdir(tmpdir)
    loader.get_crafter()
    assert capfd.readouterr()[1] == "Aucune machine trouvée\n"

@pytest.mark.usefixtures("capfd")
@pytest.mark.loading
def test_loading(capfd):
    import loading
    loads = loading.Loading()
    loads.valeur
    del loads
    assert True
