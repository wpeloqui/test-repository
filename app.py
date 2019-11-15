# Copyright 2019 The Eclectic Engineer LLC

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'N8WP'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=600)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)   # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/register')

if __name__ == '__main__':

    from db import db   # Avoid circular dependencies

    db.init_app(app)
    app.run(port=5000, debug=True)