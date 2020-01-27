import pytest


@pytest.mark.set1
#@pytest.mark.xfail
def test_file2_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.skip
#@pytest.mark.set2
def test_file2_method2(setup_fixture):
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x - 1 == setup_fixture, 'test passed'
