"""
Newsletter related actions

Documentation: https://www.mailcamp.nl/api/en/#api-Newsletter
"""
from mailcamp.BaseApi import BaseApi
from mailcamp.helpers import xmltodict
from datetime import datetime


class Newsletters(BaseApi):
    request_type = 'newsletters'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def get_all(
            self,
            ownerid=None,
            sort_by='Date',
            direction='Down',
            fields=None):
        """
        Get all the newsletters, filter on the fields to return
        :return:
        """
        request_method = 'GetNewsletters'
        details = {
            'owner': ownerid,
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

    def create(
            self,
            name,
            ownerid,
            format='b',
            subject=None,
            textbody=None,
            htmlbody=None,
            createdate=None,
            active=1,
            archive=0
    ):
        """
        Create a newsletter and get back its id
        :param name: The name of the newsletter.
        :param ownerid: The owner id
        :param format: The format. This can be, H (HTML), t (text/plain text)
        or b (both). The best is b, but then you need both a text and HTML
        version ready to upload.
        :param subject: The subject of the newsletter. Not more than 50
        characters.
        :param textbody: The content of the newsletter in plain text format.
        :param htmlbody: The content of the newsletter in HTML format. Do not
        forget to add the CDATA-tag
        <![CDATA[<html><head></head><body>Dit is de html body</body>]]>
        :param createdate: The date in unix time stamp.
        :param active: Uses the value 1 for the Newsletter as active.
        0 is for inactive.
        :param archive: Use value '1' to add the newsletter to the archive.
        :return: The id of the newly created newsletter
        """
        request_method = 'Create'
        details = {
            'ownerid': ownerid,
            'name': name,
            'subject': subject,
            'format': format,
            'textbody': textbody,
            'htmlbody': htmlbody,
            'createdate': createdate or datetime.utcnow().timestamp(),
            'active': active,
            'archive': archive
        }

        request = self._get_xml_request(
            requesttype=self.request_type, requestmethod=request_method,
            details=details)
        response = self._mailcamp_client._post(request)
        response_dict = xmltodict(response)
        # Check if response status is ok
        if response_dict.get('status', 'FAILED') == 'FAILED':
            raise ConnectionError('Could not retrieve data')
        return response_dict['data']
