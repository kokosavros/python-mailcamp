import unittest
from mailcamp.helpers import dicttoxml, xmltodict


class TestHelpers(unittest.TestCase):
    def setUp(self):
        pass

    def test_dicttoxml(self):
        # Test with empty dictionary
        result = dicttoxml({})
        self.assertEqual(
            result, '', 'Empty dictionary does not return empty string')

    def test_xmltodict(self):
        xml = """<xmlrequest>
                <status>success</status>
                <message>You did it</message>
                </xmlrequest>"""
        result = xmltodict(xml)
        expected = {'message': 'You did it', 'status': 'success'}
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a simple request is not correct')

        xml = """<xmlrequest>
                <status>success</status>
                <message>You did it</message>
                <details>
                <name>name</name>
                <lastname>lastname</lastname>
                </details>
                </xmlrequest>"""
        result = xmltodict(xml)
        expected = {
            'message': 'You did it',
            'details': {'name': 'name', 'lastname': 'lastname'},
            'status': 'success'
        }
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a request with simple nested field is '
            'not correct')

        xml = """<ids><id>1</id><id>2</id><id>3</id></ids>"""
        result = xmltodict(xml)
        expected = {
            'id': ['1', '2', '3']
        }
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a request with array field is '
            'not correct')

        xml = """<xmlrequest>
                <status>success</status>
                <message>You did it</message>
                <details>
                <item>
                <name>name1</name>
                <lastname>lastname1</lastname>
                </item>
                <item>
                <name>name2</name>
                <lastname>lastname2</lastname>
                </item>
                </details>
                </xmlrequest>"""

        result = xmltodict(xml)
        expected = {
            'message': 'You did it',
            'status': 'success',
            'details': {
                'item': [
                    {'name': 'name1', 'lastname': 'lastname1'},
                    {'name': 'name2', 'lastname': 'lastname2'}
                ]
            }
        }
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a request with array of nested fields is '
            'not correct')

        xml = """<xmlrequest>
                <status>success</status>
                <message>You did it</message>
                <details>
                <item>
                <name>name1</name>
                <lastname>lastname1</lastname>
                </item>
                <item>
                <name>name2</name>
                <lastname>lastname2</lastname>
                </item>
                <ids><id>1</id><id>2</id><id>3</id></ids>
                </details>
                </xmlrequest>"""
        result = xmltodict(xml)
        expected = {
            'message': 'You did it',
            'status': 'success',
            'details': {
                'item': [
                    {'name': 'name1', 'lastname': 'lastname1'},
                    {'name': 'name2', 'lastname': 'lastname2'}
                ],
                'ids': {'id': ['1', '2', '3']}
            }
        }
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a request with array of nested fields '
            ' and simple array is not correct')

        xml = """<xmlrequest>
                <status>success</status>
                <message>You did it</message>
                <details>
                <item>
                <name>name1</name>
                <lastname>lastname1</lastname>
                </item>
                <item>
                <name>name2</name>
                <lastname>lastname2</lastname>
                </item>
                <ids><id>1</id><id>
                <active>True</active>
                <number>2</number>
                </id><id>3</id></ids>
                </details>
                </xmlrequest>"""
        result = xmltodict(xml)
        expected = {
            'message': 'You did it',
            'status': 'success',
            'details': {
                'item': [
                    {'name': 'name1', 'lastname': 'lastname1'},
                    {'name': 'name2', 'lastname': 'lastname2'}
                ],
                'ids': {'id': ['1', {'active': 'True', 'number': '2'}, '3']}
            }
        }
        self.assertDictEqual(
            expected,
            result,
            'The dictionary of a request with complex structure is not '
            'correct')

if __name__ == '__main__':
    unittest.main()
