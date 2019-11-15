# -*- coding: utf-8 -*-

#     UserModel Class
#
#     This module abstract a user.
#
#     Example:
#         N/A
#
#     Attributes:
#         id (int) user id
#         username (string) user's name
#         password (string) user's password
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


class UserModel(db.Model):

    # SQL Alchemy Configuration
    #
    #

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):

        # UserModel Constructor.
        #
        # Args:
        #     name (string) The item name.
        #     price (float) The item price.
        #
        # Returns:
        #     N/A

        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):

        # This method finds the User object by name and returns it.
        #
        # Args:
        #     username (string) The user's name.
        #
        # Returns:
        #     The class object, or None.

        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):

        # This method finds the User object by id and returns it.
        #
        # Args:
        #     id (int) The user's id.
        #
        # Returns:
        #     The class object, or None.

        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):

        # This method saves the User object to the database.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     N/A

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        # This method delete the User object from the database.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     N/A

        db.session.delete(self)
        db.session.commit()
