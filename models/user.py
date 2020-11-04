#!/usr/bin/python3

""" User module """

from .base_model import BaseModel


class User(BaseModel):
    """ Class representing an user in the HBNB storage.
        Inherits from BaseModel.

        Attributes:
            email (string): User's email.
            password (string): User's password.
            first_name (string): User's first name.
            last_name (string): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
