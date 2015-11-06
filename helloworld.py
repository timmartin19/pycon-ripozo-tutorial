from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from flask import Flask
from flask_ripozo import FlaskDispatcher
from ripozo import ResourceBase, adapters, apimethod, translate, fields, RequestContainer

app = Flask('helloworld')


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
