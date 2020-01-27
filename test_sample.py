import pytest


# @pytest.fixture()
# def setup_fixture():
#    c = 8
#    return c

@pytest.mark.set1
def test_file1_method1():
    x = 5
    y = 6
    assert x + 2 == y, "test failed"
    assert x == y, "test failed"


@pytest.mark.set2
def test_file1_method2():
    x = 5
    y = 6
    assert x + 2 == y, "test failed"


@pytest.mark.set1
def test_file1_method3(setup_fixture):
    x = 5
    y = 6
    assert x + y == setup_fixture, "test failed"
