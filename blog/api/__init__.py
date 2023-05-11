from combojsonapi.spec import ApiSpecPlugin


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            'Tags': 'Tags API'
        }
    )
    return api_spec_plugin
