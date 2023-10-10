import pytest
import debug
import os

#
# Debug
#

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.hookimpl(tryfirst=True)
@pytest.mark.debug
def test_log(tmpdir, monkeypatch):
    monkeypatch.chdir(tmpdir)
    debug.debug("This is a test log")
    with open(os.path.join(".", "debug.log")) as f:
        txt = f.read()
    assert txt=="\"\"\" This is a test log \"\"\"\n"

#
# conftest.py
#
class It():
    def __init__(self) -> None:
        self.data = "Data"
    def clear(self) -> None:
        del self.data

@pytest.hookimpl(tryfirst=True)
@pytest.mark.debug
def test_conftest_success():
    import conftest
    conftest.Fail = False
    item = It()
    conftest.pytest_collection_modifyitems(None, item)
    assert hasattr(item, "data")

@pytest.hookimpl(tryfirst=True)
@pytest.mark.debug
def test_conftest_fail():
    import conftest
    conftest.Fail = True
    item = It()
    conftest.pytest_collection_modifyitems(None, item)
    assert not hasattr(item, "data")
