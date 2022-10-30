#!/usr/bin/python3
from models import storage
from models.new_class import make_class
a = make_class("User")
print(a)
setattr(a, 'name', 'Mia')
print('__')
print(a.to_dict())
