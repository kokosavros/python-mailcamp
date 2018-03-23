from mailcamp.mailcampclient import MailCampClient
from mailcamp.requests.tokencheck import TokenCheck
from mailcamp.requests.user import User
from mailcamp.requests.newsletters import Newsletters
from mailcamp.requests.subscribers import Subscribers


class MailCamp(MailCampClient):
    """
    MailCamp class to communicate with the API
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the mailcamp class and client
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.token_check = TokenCheck(self)
        self.user = User(self)
        self.newsletters = Newsletters(self)
        self.subscribers = Subscribers(self)
