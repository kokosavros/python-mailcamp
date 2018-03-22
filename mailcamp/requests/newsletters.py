"""
Newsletter related actions

Documentation: https://www.mailcamp.nl/api/en/#api-Newsletter
"""
from mailcamp.BaseApi import BaseApi
import xml.etree.ElementTree as et


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
        newsletters = list()
        for child in et.fromstring(response):
            if child.tag == 'status' and child.text == 'FAILED':
                raise ConnectionError('Could not retrieve data')
            if child.tag == 'data':
                for d in child:
                    if d.tag == 'item':
                        if fields:
                            newsletter = {
                                i.tag: i.text for i in d if i.tag in fields}
                        else:
                            newsletter = {i.tag: i.text for i in d}
                        newsletters.append(newsletter)
        return newsletters
