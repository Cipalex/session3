# test file
import pytest


@pytest.mark.sanity
def test_always_passes():
    assert True

@pytest.mark.regression
def test_always_fails():
    assert False


