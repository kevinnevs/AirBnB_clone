#!/usr/bin/python3
"""This module defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class describes data for city in a state"""
    name = ""
    state_id = ""
