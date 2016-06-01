import json

from ckanext.scheming.validation import scheming_validator
from ckantoolkit import _

@scheming_validator
def envidat_schema_spatial(field, schema):

    def validator(key, data, errors, context):

        # if there was an error before calling our validator
        # don't bother with our validation
        if errors[key]:
            return

        value = data[key]
        print "Value is " + str(type(value))

	if not value:
            return

	try:
            if not isinstance(value, dict):
                value =  json.loads(value)
            print value["type"]
            sp_type = value["type"]
            print value["coordinates"]
            coordinates = value["coordinates"]
        except:
            print "ERROR validating spatial field, value = " + str(value)
            errors[key].append(_('expecting spatial dictionary with keys type and coordinates'))
            return

        if not errors[key]:
            data[key] = json.dumps(value, ensure_ascii=False)
        return

    return validator

def envidat_schema_spatial_output(value):
    """
    return dictionary or none
    """
    if isinstance(value, dict):
        return value
    try:
       spatial_dict = json.loads(value)
       type = spatial_dict["type"]
       coordinates = spatial_dict["coordinates"]
       return spatial_dict
    except (ValueError, KeyError, TypeError):
       print "ERROR in Spatial field, value = " + str(value)
       return ({'type':'', 'coordinates':[]})

