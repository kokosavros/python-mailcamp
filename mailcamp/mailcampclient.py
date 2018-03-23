import requests as re
from mailcamp.helpers import xmltodict


class MailCampError(Exception):
    pass


class MailCampClient:
    """
    MailCamp class to communicate with mailcamps XML API
    """
    def __init__(self, username, xml_token, url):
        """
        Initialize the class with username, xml_token and url
        :param username: The username of a user in mailcamp
        :param xml_token: The xml_token provided by mailcamp
        :param url: The url where the requests are sent to.
        """
        self.username = username
        self.xml_token = xml_token
        self.url = url

    def _post(self, xml_request):
        """
        The post method to the MailCamp api
        :param xml_request:
        :return:
        """
        response = re.post(self.url, data=xml_request).content.decode('utf-8')
        # Transform response into dict
        response_dict = xmltodict(response)
        self._check_response_status(response_dict)
        return response_dict['data']

    @staticmethod
    def _check_response_status(response):
        """
        This function checks the status of the response and raises an error
        if the response was not successful
        :param response: The dictionary of the response
        :return:
        """
        if response.get('status', 'FAILED') == 'FAILED':
            raise MailCampError(
                response.get(
                    'errormessage', 'Mailcamp returned an error'))
