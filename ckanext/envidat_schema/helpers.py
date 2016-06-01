import json

def envidat_schema_spatial_value(value):
    """
    :param value: spatial dictionary value
    Return the dictionary as a json dump
    """
    if not value:
        return ""

    json_value = ""

    try:
       json_value = json.dumps(value, ensure_ascii=False)
    except:
       json_value = value

    return (json_value)
