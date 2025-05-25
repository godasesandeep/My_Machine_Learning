#fixtures are used as setup & tear down methods for test cases
#Conftest file to generalize fixyure & make it available to all test cases.


import pytest

@pytest.fixture()

def setup():
    print("I will executing first")
    yield
    print("I wii execute last")


def test_fixtureDemo(setup):
    print("I wii execute steps in fixtureDemo method")


# yield keyword it automatically treats that whatever you write after that yield step wii be 
#executed after your test execution is completed,SO that means post test execution teardown method run after yield 
#and prerequest setup method run before yield 
#print("I wii execute last") you will use this to close the browser and to delete the cookies at the end after your execution is done

