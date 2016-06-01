import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.envidat_schema.helpers import envidat_schema_spatial_value 

from ckanext.envidat_schema.validators import (
     envidat_schema_spatial,
     envidat_schema_spatial_output)


class Envidat_SchemaPlugin(plugins.SingletonPlugin):
     plugins.implements(plugins.IConfigurer)
     plugins.implements(plugins.ITemplateHelpers)
     plugins.implements(plugins.IValidators)

     # IConfigurer

     def update_config(self, config_):
         toolkit.add_template_directory(config_, 'templates')
         toolkit.add_public_directory(config_, 'public')
         toolkit.add_resource('fanstatic', 'envidat_schema')

     # ITemplateHelpers
     def get_helpers(self):
         return {
            'envidat_schema_spatial_value': envidat_schema_spatial_value
         }

     # IValidators
     def get_validators(self):
         return {"envidat_schema_spatial": envidat_schema_spatial,
                 "envidat_schema_spatial_output": envidat_schema_spatial_output}

