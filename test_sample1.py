import pytest

@pytest.fixture
def data():
	z=8
	return z

#using fixture: since data returns z we can directly use data in below methods, if data returns list then data[0] i.e we can use indexing
def test_file1_method1(data,test_fix):
	x=5
	y=6
	assert x+1 == y,"test failed because x=" +str(x)+"and y="+str(y)
	assert x == y,"test failed"
	assert data == x+y, "test failed"
	assert test_fix[1]==x, "test passed"
def test_file1_method2(data):
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert data == x + y, "test failed"
def file1_method2(): #invalid naming convention without test
	x=5
	y=6
	assert x+1 == y,"test failed"