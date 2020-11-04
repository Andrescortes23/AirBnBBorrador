#!/usr/bin/python3
"""
Module that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""
