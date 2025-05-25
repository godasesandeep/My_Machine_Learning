
import pytest

@pytest.fixture(scope="class")

def setup():
    print("I will executing first")
    yield
    print("I will executing last")


import pytest

@pytest.fixture()

def dataLoad():
    print ("User profile data is being created")
    return ["Ashwini","Sandeep","AshSandyacademy.com"]

import pytest

@pytest.fixture(params=[("chrome","Ashwini","Godase"),("firefox","Sandeep"),("IE","AS")])

def crossBrowser(request):
    return request.param