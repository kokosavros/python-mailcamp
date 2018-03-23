import unittest
from mailcamp.helpers import dicttoxml


class TestHelpers(unittest.TestCase):
    def setUp(self):
        pass

    def test_dicttoxml(self):
        # Test with empty dictionary
        result = dicttoxml({})
        self.assertEquals(result, '', 'Empty dictionary does not return empty string')

if __name__ == '__main__':
    unittest.main()