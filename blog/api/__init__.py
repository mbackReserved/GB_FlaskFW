from flask_combo_jsonapi import Api
from blog.api.tag import TagList, TagDetail
from combojsonapi.spec import ApiSpecPlugin


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        # Declaring tags list with their descriptions,
        # so API gets organized into groups. it's optional.
        tags={
            "Tag": "Tag API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(
        app,
        plugins=[
            api_spec_plugin,
        ],
    )

    
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")