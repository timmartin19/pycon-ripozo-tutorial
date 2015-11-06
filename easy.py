from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import restmixins, apimethod, translate, ListRelationship, Relationship, adapters
from ripozo.resources.fields.common import IntegerField
from ripozo_sqlalchemy import create_resource, ScopedSessionHandler

from common.models import Post, Comment, engine


app = Flask('easyapp')

session_handler = ScopedSessionHandler(engine)


dispatcher = FlaskDispatcher(app, url_prefix='/api')
dispatcher.register_resources(PostResource, CommentResource)
dispatcher.register_adapters(adapters.SirenAdapter, adapters.HalAdapter)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
