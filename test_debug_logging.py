import pytest
import debug
import os

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.hookimpl(tryfirst=True)
@pytest.mark.debug
def test_log(tmpdir, monkeypatch):
    monkeypatch.chdir(tmpdir)
    debug.debug("This is a test log")
    with open(os.path.join(".", "debug.log")) as f:
        txt = f.read()
    assert txt=="\"\"\" This is a test log \"\"\"\n"
