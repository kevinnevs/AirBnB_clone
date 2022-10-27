#!/usr/bin/python3
"""module review. Holds a single class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review placed by user about the used Airbnb services"""
    place_id = ""
    user_id = ""
    text = ""
