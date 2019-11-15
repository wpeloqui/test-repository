# -*- coding: utf-8 -*-

#     Store Class Module.
#
#     This module defines the Store Class.
#
#     Example:
#         N/A
#
#     Attributes:
#         N/A
#
#     Todo:
#         N/A

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

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.store_model import StoreModel


class Store(Resource):

    def get(self, name):

        store = StoreModel.find_by_name(name)

        if store:
            return store.json()

        return {'message': "Store '{}' not found".format(name)}, 404

    def post(self, name):

        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' already exists".format(name)}, 404

        store = StoreModel(name)

        try:

            store.save_to_db()

        except Exception as err:
            return {'message': "Database Failed Creating '{}' with '{}'".format(name, err[0])}, 500

        return store.json(), 201

    def delete(self, name):

        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()

        return {'message': 'Store Deleted'}


class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}