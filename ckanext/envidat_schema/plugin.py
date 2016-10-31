import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.envidat_schema import helpers

class Envidat_SchemaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'envidat_schema')

    # ITemplateHelpers
    def get_helpers(self):
	return { 'envidat_schema_get_citation': helpers.envidat_schema_get_citation }
