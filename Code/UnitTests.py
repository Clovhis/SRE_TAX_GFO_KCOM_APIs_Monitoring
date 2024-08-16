from unittest import TestCase
from ErrorHandler import HttpException

def isPepe():
    return True

class SimplisticTest(TestCase):
    def test(self):
        a = True
        assert isPepe()

class TestException(TestCase):
    def test(self):
        raise HttpException('http://google.com')
        
try:
    TestException().test()
except Exception:
    print("Continued after error is raised")