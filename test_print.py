import pytest
from print_clearable import *

test_work = set()

#
# test clear_cache
#

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.mark.print
def test_print_to_file(tmpdir, monkeypatch):
    global PRINT_BUFFER
    PRINT_BUFFER["./somefile"] = "Text"
    clear_cache("./somefile")
    assert PRINT_BUFFER == {}
    PRINT_BUFFER["./somefile"] = "Text"
    PRINT_BUFFER["./someotherfile"] = "Tet"
    clear_cache(all=True)
    assert PRINT_BUFFER == {}
    PRINT_BUFFER["./somefile"] = "Text\nn\n\n\nte\n"
    clear_cache("./somefile")
    assert PRINT_BUFFER == {}
    import sys
    PRINT_BUFFER[sys.stdout] = "Text"
    clear_cache()
    assert PRINT_BUFFER == {}
    import io
    f = io.StringIO()
    PRINT_BUFFER[f] = "Text"
    clear_cache(f)
    assert PRINT_BUFFER == {}
    test_work.add("clear_cache")

#
# test print
#

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.mark.print
def test_print_to_file(tmpdir, monkeypatch):
    pytest.mark.skipif("clear_cache" not in test_work, reason="Cannot write to file to clear after")
    monkeypatch.chdir(tmpdir)
    with open("./somefile", "w") as f:
        print("This is a test", file=f)
    with open("./somefile2", "w") as f:
        original_print("This is a test", file=f)
    with open("./somefile") as f:
        txt = f.read()
    with open("./somefile2") as f:
        txt2 = f.read()
    assert txt == txt2
    clear_cache()
    test_work.add("print_write_to_file")

@pytest.mark.usefixtures("capfd")
@pytest.mark.print
def test_print_to_stdout(capfd):
    pytest.mark.skipif("clear_cache" not in test_work, reason="Cannot write to file to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test")
    txt = capfd.readouterr()[0]
    original_print("This is a test")
    txt2 = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == txt2
    clear_cache()
    test_work.add("print_write_to_stdout")

@pytest.mark.usefixtures("capfd")
@pytest.mark.print
def test_print_to_stderr(capfd):
    pytest.mark.skipif("clear_cache" not in test_work, reason="Cannot write to file to clear after")
    import sys
    print("This is a test", file=sys.stderr)
    txt = capfd.readouterr()[1]
    original_print("This is a test", file=sys.stderr)
    txt2 = capfd.readouterr()[1]
    assert txt == txt2
    clear_cache()
    test_work.add("print_write_to_stderr")

@pytest.mark.usefixtures("capfd")
@pytest.mark.print
def test_multiple_print_to_stdout(capfd):
    pytest.mark.skipif("clear_cache" not in test_work, reason="Cannot write to file to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test")
    print("This is a test")
    txt = capfd.readouterr()[0]
    original_print("This is a test")
    original_print("This is a test")
    txt2 = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == txt2
    clear_cache()
    test_work.add("multi_print_write_to_stdout")

@pytest.mark.usefixtures("capfd")
@pytest.mark.print
def test_multiple_element_print_to_stdout(capfd):
    pytest.mark.skipif("clear_cache" not in test_work, reason="Cannot write to file to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test", "This is a test")
    txt = capfd.readouterr()[0]
    original_print("This is a test", "This is a test")
    txt2 = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == txt2
    clear_cache()
    test_work.add("multi_elem_print_write_to_stdout")

#
# test clear
#

@pytest.mark.usefixtures("tmpdir", "monkeypatch")
@pytest.mark.clear
@pytest.mark.skip("File clear not setup")
def test_clear_to_file(tmpdir, monkeypatch):
    pytest.mark.skipif("print_write_to_file" not in test_work, reason="Cannot write to file to clear after")
    monkeypatch.chdir(tmpdir)
    with open("./somefile", "w") as f:
        print("This is a test", file=f)
        clear(f)
    with open("./somefile") as f:
        txt = f.read()
    assert txt == ""
    clear_cache()

@pytest.mark.usefixtures("capfd")
@pytest.mark.clear
def test_clear_to_stdout(capfd):
    pytest.mark.skipif("print_write_to_stdout" not in test_work, reason="Cannot write to stdout to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test")
    clear()
    txt = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == ""
    clear_cache()

@pytest.mark.usefixtures("capfd")
@pytest.mark.clear
@pytest.mark.skip("Made using stdout (to fix)")
def test_clear_to_stderr(capfd):
    pytest.mark.skipif("print_write_to_stderr" not in test_work, reason="Cannot write to stderr to clear after")
    import sys
    print("This is a test", file=sys.stderr)
    txt = capfd.readouterr()[1]
    assert txt == ""
    clear_cache()

@pytest.mark.usefixtures("capfd")
@pytest.mark.clear
def test_multiple_clear_to_stdout(capfd):
    pytest.mark.skipif("multi_print_write_to_stdout" not in test_work, reason="Cannot write to stdout to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test")
    print("This is a test")
    txt = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == ""
    clear_cache()

@pytest.mark.usefixtures("capfd")
@pytest.mark.clear
def test_multiple_element_clear_to_stdout(capfd):
    pytest.mark.skipif("multi_elem_print_write_to_stdout" not in test_work, reason="Cannot write to stdout to clear after")
    from io import StringIO
    import sys
    out = StringIO()
    sys.stdout = out
    print("This is a test", "This is a test")
    txt = capfd.readouterr()[0]
    sys.stdout = sys.__stdout__
    assert txt == ""
    clear_cache()
