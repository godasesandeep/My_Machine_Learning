
# Any pytest file should starts with test_ or ends with _test keyword
# pytest method names should starts with test
# Any code should be wrapped in method only
# method name should have sence
# Give meaningful names to test files and methods.
# In pytest you can not have multiple test methods name with the same name, if you have that it oveerrides the previous result
# -k stands for method name execution,-s logs in output ,-v stands for more info metadata (verbosity)
# you can run specific file with py.test<filename>
# If you don't give the file name then it will run all the file present in the package
# & if you give the file name then it will run only that specific file
# change directory --> cd pytestDemo
# Run Script --> python -m pytest test_demo1.py -v -s
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip test with @pytest.mark.skip
# when you give this @pytest.mark.xfail the particular test will run but in output won't see pass or fail. 



import pytest
def test_firstprogram():
    print("Hello..!!")
    msg = "Hii"
    assert msg =="Hii"
    

 #Asseration error
@pytest.mark.skip
def test_secondprogram():
   print("Hello..!!")
   msg="Hii"
   assert msg =="Hello","Test failed because string do not match"

def test_thirdprogram():
    a = 4
    b = 6
    assert a+2 == 6 , "Addition do not match"

@pytest.mark.xfail
def test_greet():
   print("Good morning...!")

# when you give this @pytest.mark.xfail the particular test will run but in output 
#you won't see about pass or fail so this is like a just running but not reporting so you want to use this
#in cases where you think this is required for further testcases to run but should not come in reporting