
import pytest

@pytest.mark.usefixtures("setup")

class TestExample:

    def test_fixtureDemo(self):
        print("I will execute the steps in fixureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute the steps in fixureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute the steps in fixureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute the steps in fixureDemo3 method")