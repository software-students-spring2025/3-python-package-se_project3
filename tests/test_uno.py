import pytest
from terminalUno import uno

class TestUno:

    def test_sanity(self):
        excepted = True
        actual = True
        assert excepted == actual, "Test failed"
        print("Pytest is running as expected")
    

