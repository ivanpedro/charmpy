
import unittest

from hello_someone import hello_someone, name

#this test runs in charmpy but you can not test it in visual studio
class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        """"test that the function returns "Hello, World!"
        "when called with the appropriate input argument"""

        self.assertEquals(hello_someone(name),"Hello, World!" )



