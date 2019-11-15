# -*- coding: utf-8 -*-

#     Item Class Module.
#
#     This module defines the Item Class.
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

from models.item_model import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='Every item requires a price.')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store id.')
    @jwt_required()
    def get(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            return item.json()

        return {'message': "Item '{}' not found.".format(name)}, 404

    def post(self, name):

        data = Item.parser.parse_args()

        if ItemModel.find_by_name(name):
            return {'message': "an item with name '{}' already exists.".format(name)}, 400

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": "An error occurred inserting the item. '{}'".format(e)}, 500

        return item.json(), 201

    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()

        return item.json(), 201

    def delete(self, name):

        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}, 201


class ItemList(Resource):

    def get(self):

        return {'items': [item.json() for item in ItemModel.query.all()]}
