import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.envidat_schema import helpers, validation

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
	return { 'envidat_schema_get_citation': helpers.envidat_schema_get_citation,
                 'envidat_schema_get_datamanager_choices': helpers.envidat_schema_get_datamanager_choices,
                 'envidat_schema_get_datamanager_user': helpers.envidat_schema_get_datamanager_user,
                 'envidat_schema_set_default': helpers.envidat_schema_set_default }

    # IValidators
    def get_validators(self):
        return { 'envidat_string_uppercase': validation.envidat_string_uppercase }
