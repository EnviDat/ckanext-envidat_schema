import json

import logging


logger = logging.getLogger(__name__)

def envidat_schema_get_citation(package_data_dict):
    '''
    Combines multiple datacite metadata into a
    citation string. Pattern:
    creators (publication_year): title; subtitle. publisher; doi:identifier.
    '''
    citation = u''

    # creators
    creators = _get_from_json_dict_list(package_data_dict.get('author', ""), 'name')
    if creators:
        citation += creators

    # publication_year
    publication_year = _get_from_json_dict(package_data_dict.get('publication', ""), 'publication_year')
    if (publication_year):
        citation += ' ('+ publication_year + ')'

    # separator
    if citation:
        citation +=': '

    # title
    title = package_data_dict.get('title', "")
    if title:
        citation += title.strip() + '; '

    # publisher
    publisher = _get_from_json_dict(package_data_dict.get('publication', ""), 'publisher')
    if (publisher):
        citation += publisher + '; '

    # doi:identifier.
    doi = package_data_dict.get('doi', "")
    if doi:
        citation += 'doi:' + doi.strip() + '.'

    return citation


def _get_from_json_dict (text, field):
    try:
        json_dict = json.loads(text)
        value = json_dict.get(field, "")
    except:
        return ""
    return _safe_str(value).strip()

def _get_from_json_dict_list (text, field, sep='; '):
    try:
        json_list = json.loads(text)
        if type(json_list) is not list:
            json_list = [ json_list ]
        value_list = []
        for item in json_list:
            value = _safe_str(item.get(field, "")).strip()
            if value:
                value_list += [ value ]
    except:
        return ""
    return (sep.join(value_list))


def _safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj)
