import pytest

#
# exemple
#

@pytest.mark.usefixtures("capfd")
@pytest.mark.loading
def test_load_exemple(capfd):
    with pytest.raises(KeyboardInterrupt):
        import load_exemple
        raise KeyboardInterrupt()
