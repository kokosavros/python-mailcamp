"""
In this file various helper functions can be found and utilized throughout
the package.
"""
import xml.etree.ElementTree as et


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


def xmltodict(xml_string):
    """
    This function returns a dictionary from a xml_string
    :param xml_string:
    :return:
    """
    result = dict()
    for child in et.fromstring(xml_string):
        # If field has multiple children create list of their values
        if list(child):
            obj = result.get(child.tag)
            new = xmltodict(et.tostring(child).decode())
            if obj and isinstance(obj, list):
                obj.append(new)
                result[child.tag] = obj
                continue
            if obj:
                a = list([obj])
                a.append(new)
                result[child.tag] = a
                continue
            result[child.tag] = new
            continue
        # If value not empty create a list
        if result.get(child.tag):
            a = list(result.get(child.tag))
            a.append(child.text)
            result[child.tag] = a
            continue
        # If value is empty give the text to the value.
        result[child.tag] = child.text
    return result
