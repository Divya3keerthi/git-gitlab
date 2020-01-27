import pytest


@pytest.mark.parametrize('input1, input2, output', [(1, 2, 3), (3, 4, 7)])
def test_add(input1, input2, output, setup_fixture):
    #assert input1 + input2 == output, 'test passed'
    assert input1 + input2 == setup_fixture, 'test failed'
