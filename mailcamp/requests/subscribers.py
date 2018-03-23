"""
Subscribers related actions

"""
from mailcamp.BaseApi import BaseApi


class Subscribers(BaseApi):
    request_type = 'subscribers'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(
            self,
            newsletter_id,
            email=None,
            confirmed=None,
            format=None,
            after=None,
            before=None,
            exact=None,
            not_registered=None,
            newsletters=None,
            sort_by='subscribedate',
            direction='Down',
            fields=None):
        """

        :param ownerid:
        :param newsletter_id:
        :param start:
        :param per_page:
        :param fields:
        :return:
        """
        request_method = 'GetSubscribers'

        details = {
            'searchinfo': {
                'List': {'array': newsletter_id}
            }
        }
        request = self._get_xml_request(
            requesttype=self.request_type, requestmethod=request_method,
            details=details)
        data = self._mailcamp_client._post(request)
        return data
