"""
Get data for the user
"""
from mailcamp.BaseApi import BaseApi
from mailcamp.helpers import xmltodict

class User(BaseApi):
    """
    Get user info
    """
    request_type = 'authentication'
    request_method = 'xmlapitest'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def id(self):
        """
        Get the id of a user
        :return: THe id of a user
        """
        request = self._get_xml_request(
            requesttype=self.request_type, requestmethod=self.request_method,
            details=None)
        response = self._mailcamp_client._post(request)
        response_dict = xmltodict(response)
        return response_dict.get('data', dict()).get('userid')
