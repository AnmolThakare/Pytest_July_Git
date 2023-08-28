## Date: 28/07/23
import pytest
from selenium import webdriver


# Config Interpreter
# pip install selenium
# pip install pytest --> for test run
# pip install pytest-html --> to generate report
# pip install pytest-xdist --> to run parallel
# pip install allure-pytest --> to generate allure report
# Select pytest as default runner in python (Go to setting --> Tools --> python integrated tools)
# Go to setting --> Tools --> Terminal --> Enter in shell path --> C:\Windows\system32\cmd.exe
# To run specific file with abs path --> pytest -v -n=4 --html=Report/report.html "G:\pythonProject
# \Pytest_July\test_file_002.py"

## Rules of Pytest Framework

# File name should start with test_
# class name should start with Test_
# testcases should start with test_
# to run the test files from terminal --> pytest
# for more details on lib/plugins --> pytest -v
# for printing the output on console --> pytest -s
# to run specific file in the project dir --> pytest filename.py (eg. pytest test_file_001.py)
# To run testcases parallel --> pytest -n=number (eg. pytest -n=2) number --> worker processor
# To generate pytest html report --> (pytest --html=Reports/report.html)
# -s use krne ke bad report me log generate nahi hoga
# Assertion is used for the testcase is intentionally failed or passed
# To set marker for testcases use @pytest.mark.marker_name before testcase
# To run testcases with user define marker --> pytest -m credence


class Test_Credence:

    #@pytest.mark.skip
    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print("sum of a & b is:" +str(sum))
        if sum == 10:
            assert True
        else:
            assert False


    def test_CredenceUrl_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("You are at credence.in")
            assert True
        else:
            print("You are at wrong url")
            assert False

    #@pytest.mark.xfail
    def test_sub_003(self):
        a = 3
        b = 7
        sub = a - b
        print("Subtraction of a from b is:" +str(sub))
        if sub == -4:
            assert True
        else:
            assert False

