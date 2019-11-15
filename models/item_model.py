# -*- coding: utf-8 -*-

#     ItemModel Class
#
#     This module abstract an item.
#
#     Example:
#         N/A
#
#     Attributes:
#         name (string)
#         price (float)
#
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

from db import db


class ItemModel(db.Model):

    # SQL Alchemy Configuration
    #
    #

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):

        # ItemModel Constructor.
        #
        # Args:
        #     name: The item name.
        #     price: The item price.
        #     store_id: Store which stocks this item.
        #
        # Returns:
        #     N/A

        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):

        # This method will return a JSON representation of the ItemModel object as a dictionary.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     JSON representation of ItemModel attributes name and price.

        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):

        # This class method will find the ItemModel object by name.
        #
        # Args:
        #     name: The item name.
        #
        # Returns:
        #     ItemModel object or None.

        return cls.query.filter_by(name=name).first()

    def save_to_db(self):

        # This method saves the ItemModel object to the database.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     N/A

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        # This method delete the ItemModel object from the database.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     N/A

        db.session.delete(self)
        db.session.commit()
