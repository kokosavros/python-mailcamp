"""
The base API to construct various xml requests strings
"""
from mailcamp.helpers import dicttoxml


class BaseApi:
    def __init__(self, mailcamp_client):
        """
        A base API class to contruct the various xml strings to be requested
        :param mailcamp_client:
        """
        self._mailcamp_client = mailcamp_client

    def _get_xml_request(self, requesttype, requestmethod, details):
        """
        
        :param requesttype:
        :param requestmethod:
        :param details:
        :return:
        """
        return '<xmlrequest>{0}{1}{2}</xmlrequest>'.format(
            self._get_xml_request_auth_part(),
            self._get_xml_request_attr_part(requesttype, requestmethod),
            self._get_xml_request_details_part(details))

    def _get_xml_request_auth_part(self):
        return '<username>{0}</username><usertoken>{1}</usertoken>'.format(
            self._mailcamp_client.username, self._mailcamp_client.xml_token)

    @staticmethod
    def _get_xml_request_details_part(details):
        """
        Returns the details part of the xml request
        :param details: A dict with the various details of the request
        :return:
        """
        xml_string = '<details>{}</details>'
        if details is None:
            return xml_string.format(' ')
        return xml_string.format(dicttoxml(details))

    @staticmethod
    def _get_xml_request_attr_part(requesttype, requestmethod):
        """
        Returns the xml string part of the request attributes, namely request
        type and request method
        :param requesttype:
        :param requestmethod:
        :return:
        """
        return """
        <requesttype>{0}</requesttype>
        <requestmethod>{1}</requestmethod>
        """.format(requesttype, requestmethod)
