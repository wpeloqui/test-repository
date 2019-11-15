# -*- coding: utf-8 -*-

#     User Class
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

from flask_restful import Resource, reqparse

from models.user_model import UserModel


class User(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Username cannot be blank!')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password cannot be blank!')

    def post(self):

        # This method adds a User to the database.
        #
        # Args:
        #     N/A
        #
        # Returns:
        #     A response message.

        data = User.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User '{}'already exists.".format(data['username'])}, 400

        user = UserModel(**data)  # The dictionary is unpacked with **
        user.save_to_db()

        return {'message': "User '{}' created successfully.".format(data['username'])}, 201
