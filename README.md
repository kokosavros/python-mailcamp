# python-mailcamp
A python client for the [mailcamp](https://www.mailcamp.nl/) xml api.

## API Documentation
API documentation can be found in the following pages:
[Dutch version](https://www.mailcamp.nl/api/nl/)
[English version](https://www.mailcamp.nl/api/en/)

## Initialization
In order to connect and you need the username, your xml token and the url
of the mailcamp server.

```
from mailcamp import MailCamp

client = MailCamp('username', 'xml_token','url')
```

## Examples
```
# Returns if a token is valid
client.token_check.is_valid()
```