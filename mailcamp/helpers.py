"""
In this file various helper functions can be found and utilized throughout
the package.
"""


def dicttoxml(dictionary):
    """
    This function gets a dictionary as an input and creates an xml string from
    it
    :param dictionary:
    :return:
    """
    xml_string = ''
    for k, v in dictionary.items():
        if v is None:
            xml_string += '<{0}> </{0}>'.format(k)
            continue
        if isinstance(v, dict):
            secondary_dict = dicttoxml(v)
            xml_string += '<{0}>{1}</{0}>'.format(k, secondary_dict)
            continue
        xml_string += '<{0}>{1}</{0}>'.format(k, v)
    return xml_string
