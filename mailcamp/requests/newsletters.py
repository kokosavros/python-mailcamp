"""
Newsletter related actions

Documentation: https://www.mailcamp.nl/api/en/#api-Newsletter
"""
from mailcamp.BaseApi import BaseApi
from mailcamp.helpers import xmltodict


class Newsletters(BaseApi):
    request_type = 'newsletters'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def get_all(
            self, owner=None, sort_by='Date', direction='Down', fields=None):
        """
        Get all the newsletters, filter on the fields to return
        :return:
        """
        request_method = 'GetNewsletters'
        details = {
            'owner': owner,
            'sortinfo': {
                'SortBy': sort_by,
                'direction': direction
            }
        }
        request = self._get_xml_request(
            requesttype=self.request_type, requestmethod=request_method,
            details=details)
        response = self._mailcamp_client._post(request)
        response_dict = xmltodict(response)
        # Check if response status is ok
        if response_dict.get('status', 'FAILED') == 'FAILED':
            raise ConnectionError('Could not retrieve data')
        data = response_dict.get('data', dict())
        newsletters = data.get('item', list())
        # Filter the newsletters
        return [
            {k: v for k, v in newsletter.items() if k in fields}
            for newsletter in newsletters]
